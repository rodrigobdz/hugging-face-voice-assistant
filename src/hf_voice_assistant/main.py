from hf_voice_assistant import (
    language_model_query,
    reproduce_audio,
    speech_transcription,
    synthesize_speech,
    wake_word_detection,
)


def main():
    # Wake word detection
    wake_word_detection.launch_fn()

    # Speech transcription
    transcription = speech_transcription.transcribe()

    # Language model query
    response = language_model_query.query(transcription)

    # Speech synthesis
    audio = synthesize_speech.synthesise(response)

    # Reproduce audio
    reproduce_audio.play_audio(audio, 16000)


if __name__ == "__main__":
    main()
