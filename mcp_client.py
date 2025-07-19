from mcp.client.session import ClientSession
from mcp.client.sse import sse_client
from langchain_core.tools import StructuredTool

class CalculatorMCPClient:
    def __init__(self, server_url: str):
        self.server_url = server_url

    async def connect(self):
        """Connect to the MCP server."""
        self.client = sse_client(self.server_url)
        read, write = await self.client.__aenter__()
        self.session_context = ClientSession(read, write)
        self.mcp_session = await self.session_context.__aenter__()
        await self.mcp_session.initialize()

    async def list_tools(self):
        """List available tools on the MCP server."""
        tools_response = await self.mcp_session.list_tools()
        langchain_tools = []
        for tool in tools_response.tools:
            print(f"Tool: {tool.name}, Description: {tool.description}")
            langchain_tools.append(StructuredTool(
                name=tool.name,
                description=tool.description,
                func=lambda *args, **kwargs: self.session_context.call_tool(tool.name, args, kwargs),
                args_schema=tool.inputSchema,
            ))
        return langchain_tools

    async def disconnect(self):
        """Close the MCP session."""
        await self.session_context.__aexit__(None, None, None)
        await self.client.__aexit__(None, None, None)