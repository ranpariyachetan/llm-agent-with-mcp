import asyncio
from dotenv import load_dotenv
from model import LLM
from mcp_client import CalculatorMCPClient

class Calculator:
    def __init__(self):
        load_dotenv()
        self.llm = LLM()
        self.mcp_client = CalculatorMCPClient("http://127.0.0.1:8000/sse")

    async def init(self):
        """Initialize the calculator by connecting to the MCP server."""
        await self.mcp_client.connect()
        tools = await self.mcp_client.list_tools()
        self.llm.bind_tools(tools, self.mcp_client.mcp_session)

    async def close(self):
        """Close the MCP client connection."""
        await self.mcp_client.disconnect()

    async def add(self, a: int, b: int) -> str:
        """Adds two numbers."""
        return await self.llm.get_answer(f"Add {a} and {b}")

    async def subtract(self, a: int, b: int) -> str:
        """Subtracts two numbers."""
        return await self.llm.get_answer(f"Subtract {b} from {a}")

    async def multiply(self, a: int, b: int) -> str:
        """Multiplies two numbers."""
        return await self.llm.get_answer(f"Multiply {a} and {b}")

    async def divide(self, a: int, b: int) -> str:
        """Divides two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return await self.llm.get_answer(f"Divide {a} by {b}")

async def main():
    calculator = Calculator()

    await calculator.init()

    print("Adding 5 and 3:", await calculator.add(5, 3))
    await calculator.close()
    # Example usage
    # print("Adding 5 and 3:", await calculator.add(5, 3))
    # print("Subtracting 5 from 10:", await calculator.subtract(10, 5))
    # print("Multiplying 4 and 6:", await calculator.multiply(4, 6))
    # print("Dividing 8 by 2:", await calculator.divide(8, 2))

if __name__ == "__main__":
    asyncio.run(main())