from services.loader.mcp_client import MCPClient
from llama_index.llms.ollama import Ollama
import asyncio

host = "http://localhost"
docker_host = "http://host.docker.internal"

QWEN_06B_MODEL = "qwen3:0.6b"
QWEN_17B_MODEL= "qwen3:1.7b"
DEEPSEEK_R1_7B_MODEL = "deepseek-r1:7b"

async def main() -> None:
    client = MCPClient(
        url=f"{host}:9999/mcp",
        llm=Ollama(model=DEEPSEEK_R1_7B_MODEL, base_url=f"{host}:11434", thinking=False, temperature=.9),
    )
    

    result = await client.interpret(
        info="""
                     get the user named 'JohnDoe' from the database and add a stat 'high_score' with value '1500' for that user.
                    """
    )

    print(f"Interpretation result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
