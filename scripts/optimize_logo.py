import os
import requests
from io import BytesIO
from PIL import Image

# Configuração
IMAGE_URL = "https://i.ibb.co/yBS9KGhc/whia.jpg"
OUTPUT_DIR = os.path.join("public", "images")
OUTPUT_FILENAME = "logo-comunidade.webp"
TARGET_SIZE = (128, 128) # 2x para retina display (exibido a 63x63 aproximadamente)

def optimize_logo():
    # Garantir que o diretório existe
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Diretório criado: {OUTPUT_DIR}")

    print(f"Baixando imagem de: {IMAGE_URL}")
    try:
        response = requests.get(IMAGE_URL)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao baixar imagem: {e}")
        return

    try:
        img = Image.open(BytesIO(response.content))
        print(f"Imagem original: {img.format}, {img.size}")

        # Converter para RGB se necessário (para salvar como WebP/JPG se a origem for RGBA/P)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Redimensionar (Lanczos para melhor qualidade no downsampling)
        img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        
        output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
        
        # Salvar como WebP com qualidade 85 (ótimo compromisso)
        img.save(output_path, "WEBP", quality=85)
        
        print(f"Imagem salva em: {output_path}")
        print(f"Tamanho final: {img.size}")
        
    except Exception as e:
        print(f"Erro ao processar imagem: {e}")

if __name__ == "__main__":
    optimize_logo()
