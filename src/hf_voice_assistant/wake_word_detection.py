import torch
from transformers import pipeline
from transformers.pipelines.audio_utils import ffmpeg_microphone_live

from hf_voice_assistant import log


def launch_fn(
    wake_word="marvin",
    prob_threshold=0.5,
    chunk_length_s=2.0,
    stream_chunk_s=0.25,
):
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    classifier = pipeline(
        "audio-classification",
        model="MIT/ast-finetuned-speech-commands-v2",
        device=device,
    )

    if wake_word not in classifier.model.config.label2id.keys():
        raise ValueError(
            f"Wake word {wake_word} not in set of valid class labels, pick a wake word in the set {classifier.model.config.label2id.keys()}."
        )

    sampling_rate = classifier.feature_extractor.sampling_rate

    mic = ffmpeg_microphone_live(
        sampling_rate=sampling_rate,
        chunk_length_s=chunk_length_s,
        stream_chunk_s=stream_chunk_s,
    )

    logger = log.init_logger()
    logger.debug("Listening for wake word...")
    for prediction in classifier(mic):
        prediction = prediction[0]
        if prediction["label"] == wake_word:
            logger.debug(f"Prediction: {prediction}")
            if prediction["score"] > prob_threshold:
                return True
