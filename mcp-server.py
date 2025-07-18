from mcp.server import FastMCP
import asyncio

app = FastMCP("calculator")

@app.tool()
async def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

@app.tool()
async def subtract(a: int, b: int) -> int:
    """Subtracts two numbers."""
    return a - b

@app.tool()
async def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

@app.tool()
async def divide(a: int, b: int) -> float:
    """Divides two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Starting MCP server...")
    asyncio.run(app.run(transport="sse"))