# Eine Audoaufnahme in Text umwandeln und zusammenfassen

## Aufgabe

Eine Audioaufnahme von gesprochener Sprache soll zunächst in einen Text umgewandelt werden, den Computer weiterverarbeiten können. Anschließend soll dieser Text zusammengefasst werden.

## Vorbereitungen

```bash
pip3 install -U openai-whisper langchain langchain-community
sudo apt update
sudo apt upgrade
sudo apt install ffmpeg # Benötigt whisper
```

## Skripte

`transcribe.py` transkribiert die Audioaufnahme und gibt den Text aus. `summerize.py` transkribiert den Text und gibt ihn zusammengefasst aus.
