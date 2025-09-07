from llama_index.tools.mcp import BasicMCPClient, McpToolSpec
from services.loader.agent import InterpreterAgent
from llama_index.llms.bedrock_converse import BedrockConverse
from llama_index.llms.ollama import Ollama


class MCPClient:
    def __init__(self, url: str, llm: Ollama | BedrockConverse):
        self.spec = McpToolSpec(BasicMCPClient(url))
        self.llm = llm

    async def interpret(self, info: str):
        tools = await self.spec.to_tool_list_async()
        self.agent = InterpreterAgent(llm=self.llm, tools=tools)
        result = await self.agent.interpret(info=info)

        return result
