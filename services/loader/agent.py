from llama_index.llms.bedrock_converse import BedrockConverse
from llama_index.llms.ollama import Ollama
from llama_index.core.agent.workflow import FunctionAgent, ToolCall, ToolCallResult
from llama_index.core.workflow import Context, Event
from llama_index.core.tools import FunctionTool


class InterpreterAgent:
    def __init__(self, llm: Ollama | BedrockConverse, tools: list[FunctionTool]):
        self.system_prompt = """
           You are an AI assistant for Tool Calling.
You need to work with tools.

First make sure you understand what actions to take.
Plan those actions out step by step.
Then call the tools you need to complete the task.

Sometimes you need to use the output of one tool as input to another tool.

You must use tools to complete the task.
            """
        self.llm = llm
        self.tools = tools
        self.set_agent()

    async def interpret(self, info: str):
        print(f"""Agent info:
              input: {info}
              model: {self.llm.model}
              host: {
            self.llm.base_url if isinstance(self.llm, Ollama) else self.llm.endpoint_url
        }
              tools: {
            [
                f"name:{tool.metadata.get_name()} descr:{tool.metadata.description} \
                        "
                for tool in self.tools
            ]
        }""")

        agent = self.agent

        context = Context(agent)

        handler = agent.run(info, ctx=context)

        print("Starting to stream events...")

        tool_calls: list[Event] = []

        async for event in handler.stream_events():
            # log ALL event types while debugging
            print(f"[{event.__class__.__name__}]")
            if isinstance(event, ToolCall):
                print(f"Calling tool {event.tool_name} with kwargs {event.tool_kwargs}")
                tool_calls.append(event)
            elif isinstance(event, ToolCallResult):
                print(f"Tool {event.tool_name} returned {event.tool_output}")
                tool_calls.append(event)

        return [tool_call.model_dump() for tool_call in tool_calls]

    def set_agent(self):
        agent = FunctionAgent(
            name="Agent",
            llm=self.llm,
            tools=self.tools,
            description="An agent that can work with Tools.",
            system_prompt=self.system_prompt,
            streaming=False,
        )
        self.agent = agent
