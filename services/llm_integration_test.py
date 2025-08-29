import unittest
from llm import Ollama

class TestLocalLLMInference(unittest.TestCase):
    def test_ollama_inference(self):
        llm=Ollama(model_name="qwen2.5vl:7b", base_url="http://localhost:11434")
        llm.system_prompt = "You know a lot about geography. You answer questions in a concise manner. Just answer with the name of the city."
        llm.few_shot_examples = """
        Q: What is the capital of the Netherlands?
        A: Amsterdam
        Q: What is the capital of Germany?
        A: Berlin"""
        llm_input = "What is the capital of France?"

        response=llm.chat(llm_input)
        self.assertEqual("Paris", response)

if __name__ == '__main__':
    unittest.main()