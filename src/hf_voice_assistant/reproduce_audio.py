import simpleaudio as sa
import soundfile as sf


def play_audio(audio, sample_rate: int = 16000):
    """
    Saves audio data to a WAV file and plays it.

    Args:
      audio (torch.Tensor): The audio data to play.
      sample_rate (int): The sample rate of the audio data.
    """
    # Save the audio data to a file
    sf.write("output.wav", audio, sample_rate)

    # Play the audio file
    wave_obj = sa.WaveObject.from_wave_file("output.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing    play_obj.wait_done()  # Wait until sound has finished playing
