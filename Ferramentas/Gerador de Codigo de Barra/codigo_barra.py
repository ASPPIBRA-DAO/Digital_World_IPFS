from barcode import EAN13
from barcode.writer import ImageWriter # para salvar em png

numero = "123123123123"

codigo_barra = EAN13(numero, writer=ImageWriter()) # writer para salvar em png
codigo_barra.save("codigo_barra")

# codigo ....


codigos_produtos = {
    "Feijao": "551746511111",
    "Arroz": "665789011111",
    "Macarrao": "665887111111",
    "Azeite": "998556211111"}

for produto in codigos_produtos:
    codigo_barra = EAN13(codigos_produtos[produto], writer=ImageWriter()) # writer para salvar em png
    codigo_barra.save(f"{produto}_codigo")