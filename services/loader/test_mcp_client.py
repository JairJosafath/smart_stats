from services.loader.mcp_client import MCPClient
from llama_index.llms.ollama import Ollama
import asyncio


def test_mcp_client():
    async def run():
        client = MCPClient(
            url="http://localhost:6275/mcp",
            llm=Ollama(model="qwen3:0.6b"),
        )
        assert client is not None

        result = await client.interpret(
            info="""
                        Jimmy had 5 goals, 10 assists and 3 yellow cards.
                        """
        )

        print(f"Interpretation result: {result}")

    asyncio.run(run())
