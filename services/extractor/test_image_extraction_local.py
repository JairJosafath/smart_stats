from services.extractor.llm import Ollama, LLM
from services.extractor.extractor import ImageInfoExtractor


def test_image_extraction():
    llms: list[LLM] = []

    llms.append(Ollama(model_name="qwen2.5vl:7b", base_url="http://localhost:11434"))

    for llm in llms:
        extractor = ImageInfoExtractor(llm=llm)
        image_path = "services/extractor/test_FN_stats.jpg"

        response = extractor.extract_info(image_location=image_path)
        expected_stats = [
            "Eliminations: 7",
            "Assists: 0",
            "Distance Traveled: 1 km",
            "Hits: 949",
        ]
        for stat in expected_stats:
            if response is None:
                raise ValueError("LLM response is None")
            assert stat in response, (
                f"Expected '{stat}' to be in the response: {response}"
            )
