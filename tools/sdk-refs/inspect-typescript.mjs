// Inspect the published declarations with the compiler, preserving overloads,
// optional properties, union constraints, and nested request types.
import fs from "node:fs";
import ts from "typescript";

const file = ts.createSourceFile(process.argv[2], fs.readFileSync(process.argv[2], "utf8"),
  ts.ScriptTarget.Latest, true, ts.ScriptKind.TS);
if (file.parseDiagnostics.length) throw new Error("Cannot parse published declarations");
const declarations = new Map(file.statements.filter(s => s.name).map(s => [s.name.text, s]));
const values = new Map(file.statements.filter(ts.isVariableStatement)
  .flatMap(s => s.declarationList.declarations.map(d => [d.name.getText(file), d])));
const text = node => node.getText(file);
const description = node => (node.jsDoc || []).map(doc =>
  typeof doc.comment === "string" ? doc.comment : doc.comment?.map(text).join("") || ""
).join("\n\n");
const references = node => {
  const found = new Set();
  function visit(n) {
    if (ts.isTypeReferenceNode(n)) found.add(text(n.typeName));
    if (ts.isExpressionWithTypeArguments(n)) found.add(text(n.expression));
    ts.forEachChild(n, visit);
  }
  visit(node);
  return [...found].filter(name => declarations.has(name));
};
const namespaces = [];
const pending = new Set(["GoodmemConfig", "RequestOptions"]);
for (const property of declarations.get("Goodmem").members) {
  if (!ts.isPropertyDeclaration(property) || property.name.text === "raw") continue;
  const api = declarations.get(text(property.type));
  if (!api || !ts.isClassDeclaration(api)) throw new Error("Missing namespace declaration");
  const methods = [];
  for (const method of api.members) {
    if (!ts.isMethodDeclaration(method) || method.modifiers?.some(m =>
      [ts.SyntaxKind.PrivateKeyword, ts.SyntaxKind.ProtectedKeyword, ts.SyntaxKind.StaticKeyword].includes(m.kind))) continue;
    method.parameters.forEach(p => references(p).forEach(name => pending.add(name)));
    methods.push({name: text(method.name), signature: text(method).replace(/;$/, ""),
      description: description(method), parameters: method.parameters.map(p => ({
        name: text(p.name), type: text(p.type), optional: !!p.questionToken,
      }))});
  }
  namespaces.push({name: property.name.text, methods});
}
const models = [];
const seen = new Set();
for (const name of pending) {
  if (seen.has(name)) continue;
  seen.add(name);
  const node = declarations.get(name);
  if (!node) throw new Error(`Missing request type ${name}`);
  if (!ts.isInterfaceDeclaration(node) && !ts.isTypeAliasDeclaration(node))
    throw new Error(`Unsupported request type ${name}`);
  references(node).forEach(ref => pending.add(ref));
  const fields = ts.isInterfaceDeclaration(node) ? node.members.filter(ts.isPropertySignature).map(p => ({
    name: text(p.name), type: text(p.type), optional: !!p.questionToken, description: description(p),
  })) : [];
  models.push({name, description: description(node), fields, declaration: text(node),
    definition: ts.isTypeAliasDeclaration(node) ? text(node.type) : null,
    valueDeclaration: values.has(name) ? "export declare const " + text(values.get(name)) + ";" : null,
    bases: node.heritageClauses?.flatMap(h => h.types.map(text)) || []});
}
process.stdout.write(JSON.stringify({namespaces, models: models.sort((a, b) => a.name.localeCompare(b.name, "en"))}));
