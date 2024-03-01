import requests
from huggingface_hub import HfFolder

from hf_voice_assistant import log


def query(text, model_id="tiiuae/falcon-7b-instruct") -> str:
    api_url = f"https://api-inference.huggingface.co/models/{model_id}"
    headers = {"Authorization": f"Bearer {HfFolder().get_token()}"}
    payload = {"inputs": text}

    logger = log.init_logger()
    logger.debug("Querying...: %s", text)
    response = requests.post(api_url, headers=headers, json=payload, timeout=10)

    parsed_response: str = response.json()[0]["generated_text"][len(text) + 1 :]
    logger.debug("Response: %s", parsed_response)
    return parsed_response
