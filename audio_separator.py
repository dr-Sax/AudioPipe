from audio_separator import separator

from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

# Using embedded configuration.
separator = Separator('spleeter:2stems')

audio_loader = AudioAdapter.default()
sample_rate = 44100
waveform, _ = audio_loader.load('espresso.mp3', sample_rate=sample_rate)

# Perform the separation :
prediction = separator.separate(waveform)
