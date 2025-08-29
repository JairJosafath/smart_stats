from ollama import Client

class LLM:
    def __init__(self, system_prompt:str="", few_shot_examples:str=""):
        self.system_prompt = system_prompt
        self.few_shot_examples = few_shot_examples

class Ollama(LLM):
    def __init__(self, model_name, base_url="http://localhost:11434"):
        super().__init__()
        self.model_name = model_name
        self.base_url = base_url
        self.client = Client(host=base_url)

    def chat(self, prompt):
        return self.client.chat(
            model=self.model_name, 
            messages=[
                {
                    "role": "system", 
                    "content": self.system_prompt
                }, 
                {
                    "role": "user", 
                    "content": self.few_shot_examples
                }, 
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            stream=False,
        ).message.content
        

class Bedrock(LLM):
    def __init__(self, model_id, region):
        super().__init__()
        self.model_id = model_id
        self.region = region

    def chat(self, prompt):
        # Mocked response for testing purposes
        if prompt == "What is the capital of France?":
            return "The capital of France is Paris."
        return "Mocked response from Bedrock model."

class ImageInfoExtractor:
    def __init__(self, llm: LLM):
        self.llm = llm