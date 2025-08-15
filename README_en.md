# 📦 Transcrypter

## 🌟 Highlights

- Transcribe audio files (.mp3, .wav).
- Extract audio from video files (.mp4) and transcribe it.
- Download videos directly from YouTube for transcription.
- Generate summaries from transcriptions using the Gemini API.
- Simple command-line interface for ease of use.

## ℹ️ Overview

Transcryptor is a Python-based tool designed to automate the process of transcribing audio and video files and generating concise summaries from the transcriptions. It leverages the Vosk library for offline speech recognition and Google's Gemini AI for summarization. The vosk model is available at https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip .

### ✍️ Authors

João Gabriel Barbosa de Luna
joaogabrieldeluna@gmail.com

## 🚀 Usage

*Run the application from the project's root directory:*

```bash
python main.py
```

*Follow the interactive menu to select the type of file you want to process. The output will be saved in the `/transcriptions` and `/resumes` folders.*

## ⬇️ Installation

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/joaoluna-dev/Transcrypter.git
   cd Transcrypter
   ```

2. **Install dependencies:**
   
   ```bash
   pip install pydub vosk moviepy google-genai python-dotenv pytubefix
   ```
   
3. **Set up API Key:**
   
   - When you first run the application, you will be prompted to enter your Google AI API key.
   
   - The key will be automatically saved in a `chaves.env` file for future use.
     *Requires Python 3.x*

## 💭 Feedback and Contributing

Feel free to open an issue for any bugs or feature requests.
