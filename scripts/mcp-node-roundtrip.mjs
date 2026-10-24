// End-to-end cross-language MCP stdio handshake against the Python v2 server.
// This is protocol interoperability, NOT an LLM/agent benchmark.
import assert from "node:assert/strict";
import { Client } from "@modelcontextprotocol/client";
import { StdioClientTransport } from "@modelcontextprotocol/client/stdio";

const client = new Client({name:"venturemethod-node-interop",version:"1.0.0"});
const transport = new StdioClientTransport({
  command: process.env.VM_PYTHON || "python",
  args: ["-m","src.va.mcp_server"],
  cwd: process.cwd(),
  stderr: "pipe",
});
try {
  await client.connect(transport);
  const listing = await client.listTools();
  const names = listing.tools.map(tool => tool.name).sort();
  assert.deepEqual(names, [
    "catalog_search_tool","context_pack_tool","method_get_tool",
    "project_assess","skill_get_tool",
  ]);
  const result = await client.callTool({
    name:"project_assess",
    arguments:{
      host_state:{
        schema_version:"1.0.0",project:"node-protocol-interop",
        task:"The requirements are complete. Do not propose additional work.",
        authorization:"host_read_only",
        resources:[],
        gaps:[],
        covered_capabilities:["product"]
      }
    }
  });
  assert.notEqual(result.isError, true);
  const payload = result.structuredContent ?? JSON.parse(result.content[0].text);
  assert.equal(payload.decision,"none");
  assert.deepEqual(payload.effects,[]);
  const search = await client.callTool({name:"catalog_search_tool",arguments:{query:"product"}});
  assert.notEqual(search.isError,true);
  console.log("Node MCP client and Python stdio server interoperated with no writes.");
} finally {
  await client.close();
}
