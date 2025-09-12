from services.loader.mcp_client import MCPClient
from llama_index.llms.ollama import Ollama
import os
from fastapi import FastAPI, UploadFile, Form
from typing import Annotated
import uvicorn
import requests
import httpx

host = os.getenv("HOST", "http://localhost")
extractor_service_url = os.getenv("EXTRACTOR_SERVICE_URL", "http://localhost:9997")
loader_service_url = os.getenv("LOADER_SERVICE_URL", "http://localhost:9998")

fast_api = FastAPI()


async def app(file: UploadFile, username: str) -> dict:
    # receive the photo

    files = {
        "file": (file.filename, await file.read(), file.content_type),
    }

    async with httpx.AsyncClient() as client:
        timeout = httpx.Timeout(60000.0, connect=5.0)  # Adjust timeouts as needed
        response = await client.post(
            f"{extractor_service_url}", files=files, timeout=timeout
        )
    response.raise_for_status()
    extracted_info = response.json().get("result")

    async with httpx.AsyncClient() as client:
        timeout = httpx.Timeout(60000.0, connect=5.0)  # Adjust timeouts as needed
        response = await client.post(
            f"{loader_service_url}",
            json={"content": extracted_info, "username": username},
            timeout=timeout,
        )
    response.raise_for_status()
    final_info = response.json().get("result")

    return {"result": final_info}

    # extract stats from the photo

    # send the stats to the loader service

    # return the result to the user


@fast_api.post("/")
async def process(file: UploadFile, username: Annotated[str, Form()]):
    result = await app(file, username)
    return result


if __name__ == "__main__":
    uvicorn.run(fast_api, host="0.0.0.0", port=8000)
