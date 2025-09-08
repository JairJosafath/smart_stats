from services.extractor.extractor import ImageInfoExtractor
from services.extractor.llm import LLM

def test_image_info_extractor_initialization():
    llm = LLM(system_prompt="You are a helpful assistant.", few_shot_examples="Example 1")
    extractor = ImageInfoExtractor(llm=llm)
    assert extractor.llm.system_prompt == """
        You are an expert at analyzing images and extracting relevant information. The information will be statistics retrieved from the image, which is a screenshot of in-game statistics."""
    assert extractor.llm.few_shot_examples ==  """
        **image description**: A screenshot showing a player's in-game statistics for a eating contest event. The stats include burgers eaten, spiceness level, and time taken.
        **extracted stats**:
        Burgers Eaten: 15
        Spiceness Level: 3
        Time Taken: 2 minutes
        """
    