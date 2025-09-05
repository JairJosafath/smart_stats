from llama_index.llms.bedrock_converse import BedrockConverse
from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context
from llama_index.core.tools import FunctionTool


class InterpreterAgent:
    def __init__(self, llm: Ollama | BedrockConverse, tools: list[FunctionTool]):
        llm.system_prompt = """
            You are an AI assistant for Tool Calling. You need to work with tools
            You will get information that will contain stats from a game. You should call the appropriate tools to insert the stats into the database.
            """
        self.llm = llm
        self.tools = tools

    def interpret(self, info: str):
        agent = FunctionAgent(
            name="InterpreterAgent",
            llm=self.llm,
            tools=self.tools,
            description="Agent to interpret game stats and call appropriate tools",
            system_prompt=self.llm.system_prompt,
        )
        context = Context(agent)

        return agent.run(user_msg=info, ctx=context)
