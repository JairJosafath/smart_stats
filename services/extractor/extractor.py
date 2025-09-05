from services.extractor.llm import LLM
import os


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

    def extract_info(self, image_location: str) -> str | None:
        return self.llm.extract_info(image_location=self.host_path + image_location)
