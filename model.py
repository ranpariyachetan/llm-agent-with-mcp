import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage

class LLM:
    """A class to handle the initialization of the OpenAI model."""
    
    def __init__(self):
        load_dotenv()
        self.model = self.init_model()
        self.system_message = SystemMessage(
            content="""You are a helpful math assistant
            You can perform addition, subtraction, multiplicatin and division calculations.
            You are given tools to perform calculations. You must use these tools to perform these 4 math operations.
            You can only perform these 4 operations.
            When a user asks for calculations, use appropriate tool from the given tools.
            If the user asks for a calculation that is not supported, politely inform them that you cannot perform that calculation.
            """
        )

    def init_model(self):
        """Initialize the OpenAI model."""
        return ChatOpenAI(
            model_name=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
        )

    def bind_tools(self, tools, mcp_session):
        """Bind tools to the model."""
        self.model = self.model.bind_tools(tools)
        self.mcp_session = mcp_session

    def start_chat(self, question: str):
        """Start a chat with the model."""
        messages = [self.system_message]
        messages.append({"role": "user", "content": question})
        response = self.model.invoke(messages)

        return response