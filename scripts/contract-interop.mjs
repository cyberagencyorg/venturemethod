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
const composedPath = process.env.VM_COMPOSITION_FILE;
if (composedPath) {
  const plan = JSON.parse(readFileSync(composedPath, "utf8"));
  if (!validators["composition-plan"](plan)) {
    throw new Error("Generated composition rejected: " + ajv.errorsText(validators["composition-plan"].errors));
  }
  if (plan.units.length) {
    const unsafe = structuredClone(plan);
    unsafe.units[0].unit.allowed_tools = ["shell"];
    if (validators["composition-plan"](unsafe)) throw new Error("Advisory schema permits shell tools");
    unsafe.units[0].unit.allowed_tools = [];
    unsafe.units[0].unit.authorized_effects = ["external_write"];
    if (validators["composition-plan"](unsafe)) throw new Error("Advisory schema permits external writes");
    const invalidReview = structuredClone(plan);
    invalidReview.units[0].unit.review.status = "accepted";
    if (validators["composition-plan"](invalidReview)) throw new Error("Advisory schema permits self-approved work");
  }
}
if (Object.keys(validators).length < 12) throw new Error("Missing published schemas");
console.log("Validated", Object.keys(validators).length, "JSON Schema contracts in Node.js");
