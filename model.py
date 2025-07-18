import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage

class LLM:
    """A class to handle the initialization of the OpenAI model."""
    
    def __init__(self):
        load_dotenv()
        self.model = self.init_model()
        system_message = SystemMessage(
            content="""You are a helpful math assistant
            You can perform addition, subtraction, multiplicatin and division calculations.
            When a user asks for calculations, use your math expertise to calculate the result.
            If the user asks for a calculation that is not supported, politely inform them that you cannot perform that calculation.
            """
        )
        self.messages = [system_message]

    def init_model(self):
        """Initialize the OpenAI model."""
        return ChatOpenAI(
            model_name=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        )

    def bind_tools(self, tools):
        """Bind tools to the model."""
        self.model.bind_tools(tools)
        
    async def get_answer(self, question: str) -> str:
        """Get the answer to a question using the OpenAI model."""
        self.messages.append({"role": "user", "content": question})
        response = self.model.invoke(self.messages)
        answer = response.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer