"""tts.txt içindeki [etiket]leri silip altyazı/hizalama metnini (script.txt) üretir."""
import re, sys

t = re.sub(r"\[[^\]]*\]", " ", open(sys.argv[1]).read())
open(sys.argv[2], "w").write(re.sub(r"[ \t]+", " ", t).strip() + "\n")
