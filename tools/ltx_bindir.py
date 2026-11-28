"""LTX canlandırma kliplerini sinematik videonun boş sahnelerine bindirir (1080x1920 çıktı).
Kullanım: python3 tools/ltx_bindir.py <klasör>
<klasör>/ltx/bindir.json: [{"klip": "ltx/x.mp4", "t0": 20.4, "t1": 24.6, "bant": "ZİGETVAR · 1566"}, ...]
LTX klibi 720p gelir; burada 1080x1920'ye büyütülür, yavaş yakınlaştırma (1.00 -> 1.07) ve
alt bant yazısı eklenir, pencere süresine göre hızı ayarlanır. Ses ve diğer kareler aynen kalır.
Sonuç: <klasör>/video.mp4 (orijinal video_ham.mp4 olarak saklanır).
"""
import json, os, subprocess, sys
d = os.path.abspath(sys.argv[1])
FONT = os.path.join(os.path.dirname(__file__), '..', 'sinematik', 'motor', 'fonts', 'Oswald.ttf')
src = os.path.join(d, 'video.mp4'); ham = os.path.join(d, 'video_ham.mp4')
if not os.path.exists(ham): os.rename(src, ham)
items = json.load(open(os.path.join(d, 'ltx', 'bindir.json')))
inputs = ['-i', ham]; fc = []; last = '0:v'
for i, it in enumerate(items):
    clip = os.path.join(d, it['klip']); dur = it['t1'] - it['t0']
    cd = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', clip]))
    k = max(dur / cd, 1.0)  # kısaysa yavaşlat, uzunsa kırp
    inputs += ['-i', clip]
    n = int(dur * 30) + 1
    txt = it.get('bant', '').replace("'", "’").replace(':', '\\:')
    band = (f",drawbox=x=90:y=1560:w=900:h=120:color=0xb3261e@0.95:t=fill,"
            f"drawtext=fontfile={FONT}:text='{txt}':fontsize=66:fontcolor=white:x=(w-tw)/2:y=1578") if txt else ''
    fc.append(f"[{i+1}:v]setpts={k:.4f}*PTS,fps=30,trim=0:{dur:.3f},setpts=PTS-STARTPTS,"
              f"scale=w='trunc(1080*(1+0.07*t/{dur:.3f})/2)*2':h='trunc(1920*(1+0.07*t/{dur:.3f})/2)*2':eval=frame:flags=lanczos,"
              f"crop=1080:1920,setsar=1,format=yuv420p{band},"
              f"setpts=PTS+{it['t0']:.3f}/TB[c{i}]")
    fc.append(f"[{last}][c{i}]overlay=0:0:enable='between(t,{it['t0']:.3f},{it['t1']:.3f})':eof_action=pass[v{i}]")
    last = f'v{i}'
cmd = ['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', f'[{last}]', '-map', '0:a',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-movflags', '+faststart', src]
subprocess.run(cmd, check=True)
print('ok', src)
