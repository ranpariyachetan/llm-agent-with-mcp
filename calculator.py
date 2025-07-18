import asyncio
from dotenv import load_dotenv
from model import LLM

class Calculator:
    def __init__(self):
        load_dotenv()
        self.llm = LLM()

    async def add(self, a: int, b: int) -> str:
        """Adds two numbers."""
        return await self.llm.get_answer(f"Add {a} and {b}")

    async def subtract(self, a: int, b: int) -> str:
        """Subtracts two numbers."""
        return await self.llm.get_answer(f"Subtract {b} from {a}")
        # Note: The original code had a typo in 'return'
        return a - b

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

    # Example usage
    print("Adding 5 and 3:", await calculator.add(5, 3))
    print("Subtracting 5 from 10:", await calculator.subtract(10, 5))
    print("Multiplying 4 and 6:", await calculator.multiply(4, 6))
    print("Dividing 8 by 2:", await calculator.divide(8, 2))

if __name__ == "__main__":
    asyncio.run(main())