import asyncio
from dotenv import load_dotenv
from model import LLM
from mcp_client import CalculatorMCPClient
from langchain_core.messages import ToolMessage

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
        return await self._perform_calculation("Add", a, b)

    async def subtract(self, a: int, b: int) -> str:
        """Subtracts two numbers."""
        return await self._perform_calculation("Subtract", a, b)

    async def multiply(self, a: int, b: int) -> str:
        """Multiplies two numbers."""
        return await self._perform_calculation("Multiply", a, b)

    async def divide(self, a: int, b: int) -> str:
        """Divides two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return await self._perform_calculation("Divide", a, b)

    async def _perform_calculation(self, operation: str, a: int, b: int) -> str:
        """Perform a calculation using the LLM."""
        print(f"Performing {operation} on {a} and {b}")
        res = self.llm.start_chat(f"{operation} {a} and {b}")
        
        if res.tool_calls:
                tool_response = await self.mcp_client.mcp_session.call_tool(res.tool_calls[0]["name"], res.tool_calls[0]["args"])
                result = tool_response.content[0].text
                
                tool_message = ToolMessage(
                    content=result,
                    tool_call_id=res.tool_calls[0]["id"],
                )

                return tool_message.content

        return res.content
    
async def main():
    calculator = Calculator()

    await calculator.init()

    print("Adding 5 and 3:", await calculator.add(5, 3))
    print("Subtracting 5 from 10:", await calculator.subtract(10, 5))
    print("Multiplying 4 and 6:", await calculator.multiply(4, 6))
    print("Dividing 8 by 2:", await calculator.divide(8, 2))

    await calculator.close()
    # Example usage
    # print("Adding 5 and 3:", await calculator.add(5, 3))
    # print("Subtracting 5 from 10:", await calculator.subtract(10, 5))
    # print("Multiplying 4 and 6:", await calculator.multiply(4, 6))
    # print("Dividing 8 by 2:", await calculator.divide(8, 2))

if __name__ == "__main__":
    asyncio.run(main())