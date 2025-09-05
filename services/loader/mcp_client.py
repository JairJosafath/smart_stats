from llama_index.tools.mcp import BasicMCPClient, McpToolSpec
from services.loader.agent import InterpreterAgent
from llama_index.llms.bedrock_converse import BedrockConverse
from llama_index.llms.ollama import Ollama


class MCPClient:
    def __init__(self, url: str, llm: Ollama | BedrockConverse):
        spec = McpToolSpec(BasicMCPClient(command_or_url=url))
        tools = spec.to_tool_list()
        self.agent = InterpreterAgent(llm=llm, tools=tools)

    def interpret(self, info: str):
        return self.agent.interpret(info=info)
