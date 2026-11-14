"""Uzun video seslendirmesi: tts.txt'yi paragraf sınırında ~1800 karakterlik parçalara böler, her parçayı
tools/tts.py ile seslendirir, 0,7 sn boşlukla build/voice.mp3'e birleştirir; ardından
`python3 tools/viral.py voice <klasör>` (voice.mp3 varsa TTS'i atlar) kelime zamanlarını çıkarır.
Kullanım: python3 tools/uzun_ses.py <klasör>
Kota: işe başlamadan ElevenLabs kalan karakterini kontrol eder; yetmezse hiçbir şey seslendirmeden çıkar (kod 3).
"""
import json, os, re, subprocess, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tts import key

d = os.path.abspath(sys.argv[1]); b = os.path.join(d, 'build'); p = os.path.join(b, 'parca'); os.makedirs(p, exist_ok=True)
text = open(os.path.join(d, 'tts.txt')).read().strip()
plain = len(re.sub(r'\[[a-z ]+\]', '', text))
sub = json.load(urllib.request.urlopen(urllib.request.Request('https://api.elevenlabs.io/v1/user/subscription', headers={'xi-api-key': key()})))
left = sub['character_limit'] - sub['character_count']
print(f'metin {len(text)} karakter, kota kalan {left}')
if len(text) + 2000 > left:
    sys.exit(3)
paras = [x.strip() for x in text.split('\n\n') if x.strip()]; parts, cur = [], ''
for x in paras:
    if cur and len(cur) + len(x) > 1800: parts.append(cur); cur = x
    else: cur = (cur + '\n\n' + x).strip()
if cur: parts.append(cur)
files = []
for i, t in enumerate(parts):
    tx, mp = os.path.join(p, f'p{i:02d}.txt'), os.path.join(p, f'p{i:02d}.mp3')
    open(tx, 'w').write(t)
    if not os.path.exists(mp): subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'tts.py'), tx, mp], check=True)
    files.append(mp)
sil = os.path.join(p, 'sessiz.wav')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=mono', '-t', '0.7', sil], check=True)
lst = os.path.join(p, 'liste.txt')
with open(lst, 'w') as f:
    for i, mp in enumerate(files):
        w = mp[:-4] + '.wav'; subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mp, '-ar', '44100', '-ac', '1', w], check=True)
        f.write(f"file '{w}'\n")
        if i < len(files) - 1: f.write(f"file '{sil}'\n")
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c:a', 'libmp3lame', '-b:a', '192k', os.path.join(b, 'voice.mp3')], check=True)
subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'viral.py'), 'voice', d], check=True)
