import asyncio
from dotenv import load_dotenv

class Calculator:
    def __init__(self):
        load_dotenv()

    async def add(self, a: int, b: int) -> int:
        """Adds two numbers."""
        return a + b

    async def subtract(self, a: int, b: int) -> int:
        """Subtracts two numbers."""
        return a - b

    async def multiply(self, a: int, b: int) -> int:
        """Multiplies two numbers."""
        return a * b

    async def divide(self, a: int, b: int) -> float:
        """Divides two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    
async def main():
    calculator = Calculator()

    # Example usage
    print("Adding 5 and 3:", await calculator.add(5, 3))
    print("Subtracting 5 from 10:", await calculator.subtract(10, 5))
    print("Multiplying 4 and 6:", await calculator.multiply(4, 6))
    print("Dividing 8 by 2:", await calculator.divide(8, 2))

if __name__ == "__main__":
    asyncio.run(main())