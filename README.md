In this repository I have tried to mimic LLM agent which uses LLM and tools exposed from MCP server to answer question by the user. 

This is a similar use case as using agents like [Cursor](https://cursor.com/en), [Claude Desktop](https://claude.ai/download), [Co-Pilot](https://github.com/features/copilot) etc.

About code
-----------
1. `mcp_server.py` - Runs MCP server.
2. `mcp_client.py` - Creates MCP Client that connects to the MCP server.
3. `model.py` - Wrapper class around LLM model. As of now using OpenAIChat model via langchain.
3. `calculator.py` - Calculator agent which interacts with model to perform math operations.

MCP Server
-----------
MCP server in this example, exposes 4 tools for basic math operations, `add`, `subtract`, `multiply` and `divide`.

LLM
-----------
LLM wrapper creates and instance of OpenAIChat model, provides system message with appropriate prompt. It also triggers tool call when the model returns response with tool calls.


How to run?
-----------
```
python mcp_server.py & python calculator.py
```