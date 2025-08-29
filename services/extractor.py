from llm.llm import LLM

class ImageInfoExtractor:
    def __init__(self, llm: LLM):
        self.llm = llm

    def extract_info(self, image_location):
        prompt = f"Extract statistics from the image"
        print(f"Extracting info from image at: {image_location}")
        response = self.llm.generate_response(prompt)
        return response