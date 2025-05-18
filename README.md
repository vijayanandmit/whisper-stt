
# 🎙️ Whisper Speech-to-Text Transcriber

This is a simple Python script that uses [OpenAI Whisper](https://github.com/openai/whisper) to convert audio (`.aac`) files into text. Whisper is a general-purpose speech recognition model trained on a large dataset of multilingual and multitask supervised data.

## 🧠 Features

- Uses OpenAI's Whisper model (`base`) for transcription
- Converts `.aac` audio to text
- Minimal and easy-to-use script

## 📁 Project Structure

```bash
whisper-stt/
├── convert.py         # Main script to run transcription
├── README.md          # Project description and usage guide
└── LICENSE            # MIT License (optional)


📦 Installation & Dependencies

✅ Requirements:
	•	Python 3.7+
	•	ffmpeg installed and in PATH

🔧 Setup:
pip install git+https://github.com/openai/whisper.git

Install ffmpeg:
	•	macOS: brew install ffmpeg
	•	Ubuntu: sudo apt install ffmpeg
	•	Windows: ffmpeg.org
▶️ Usage
python convert.py

🙌 Acknowledgements
	•	OpenAI Whisper
	•	FFmpeg

