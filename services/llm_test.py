import unittest
from llm import LLM, Ollama, Bedrock, ImageInfoExtractor

class TestLLMClasses(unittest.TestCase):
    def test_llm_initialization(self):
        llm = LLM(system_prompt="You are a helpful assistant.", few_shot_examples="Example 1")
        self.assertEqual(llm.system_prompt, "You are a helpful assistant.")
        self.assertEqual(llm.few_shot_examples, "Example 1")

    def test_ollama_initialization(self):
        ollama = Ollama(model_name="llama2", base_url="http://localhost:11434")
        self.assertEqual(ollama.model_name, "llama2")
        self.assertEqual(ollama.base_url, "http://localhost:11434")
        self.assertEqual(ollama.system_prompt, "")
        self.assertEqual(ollama.few_shot_examples, "")

    def test_bedrock_initialization(self):
        bedrock = Bedrock(model_id="amazon-model", region="us-west-2")
        self.assertEqual(bedrock.model_id, "amazon-model")
        self.assertEqual(bedrock.region, "us-west-2")
        self.assertEqual(bedrock.system_prompt, "")
        self.assertEqual(bedrock.few_shot_examples, "")

    def test_image_info_extractor_initialization(self):
        llm = LLM(system_prompt="You are a helpful assistant.", few_shot_examples="Example 1")
        extractor = ImageInfoExtractor(llm=llm)
        self.assertIs(extractor.llm, llm)

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