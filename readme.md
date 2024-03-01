# Hugging Face Voice Assistant

Implementation of [_Creating a voice assistant_](https://huggingface.co/learn/audio-course/chapter7/voice-assistant) from Hugging Face's audio course.

![Voice assistant diagram](https://github.com/rodrigobdz/hugging-face-voice-assistant/assets/14152377/8b12ae46-0f4f-492a-871e-495bfefc0931)
[Source](https://huggingface.co/datasets/huggingface-course/audio-course-images/resolve/main/voice_assistant.png)

## Requirements

- macOS
- [uv](https://astral.sh/blog/uv)
- [Generate](https://huggingface.co/settings/tokens) a Hugging Face [Access Token](https://huggingface.co/docs/hub/security-tokens) with `read` scope and set it as `HF_TOKEN` environment variable

  ```sh
  export HF_TOKEN=your_token
  ```

- [Whisper](https://github.com/openai/whisper) dependency `ffmpeg`

  ```sh
  brew install ffmpeg
  ```

## Installation

- Install dependencies

  ```sh
  ./script/bootstrap
  ```

- Install the package

  ```sh
  ./script/install
  ```

## Usage

- Run voice assistant

  ```sh
  ./script/run
  ```

## Troubleshooting

- Microphone not working in Jupyter notebook

  [Error:](https://github.com/huggingface/transformers/issues/25183) No error message, just no transcription

  Solution: Run code locally in a Python script

- Microphone not working in macOS and only showing `you` as transcription

  Error:

  ```sh
  Start speaking...
    you
  ```

  [Solution:](https://github.com/huggingface/transformers/issues/28154#issue-2049630196)

  Patch `.venv/lib/python3.12/site-packages/transformers/pipelines/audio_utils.py`

  ```diff
   elif system == "Darwin":
      format_ = "avfoundation"
  -    input_ = ":0"
  +    input_ = ":default"
  ```

- Library not loaded during speech transcription

  Error:

  ```sh
  dyld[657]: Library not loaded: /opt/homebrew/opt/libunibreak/lib/libunibreak.5.dylib
    Referenced from: <6EF87AAD-BAC6-3DFD-909B-EEC70DA343DE> /opt/homebrew/Cellar/libass/0.17.1/lib/libass.9.dylib
    Reason: tried: '/opt/homebrew/opt/libunibreak/lib/libunibreak.5.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/opt/homebrew/opt/libunibreak/lib/libunibreak.5.dylib' (no such file), '/opt/homebrew/opt/libunibreak/lib/libunibreak.5.dylib' (no such file), '/usr/local/lib/libunibreak.5.dylib' (no such file), '/usr/lib/libunibreak.5.dylib' (no such file, not in dyld cache), '/opt/homebrew/Cellar/libunibreak/6.0/lib/libunibreak.5.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/opt/homebrew/Cellar/libunibreak/6.0/lib/libunibreak.5.dylib' (no such file), '/opt/homebrew/Cellar/libunibreak/6.0/lib/libunibreak.5.dylib' (no such file), '/usr/local/lib/libunibreak.5.dylib' (no such file), '/usr/lib/libunibreak.5.dylib' (no such file, not in dyld cache)
  ```

  Solution:

  ```sh
  brew reinstall ffmpeg
  ```

## Contributing

Please read [contributing.md](contributing.md) for details on the guidelines for this project.

## Credits

- Scripts follow [rodrigobdz's Shell Style Guide](https://github.com/rodrigobdz/styleguide-sh)
- Linter configuration files imported from [rodrigobdz/linter](https://github.com/rodrigobdz/linters)
- Readme is based on [rodrigobdz/minimal-readme](https://github.com/rodrigobdz/minimal-readme)
- Code is based on [Hugging Face's audio course](https://huggingface.co/learn/audio-course/chapter7/voice-assistant)

## License

[The Unlicense](license) © [rodrigobdz](https://github.com/rodrigobdz).
