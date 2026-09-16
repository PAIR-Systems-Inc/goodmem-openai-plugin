using System.Reflection;
using System.Runtime.Loader;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Xml.Linq;

var assembly = AssemblyLoadContext.Default.LoadFromAssemblyPath(Path.GetFullPath(args[0]));
var docs = XDocument.Load(args[1]).Descendants("member")
    .ToDictionary(e => e.Attribute("name")!.Value, e => e);
var nullability = new NullabilityInfoContext();
var pending = new Queue<Type>();
var seen = new HashSet<Type>();
var namespaces = new List<object>();
var models = new List<object>();
const BindingFlags flags = BindingFlags.Public | BindingFlags.Instance;

string Doc(string id) => docs.TryGetValue(id, out var e)
    ? string.Join(" ", (e.Element("summary")?.Value ?? "").Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries)) : "";
string XmlType(Type t) => t.IsGenericType
    ? t.GetGenericTypeDefinition().FullName!.Split('`')[0] + "{" + string.Join(",", t.GenericTypeArguments.Select(XmlType)) + "}"
    : t.FullName!;
string TypeName(Type t, NullabilityInfo? info = null) {
    if (t.IsArray) return TypeName(t.GetElementType()!, info?.ElementType) + "[]";
    if (Nullable.GetUnderlyingType(t) is Type value) return TypeName(value) + "?";
    var name = t == typeof(string) ? "string" : t == typeof(bool) ? "bool" : t == typeof(int) ? "int"
        : t == typeof(long) ? "long" : t == typeof(double) ? "double" : t == typeof(float) ? "float"
        : t == typeof(byte) ? "byte" : t == typeof(object) ? "object" : t == typeof(void) ? "void" : t.Name.Split('`')[0];
    if (t.IsGenericType) name += "<" + string.Join(", ", t.GenericTypeArguments.Select((g, i) =>
        TypeName(g, info?.GenericTypeArguments.ElementAtOrDefault(i)))) + ">";
    if (!t.IsValueType && info?.ReadState == NullabilityState.Nullable) name += "?";
    return name;
}
void Visit(Type t) {
    if (t.IsArray) { Visit(t.GetElementType()!); return; }
    foreach (var arg in t.GenericTypeArguments) Visit(arg);
    if (t.Assembly == assembly && !seen.Contains(t)) { seen.Add(t); pending.Enqueue(t); }
}
foreach (var ns in assembly.GetType("Goodmem.Client.GoodmemClient")!.GetProperties(flags).OrderBy(p => p.Name, StringComparer.Ordinal)) {
    if (ns.PropertyType.Namespace != "Goodmem.Client.Api" || !ns.PropertyType.Name.EndsWith("Api")) continue;
    var methods = new List<object>();
    foreach (var method in ns.PropertyType.GetMethods(flags | BindingFlags.DeclaredOnly)
        .Where(m => !m.IsSpecialName).OrderBy(m => m.Name, StringComparer.Ordinal).ThenBy(m => m.ToString(), StringComparer.Ordinal)) {
        var parameters = method.GetParameters();
        foreach (var p in parameters) Visit(p.ParameterType);
        var signature = TypeName(method.ReturnType, nullability.Create(method.ReturnParameter)) + " " + method.Name + "(" +
            string.Join(", ", parameters.Select(p => TypeName(p.ParameterType, nullability.Create(p)) + " " + p.Name +
                (p.HasDefaultValue ? p.ParameterType.IsValueType ? " = default" : " = null" : ""))) + ")";
        var id = "M:" + method.DeclaringType!.FullName + "." + method.Name +
            (parameters.Length > 0 ? "(" + string.Join(",", parameters.Select(p => XmlType(p.ParameterType))) + ")" : "");
        methods.Add(new { name = method.Name, signature, description = Doc(id) });
    }
    namespaces.Add(new { name = ns.Name, methods });
}
while (pending.TryDequeue(out var model)) {
    var fields = new List<object>();
    if (model.IsEnum) {
        foreach (var field in model.GetFields(BindingFlags.Public | BindingFlags.Static))
            fields.Add(new { name = field.Name, type = model.Name, description = Doc("F:" + model.FullName + "." + field.Name) });
    } else {
        foreach (var p in model.GetProperties(flags).OrderBy(p => p.Name, StringComparer.Ordinal)) {
            Visit(p.PropertyType);
            fields.Add(new { name = p.Name, type = TypeName(p.PropertyType, nullability.Create(p)),
                required = p.CustomAttributes.Any(a => a.AttributeType.Name == "RequiredMemberAttribute"),
                wire = p.GetCustomAttribute<JsonPropertyNameAttribute>()?.Name,
                description = Doc("P:" + p.DeclaringType!.FullName + "." + p.Name) });
        }
    }
    models.Add(new { name = model.Name, fullName = model.FullName, description = Doc("T:" + model.FullName),
        isEnum = model.IsEnum, fields });
}
Console.Write(JsonSerializer.Serialize(new { namespaces, models }));
