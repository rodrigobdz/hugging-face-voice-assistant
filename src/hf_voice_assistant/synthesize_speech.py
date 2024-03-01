import torch
from datasets import load_dataset
from transformers import SpeechT5ForTextToSpeech, SpeechT5HifiGan, SpeechT5Processor


def synthesise(text: str):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")

    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts").to(device)
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan").to(device)

    embeddings_dataset = load_dataset(
        "Matthijs/cmu-arctic-xvectors", split="validation"
    )
    speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    inputs = processor(text=text, return_tensors="pt")
    speech = model.generate_speech(
        inputs["input_ids"].to(device), speaker_embeddings.to(device), vocoder=vocoder
    )
    return speech.cpu()
