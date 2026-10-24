"""A genuine MCP protocol round trip without external network or host credentials."""
import asyncio
import hashlib
import unittest
from mcp import Client
from src.va.mcp_server import mcp


class MCPRoundTripTests(unittest.TestCase):
    def test_read_only_tool_registration_and_live_protocol(self):
        async def exercise():
            async with Client(mcp) as client:
                available = await client.list_tools()
                names = {item.name for item in available}
                self.assertEqual(names, {
                    "catalog_search_tool", "method_get_tool", "skill_get_tool",
                    "project_assess", "context_pack_tool"
                })
                res = await client.call_tool("method_get_tool", {"method_id": "opportunity-solution-tree"})
                self.assertFalse(res.is_error)
                assess_state = {
                    "schema_version": "1.0.0", "project": "test", "task": "Review a draft",
                    "authorization": "host_read_only", "covered_capabilities": [],
                    "resources": [{"id": "file:README.md", "sha256": hashlib.sha256(b"ok").hexdigest()}],
                    "gaps": []
                }
                result = await client.call_tool("project_assess", {"host_state": assess_state})
                self.assertFalse(result.is_error)
                self.assertEqual(result.structured_content["decision"], "none")
        asyncio.run(exercise())


if __name__ == "__main__":
    unittest.main()
