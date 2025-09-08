from llama_index.llms.bedrock_converse import BedrockConverse
from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import FunctionAgent, ToolCall, ToolCallResult
from llama_index.core.workflow import Context
from llama_index.core.tools import FunctionTool


class InterpreterAgent:
    def __init__(self, llm: Ollama | BedrockConverse, tools: list[FunctionTool]):
        self.system_prompt = """
           You are an AI assistant for Tool Calling.
You need to work with tools.
            """
        self.llm = llm
        self.tools = tools
        self.set_agent()

    async def interpret(self, info: str):
        for tool in self.tools:
            print(
                f"><><><><><><<><> Tool available: {tool.metadata.get_name()} - {tool.metadata.description}"
            )
        agent = self.agent
        
        context = Context(agent)

        handler = agent.run(info, ctx=context)

        print("Starting to stream events...")

        saw_tool = False

        async for event in handler.stream_events():
            # log ALL event types while debugging
            print(f"[{event.__class__.__name__}]")
            if isinstance(event, ToolCall):
                saw_tool = True
                print(f"Calling tool {event.tool_name} with kwargs {event.tool_kwargs}")
            elif isinstance(event, ToolCallResult):
                print(f"Tool {event.tool_name} returned {event.tool_output}")

        if not saw_tool:
            print("No ToolCall events were emitted during streaming.")
        return "OK"
    
    def set_agent(self):
        agent = FunctionAgent(
            name="Agent",
            llm=self.llm,
            tools=self.tools,
            description="An agent that can work with Tools.",
            system_prompt=self.system_prompt,
            streaming=False
        )
        self.agent= agent
