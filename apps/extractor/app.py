from services.extractor.extractor import ImageInfoExtractor
from services.extractor.llm import Ollama
import os
from fastapi import FastAPI, UploadFile
import uvicorn

host = os.getenv("HOST", "http://localhost")
fast_api = FastAPI()

QWEN_2_5B_MODEL = "qwen2.5vl:7b"


async def app(file: UploadFile) -> dict:
    extractor = ImageInfoExtractor(
        llm=Ollama(
            model_name=QWEN_2_5B_MODEL,
            base_url=f"{host}:11434",
        ),
    )

    image_path = "temp_image.jpg"
    with open(image_path, "wb") as img_file:
        img_file.write(await file.read())

    result = extractor.extract_info(image_location=image_path)

    os.remove(image_path)

    return {"result": result}


@fast_api.post("/")
async def extract(file: UploadFile):
    result = await app(file)
    return result


if __name__ == "__main__":
    uvicorn.run(fast_api, host="0.0.0.0", port=8000)
