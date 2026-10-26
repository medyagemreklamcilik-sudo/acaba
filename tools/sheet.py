import sys, glob, os
from PIL import Image, ImageDraw, ImageFont
files=sys.argv[2:]; out=sys.argv[1]
cw,ch=300,380; cols=6
rows=(len(files)+cols-1)//cols
sheet=Image.new("RGB",(cw*cols,ch*rows),(30,30,30)); d=ImageDraw.Draw(sheet)
f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",16)
for i,fn in enumerate(files):
    im=Image.open(fn); im.thumbnail((cw-10,ch-40))
    x,y=(i%cols)*cw,(i//cols)*ch
    sheet.paste(im,(x+5,y+5)); d.text((x+5,y+ch-30),os.path.basename(fn)[:30],font=f,fill=(255,255,0))
sheet.save(out,quality=80)
