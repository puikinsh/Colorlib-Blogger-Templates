#!/usr/bin/env python3
"""Generate an original, low-amplitude 12-second PCM audio QA signal."""
from pathlib import Path
import math, struct, wave

path=Path(__file__).resolve().parents[1]/'assets/qa/media-signal.wav'
path.parent.mkdir(exist_ok=True)
rate=16000
samples=[]
for index in range(rate*12):
    second=index/rate
    phase=second%1
    envelope=math.sin(math.pi*phase/0.18)**2 if phase<0.18 else 0
    samples.append(round(32767*0.05*envelope*math.sin(2*math.pi*440*second)))
with wave.open(str(path),'wb') as output:
    output.setnchannels(1)
    output.setsampwidth(2)
    output.setframerate(rate)
    output.writeframes(struct.pack('<'+'h'*len(samples),*samples))
print(path)
