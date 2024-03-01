import sys

import torch
from hf_voice_assistant import log
from transformers import pipeline
from transformers.pipelines.audio_utils import ffmpeg_microphone_live


def transcribe(chunk_length_s=5.0, stream_chunk_s=1.0) -> str:
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    transcriber = pipeline(
        "automatic-speech-recognition", model="openai/whisper-base.en", device=device
    )

    sampling_rate = transcriber.feature_extractor.sampling_rate

    mic = ffmpeg_microphone_live(
        sampling_rate=sampling_rate,
        chunk_length_s=chunk_length_s,
        stream_chunk_s=stream_chunk_s,
    )

    logger = log.init_logger()
    logger.debug("Start speaking...")
    for item in transcriber(mic, generate_kwargs={"max_new_tokens": 128}):
        sys.stdout.write("\033[K")
        logger.debug(item["text"])
        if not item["partial"][0]:
            break

        return item["text"]
