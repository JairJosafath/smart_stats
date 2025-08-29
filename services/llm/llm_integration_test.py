import unittest
from llm import Ollama, ImageInfoExtractor

class TestLocalLLMInference(unittest.TestCase):
    def test_ollama_inference(self):
        llm=Ollama(model_name="qwen3:0.6b", base_url="http://localhost:11434")
        llm.system_prompt = "You know a lot about geography. You answer questions in a concise manner. Just answer with the name of the city."
        llm.few_shot_examples = """
        Q: What is the capital of the Netherlands?
        A: Amsterdam
        Q: What is the capital of Germany?
        A: Berlin"""
        llm_input = "What is the capital of France?"

        response=llm.chat(llm_input)
        if "<think>" in response and "</think>" in response:
            response = response.split("<think>")[0] + response.split("</think>")[-1]
        response = response.strip()

        self.assertIn("Paris", response)


    def test_ollama_image_extraction(self):
        llm=Ollama(model_name="qwen2.5vl:7b", base_url="http://localhost:11434")
        extractor = ImageInfoExtractor(llm=llm)
        image_path = "services/llm/FN_stats.jpg"
        
        response = extractor.extract_info(image_location=image_path)
        expected_stats = [
            "Eliminations: 7",
            "Assists: 0",
            "Distance Traveled: 1 km",
            "Hits: 949",
        ]
        print("Extraction Response:", response)
        for stat in expected_stats:
            self.assertIn(stat, response)

if __name__ == '__main__':
    unittest.main()