import json, sys
from faster_whisper import WhisperModel
m=WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=4)
import subprocess, numpy as np
pcm=subprocess.run(["ffmpeg","-v","quiet","-i",sys.argv[1],"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout
audio=np.frombuffer(pcm,dtype=np.float32)
segs,info=m.transcribe(audio, language="tr", word_timestamps=True, beam_size=5)
out=[]
for s in segs:
    for w in s.words: out.append({"w":w.word.strip(),"s":round(w.start,3),"e":round(w.end,3)})
    print(f"{s.start:.2f}-{s.end:.2f} {s.text}", flush=True)
json.dump(out, open(sys.argv[2],"w"), ensure_ascii=False, indent=0)
