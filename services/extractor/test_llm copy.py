from services.llm.llm import LLM, Ollama, Bedrock

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