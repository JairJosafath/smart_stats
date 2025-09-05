from services.extractor.llm import Ollama, LLM


def test_inference():
    llms: list[LLM] = [] 
    llms.append(Ollama(model_name="qwen3:0.6b", base_url="http://localhost:11434"))

    for llm in llms:
        llm.system_prompt = "You know a lot about geography. You answer questions in a concise manner. Just answer with the name of the city."
        llm.few_shot_examples = """
        What is the capital of the Netherlands?
        Amsterdam
        What is the capital of Germany?
        Berlin"""
        llm_input = "What is the capital of France?"

        response = llm.chat(llm_input)

        if response is None:
            raise ValueError("LLM response is None")

        assert "Paris" in response, f"Expected 'Paris' in response but got: {response}"
