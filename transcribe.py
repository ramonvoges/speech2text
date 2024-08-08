import whisper

model = whisper.load_model("base")
result = model.transcribe("Test.m4a")
print(result["text"])
