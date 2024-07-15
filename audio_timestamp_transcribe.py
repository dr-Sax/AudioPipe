# https://github.com/linto-ai/whisper-timestamped

import whisper_timestamped as whisper

audio = whisper.load_audio("media/audio_back.wav")

model = whisper.load_model("tiny", device="cpu")

result = whisper.transcribe(model, audio, language="en")

import json
json_object = json.dumps(result, indent = 2, ensure_ascii = False)

with open("audio_transcript.json", "w") as outfile:
    outfile.write(json_object)