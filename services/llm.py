import os
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
                    "content": f"""
                                Example(s):
                                {self.few_shot_examples}
                                """
                }, 
                {
                    "role": "user", 
                    "content": prompt
                }
            ],
            stream=False,
        ).message.content
    
    def extract_info(self, image_location: str) -> str:
         return self.client.chat(
            model=self.model_name, 
            messages=[
                {
                    "role": "system", 
                    "content": self.system_prompt
                }, 
                {
                    "role": "user", 
                    "content": f"""
                                Example(s):
                                {self.few_shot_examples}
                                """
                }, 
                {
                    "role": "user", 
                    'content': 'extract the stats from the image, also give some context about the stats if neccessary, be concise and to the point',
                    'images': [image_location]
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
    
    def extract_info(self, image_location: str) -> str:
        return "Mocked image info extraction."

class ImageInfoExtractor:
    def __init__(self, llm: LLM):
        llm.system_prompt = """
        You are an expert at analyzing images and extracting relevant information. The information will be statistics retrieved from the image, which is a screenshot of in-game statistics."""
        llm.few_shot_examples = """
        **image description**: A screenshot showing a player's in-game statistics for a eating contest event. The stats include burgers eaten, spiceness level, and time taken.
        **extracted stats**:
        Burgers Eaten: 15
        Spiceness Level: 3
        Time Taken: 2 minutes
        """
        self.llm = llm
        self.host_path = os.getcwd() + "/"

    def extract_info(self, image_location: str) -> str:
        return self.llm.extract_info(image_location=self.host_path + image_location)
        