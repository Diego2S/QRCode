import qrcode
from pathlib import Path

ROOTDIR = Path(__file__).parent
PATHQRCodes = ROOTDIR / 'QRCodes'

PATHQRCodes.mkdir(parents=True,exist_ok=True)


link = "https://youtu.be/JIKQV8br-mM?si=jOeitQMmYwiwZorY"
link2 = 'https://github.com/Diego2S'

qr = qrcode.QRCode(None,
                   qrcode.ERROR_CORRECT_H
                   )

qr.add_data(link2)
qr.make(fit=True)

img = qr.make_image()

PathImg = PATHQRCodes / 'qrcode.png'

img.save(PathImg)


if __name__ == '__main__':
    pass