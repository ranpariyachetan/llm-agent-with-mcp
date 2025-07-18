import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.sse import sse_client
async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["mcp-server.py"]
    )

    async with sse_client(url="http://127.0.0.1:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:

            print("Connecting to MCP server...")
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")
            # print(tools.tools)

if __name__ == "__main__":
    asyncio.run(main())