from llama_index.llms.bedrock_converse import BedrockConverse
from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import FunctionAgent, ToolCall, ToolCallResult
from llama_index.core.workflow import Context
from llama_index.core.tools import FunctionTool


class InterpreterAgent:
    def __init__(self, llm: Ollama | BedrockConverse, tools: list[FunctionTool]):
        llm.system_prompt = """
           You are an AI assistant for Tool Calling.
You need to work with tools.
            """
        self.llm = llm
        self.tools = tools

    async def interpret(self, info: str):
        for tool in self.tools:
            print(
                f"><><><><><><<><>Tool available: {tool.metadata.get_name()} - {tool.metadata.description}"
            )
        agent = FunctionAgent(
            name="InterpreterAgent",
            llm=self.llm,
            tools=self.tools,
            description="An agent that can work with Tools.",
            system_prompt=self.llm.system_prompt,
        )
        context = Context(agent)

        handler = agent.run(info, ctx=context)

        print("Starting to stream events...")

        async for event in handler.stream_events():
            if type(event) is ToolCall:
                print(f"Calling tool {event.tool_name} with kwargs {event.tool_kwargs}")
            elif type(event) is ToolCallResult:
                print(f"Tool {event.tool_name} returned {event.tool_output}")

        return "OK"
