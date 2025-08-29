from services.extractor.llm import Ollama, ImageInfoExtractor

def test_ollama_inference():
    llm=Ollama(model_name="qwen3:0.6b", base_url="http://localhost:11434")
    llm.system_prompt = "You know a lot about geography. You answer questions in a concise manner. Just answer with the name of the city."
    llm.few_shot_examples = """
    What is the capital of the Netherlands?
    Amsterdam
    What is the capital of Germany?
    Berlin"""
    llm_input = "What is the capital of France?"

    response=llm.chat(llm_input)

    assert "Paris" in response, f"Expected 'Paris' in response but got: {response}"


def test_ollama_image_extraction():
    llm=Ollama(model_name="qwen2.5vl:7b", base_url="http://localhost:11434")
    extractor = ImageInfoExtractor(llm=llm)
    image_path = "services/extractor/FN_stats.jpg"
    
    response = extractor.extract_info(image_location=image_path)
    expected_stats = [
        "Eliminations: 7",
        "Assists: 0",
        "Distance Traveled: 1 km",
        "Hits: 949",
    ]
    for stat in expected_stats:
        assert stat in response, f"Expected '{stat}' to be in the response: {response}"
