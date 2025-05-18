import speech_recognition as sr
from pydub import AudioSegment

# Convert .aac to .wav (since SpeechRecognition needs wav)
def convert_aac_to_wav(aac_path, wav_path):
    audio = AudioSegment.from_file(aac_path, format="aac")
    audio.export(wav_path, format="wav")

# Transcribe using Google Web Speech API
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Speech was unclear."
        except sr.RequestError as e:
            return f"API unavailable: {e}"

if __name__ == "__main__":
    aac_file = "your_audio.aac"
    wav_file = "temp.wav"
    convert_aac_to_wav(aac_file, wav_file)
    transcript = transcribe_audio(wav_file)
    print("Transcription:\n", transcript)


