// Independent JavaScript JSON Schema 2020-12 conformance against published artifacts.
import { readFileSync, readdirSync } from "node:fs";
import Ajv2020 from "ajv/dist/2020.js";
const ajv = new Ajv2020({ strict: false, validateFormats: false });
const dir = "schemas/v1";
const validators = {};
for (const name of readdirSync(dir).filter(f => f.endsWith(".schema.json"))) {
  const schema = JSON.parse(readFileSync(dir + "/" + name, "utf8"));
  const valid = ajv.compile(schema);
  validators[name.replace(".schema.json", "")] = valid;
}
for (const [name, type] of [["host-unmet","host-state"],["host-covered","host-state"]]) {
  const instance = JSON.parse(readFileSync("examples/portable/" + name + ".json", "utf8"));
  if (!validators[type](instance)) throw new Error(name + ": " + ajv.errorsText(validators[type].errors));
}
if (Object.keys(validators).length < 11) throw new Error("Missing published schemas");
console.log("Validated", Object.keys(validators).length, "JSON Schema contracts in Node.js");
