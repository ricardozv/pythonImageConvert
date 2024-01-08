from PIL import Image
import os

# Caminho para a imagem carregada
img_path = 'morroco.jpg'  

# Carregar a imagem do arquivo
color_image = Image.open(img_path)

# Converter a imagem para escala de cinza
gray_image = color_image.convert("L")

# Binarizar a imagem
threshold = 128
binary_image = gray_image.point(lambda x: 255 if x > threshold else 0, '1')

# Caminhos onde as imagens serão salvas
gray_image_path = 'escala_de_cinza.jpg'
binary_image_path = 'binarizada.jpg'

# Verificar se o diretório do caminho existe e criá-lo se não existir
dir_name = os.path.dirname(gray_image_path)
if dir_name:
    os.makedirs(dir_name, exist_ok=True)

# Salvar a imagem em escala de cinza
gray_image.save(gray_image_path)

# Salvar a imagem binarizada
binary_image.save(binary_image_path)

print(f"A imagem em escala de cinza foi salva como: {gray_image_path}")
print(f"A imagem binarizada foi salva como: {binary_image_path}")
