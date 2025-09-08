from services.loader.mcp_client import MCPClient
from llama_index.llms.ollama import Ollama
import asyncio


async def run():
    client = MCPClient(
        url="http://localhost:6275/mcp",
        llm=Ollama(model="qwen3:0.6b"),
    )
    assert client is not None

    result = await client.interpret(
        info="""
                     get the user named 'JohnDoe' from the database and add a stat 'high_score' with value '1500' for that user.
                    """
    )

    print(f"Interpretation result: {result}")


if __name__ == "__main__":
    asyncio.run(run())
