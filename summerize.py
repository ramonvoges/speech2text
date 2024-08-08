import whisper
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# Transkription mit Whisper
model = whisper.load_model("base")
result = model.transcribe("Test.m4a")
transcription = result["text"]

# Nachbearbeitung mit Ollama
ollama = Ollama(base_url="http://10.10.14.225:10000", model="mistral:instruct")

prompt = PromptTemplate(
    input_variables=["transcription"],
    template="Zusammenfassung der folgenden Transkription:\n\n{transcription}\n\nZusammenfassung:",
)

print(transcription)
response = ollama(prompt.format(transcription=transcription))
print(response)
