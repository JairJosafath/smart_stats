from services.extractor.llm import LLM, Ollama, Bedrock
from services.extractor.extractor import ImageInfoExtractor

def test_llm_initialization():
    llm = LLM(system_prompt="You are a helpful assistant.", few_shot_examples="Example 1")
    assert llm.system_prompt == "You are a helpful assistant."
    assert llm.few_shot_examples == "Example 1"

def test_ollama_initialization():
    ollama = Ollama(model_name="llama2", base_url="http://localhost:11434")
    assert ollama.model_name == "llama2"
    assert ollama.base_url == "http://localhost:11434"

def test_bedrock_initialization():
    bedrock = Bedrock(model_id="amazon-model", region="us-west-2")
    assert bedrock.model_id == "amazon-model"
    assert bedrock.region == "us-west-2"

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
    