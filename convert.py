import whisper

model = whisper.load_model("base")
result = model.transcribe("your_audio.aac")
print(result["text"])

