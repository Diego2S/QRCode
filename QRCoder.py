import qrcode
from pathlib import Path

ROOTDIR = Path(__file__).parent
PATHQRCodes = ROOTDIR / 'QRCodes'

PATHQRCodes.mkdir(parents=True,exist_ok=True)


link = "https://youtu.be/JIKQV8br-mM?si=jOeitQMmYwiwZorY"
link2 = 'https://github.com/Diego2S/QRCode'

img = qrcode.make(link2)

PathImg = PATHQRCodes / 'qrcode.png'

img.save(PathImg)