from ollama import Client


class LLM:
    def __init__(self, system_prompt: str = "", few_shot_examples: str = ""):
        self.system_prompt = system_prompt
        self.few_shot_examples = few_shot_examples

    def extract_info(self, image_location: str) -> str:
        raise NotImplementedError("This method should be overridden by subclasses.")

    def chat(self, prompt: str) -> str | None:
        raise NotImplementedError("This method should be overridden by subclasses.")


class Ollama(LLM):
    def __init__(self, model_name, base_url="http://localhost:11434"):
        super().__init__()
        self.model_name = model_name
        self.base_url = base_url
        self.client = Client(host=base_url)
        self.extract_info = self.extract_info_ollama
        self.chat = self.chat_ollama

    def chat_ollama(self, prompt):
        return self.client.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {
                    "role": "user",
                    "content": f"""
                                Example(s):
                                {self.few_shot_examples}
                                """,
                },
                {"role": "user", "content": prompt},
            ],
            stream=False,
        ).message.content

    def extract_info_ollama(self, image_location: str) -> str:
        result = self.client.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {
                    "role": "user",
                    "content": f"""
                                Example(s):
                                {self.few_shot_examples}
                                """,
                },
                {
                    "role": "user",
                    "content": "extract the stats from the image, also give some context about the stats if neccessary, be concise and to the point",
                    "images": [image_location],
                },
            ],
            stream=False,
        ).message.content

        return result if result else "No response from Ollama."


class Bedrock(LLM):
    def __init__(self, model_id, region):
        super().__init__()
        self.model_id = model_id
        self.region = region
        self.extract_info = self.extract_info_bedrock
        self.chat = self.chat_bedrock

    def chat_bedrock(self, prompt):
        raise NotImplementedError("Bedrock chat method is not implemented.")

    def extract_info_bedrock(self, image_location: str) -> str:
        raise NotImplementedError("Bedrock extract_info method is not implemented.")
