"""Optional, local-only MCP tools. This module exposes no host file-reading or writes.

Install with pip install '.[mcp]' and run \`venturemethod-mcp\`.
Transport is stdio. Do not expose as a hosted endpoint without a separate
authenticated design and threat review.
"""
from __future__ import annotations
from mcp.server import MCPServer

from .portable import catalog_search, method_get, skill_get, assess, context_pack, work_plan, provider_catalog
from .composition_v1 import compose

mcp = MCPServer("Khan's Venture Method", instructions=(
    "Read-only professional reference library. Host owns context and authority. "
    "Use project_assess only with specifically authorized host state. "
    "Recommendations are not execution or independent verification."
))


@mcp.tool()
def catalog_search_tool(query: str, limit: int = 6) -> dict:
    """Search portable capability metadata; results are advisory only."""
    return catalog_search(query, limit)


@mcp.tool()
def method_get_tool(method_id: str) -> dict:
    """Retrieve a sourced method record by exact catalog ID."""
    return method_get(method_id)


@mcp.tool()
def skill_get_tool(skill_id: str) -> dict:
    """Retrieve a first-party skill as a bounded reference document."""
    return skill_get(skill_id)


@mcp.tool()
def project_assess(host_state: dict) -> dict:
    """Assess only the host's explicitly supplied, read-only project context."""
    return assess(host_state)


@mcp.tool()
def context_pack_tool(host_state: dict, max_chars: int = 8000) -> dict:
    """Build a bounded, optional skill packet from supplied host context."""
    return context_pack(host_state, max_chars)



@mcp.tool()
def work_plan_tool(host_state: dict) -> dict:
    """Return a typed advisory work proposal with no authority or side effects."""
    return work_plan(host_state)


@mcp.tool()
def providers_get_tool() -> dict:
    """Return versioned first-party skill provider maturity and permissions."""
    return provider_catalog()



@mcp.tool()
def composition_plan_tool(host_state: dict, max_units: int = 3) -> dict:
    """Propose bounded evidence-based work units with explicit prerequisites. No execution."""
    return compose(host_state, max_units=max_units)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
