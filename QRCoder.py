from PIL import Image
import qrcode
from pathlib import Path

# Diretórios
ROOTDIR = Path(__file__).parent
PATHQRCodes = ROOTDIR / 'QRCodes'
ICONPATH = ROOTDIR / 'icon.png'

# Garante que o diretório para os QR Codes existe
PATHQRCodes.mkdir(parents=True, exist_ok=True)

# Links para gerar QR Codes
link = "https://youtu.be/JIKQV8br-mM?si=jOeitQMmYwiwZorY"
link2 = 'https://github.com/Diego2S'

# Função para criar o QR Code
def criar_QRCode(link, nomeDoArquivo='QRCode',logo=True):

    qr = qrcode.QRCode(
        version=1,  # Tamanho do QR Code
        error_correction=qrcode.ERROR_CORRECT_H,  # Nível de correção
        box_size=10,  # Tamanho das células
        border=4  # Tamanho da borda
    )

    qr.add_data(link)
    qr.make(fit=True)

    # Cria a imagem do QR Code
    img = qr.make_image(fill="black", back_color="white")

    # Caminho para salvar a imagem do QR Code
    PathImg = PATHQRCodes / f'{nomeDoArquivo}.png'

    # Adiciona a logo se o arquivo de logo existir
    if ICONPATH.exists() and logo:
        logo = Image.open(ICONPATH).convert("RGBA")  # Converte a logo para RGBA

        # Redimensiona a logo para 40% do tamanho do QR Code
        qr_size = img.size[0]
        logo_size = int(qr_size * 0.4)
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        # Cria a máscara para a logo
        logo_mask = logo.split()[3] if logo.mode == "RGBA" else None  # Canal alfa para transparência

        # Centraliza a logo no QR Code
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        
        # Aqui, mantemos a cor do logo, mesmo se ele tiver transparência
        img = img.convert("RGBA")  # Converte o QR Code para RGBA
        img.paste(logo, pos, mask=logo_mask)  # Aplica a logo com a máscara

    # Salva a imagem final com o QR Code e a logo
    img.save(PathImg)

    print(f'QRCode criado com sucesso.\n{PathImg}')

# Cria o QR Code ao rodar o script
if __name__ == '__main__':
    for enu,valor in enumerate([link,link2]):
        criar_QRCode(valor, f'QrCode {enu}')

    for enu,valor in enumerate([link,link2],2):
        criar_QRCode(valor, f'QrCode {enu}',logo=False)
        
