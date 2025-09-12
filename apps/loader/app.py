from services.loader.mcp_client import MCPClient
from llama_index.llms.ollama import Ollama
import os
from fastapi import FastAPI
import uvicorn

host = os.getenv("HOST", "http://localhost")
fast_api = FastAPI()

QWEN_06B_MODEL = "qwen3:0.6b"
QWEN_17B_MODEL = "qwen3:1.7b"
DEEPSEEK_R1_7B_MODEL = "deepseek-r1:7b"


async def app(info: str) -> list[dict]:
    client = MCPClient(
        url=f"{host}:9999/mcp",
        llm=Ollama(
            model=QWEN_06B_MODEL,
            base_url=f"{host}:11434",
            thinking=False,
            temperature=0,
        ),
    )

    result = await client.interpret(info)

    return result


@fast_api.post("/")
async def load(input: dict):
    info = input["content"]
    username = input["username"]
    instr = f"For a user with username {username}, the following stats were extracted: \n{info}.\n Store each of these stats in the database"

    result = await app(instr)

    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(fast_api, host="0.0.0.0", port=8000)
