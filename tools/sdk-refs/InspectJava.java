import com.sun.source.tree.*;
import com.sun.source.util.*;
import com.sun.source.doctree.ParamTree;
import com.sun.source.doctree.SnippetTree;
import java.net.URI;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.zip.ZipFile;
import javax.lang.model.element.Modifier;
import javax.tools.*;

// Parse public source declarations using javac's syntax tree; no SDK dependencies
// or compilation of the downloaded sources is needed.
class InspectJava {
    static ZipFile jar;
    static final String ROOT = "ai/pairsys/goodmem/client/";
    static final Set<String> models = new TreeSet<>();
    static void modelsIn(String type) {
        var names = java.util.regex.Pattern.compile("[A-Za-z_$][\\w$]*").matcher(type);
        while (names.find()) if (jar.getEntry(ROOT + "models/" + names.group() + ".java") != null)
            models.add(names.group());
    }
    static class Source extends SimpleJavaFileObject {
        final String source;
        Source(String path) throws Exception {
            super(URI.create("string:///" + path), Kind.SOURCE);
            source = new String(jar.getInputStream(jar.getEntry(path)).readAllBytes(), StandardCharsets.UTF_8);
        }
        public CharSequence getCharContent(boolean ignored) { return source; }
    }
    record Parsed(CompilationUnitTree unit, ClassTree type, DocTrees docs) {}
    static Parsed parse(String path) throws Exception {
        var compiler = ToolProvider.getSystemJavaCompiler();
        var task = (JavacTask) compiler.getTask(null, null, null, List.of("-proc:none"), null, List.of(new Source(path)));
        var unit = task.parse().iterator().next();
        var type = (ClassTree) unit.getTypeDecls().stream().filter(t -> t instanceof ClassTree).findFirst().orElseThrow();
        return new Parsed(unit, type, DocTrees.instance(task));
    }
    static String encode(String text) { return Base64.getEncoder().encodeToString(text.getBytes(StandardCharsets.UTF_8)); }
    static String parameter(VariableTree parameter) {
        String type = parameter.getType().toString();
        // javac represents varargs as an array type; its variable printer retains
        // the ellipsis flag. Preserve it while leaving real array parameters alone.
        if (type.endsWith("[]") && parameter.toString().endsWith("... " + parameter.getName()))
            type = type.substring(0, type.length() - 2) + "...";
        return type + " " + parameter.getName();
    }
    static String description(Parsed parsed, Tree member) {
        var comment = parsed.docs.getDocCommentTree(TreePath.getPath(parsed.unit, member));
        if (comment == null) return "";
        var result = new StringBuilder();
        for (var node : comment.getFullBody()) {
            if (node instanceof SnippetTree snippet && snippet.getBody() != null) {
                var code = snippet.getBody().getBody().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;");
                result.append("\n```java\n").append(code).append("\n```\n");
            } else result.append(node);
        }
        return result.toString();
    }
    public static void main(String[] args) throws Exception {
        try (var opened = new ZipFile(args[0])) {
            jar = opened;
            var root = ROOT;
            var client = parse(root + "Goodmem.java");
            var namespaces = new TreeMap<String, String>();
            for (var member : client.type.getMembers()) {
                if (member instanceof VariableTree field && field.getModifiers().getFlags().contains(Modifier.PUBLIC)
                        && field.getType().toString().endsWith("API") && !field.getName().contentEquals("raw"))
                    namespaces.put(field.getName().toString(), field.getType().toString());
            }
            for (var ns : namespaces.entrySet()) {
                var methods = new TreeMap<String, String[]>();
                for (var path : List.of(root + "internal/apibase/" + ns.getValue() + "Base.java", root + "api/" + ns.getValue() + ".java")) {
                    var parsed = parse(path);
                    for (var member : parsed.type.getMembers()) {
                        if (!(member instanceof MethodTree method) || method.getReturnType() == null
                                || !method.getModifiers().getFlags().contains(Modifier.PUBLIC)
                                || method.getModifiers().getFlags().contains(Modifier.STATIC)) continue;
                        var params = String.join(", ", method.getParameters().stream().map(InspectJava::parameter).toList());
                        method.getParameters().forEach(p -> modelsIn(p.getType().toString()));
                        var key = method.getName() + "(" + params + ")";
                        var doc = description(parsed, method);
                        if (methods.containsKey(key)) doc = doc.replace("{@inheritDoc}", methods.get(key)[1]);
                        methods.put(key, new String[] {method.getReturnType() + " " + key, doc});
                    }
                }
                for (var method : methods.entrySet()) System.out.println("method\t" + String.join("\t",
                    encode(ns.getKey()), encode(method.getKey()), encode(method.getValue()[0]), encode(method.getValue()[1])));
            }
            var visited = new HashSet<String>();
            while (!visited.containsAll(models)) {
                var name = models.stream().filter(n -> !visited.contains(n)).findFirst().orElseThrow();
                visited.add(name);
                var parsed = parse(root + "models/" + name + ".java");
                var path = TreePath.getPath(parsed.unit, parsed.type);
                var doc = description(parsed, parsed.type);
                var fields = new HashMap<String, String>();
                var comment = parsed.docs.getDocCommentTree(path);
                if (comment != null) for (var tag : comment.getBlockTags()) {
                    if (tag instanceof ParamTree param && !param.isTypeParameter())
                        fields.put(param.getName().toString(), String.join("", param.getDescription().stream().map(Object::toString).toList()));
                }
                System.out.println("model\t" + String.join("\t", encode(name), encode(doc == null ? "" : doc)));
                for (var permitted : parsed.type.getPermitsClause()) {
                    modelsIn(permitted.toString());
                    System.out.println("variant\t" + encode(name) + "\t" + encode(permitted.toString()));
                }
                for (var member : parsed.type.getMembers()) {
                    if (!(member instanceof VariableTree field)) continue;
                    var isEnum = parsed.type.getKind() == Tree.Kind.ENUM;
                    if (isEnum && !field.getModifiers().getFlags().contains(Modifier.PUBLIC)) continue;
                    if (!isEnum && field.getModifiers().getFlags().contains(Modifier.STATIC)) continue;
                    modelsIn(field.getType().toString());
                    System.out.println("field\t" + String.join("\t", encode(name), encode(field.getName().toString()),
                        encode(field.getType().toString()), encode(fields.getOrDefault(field.getName().toString(), ""))));
                }
            }
        }
    }
}
