import pytesseract
import cv2

# links uteis:
# corrigir instalação windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# pegar linguas: print(pytesseract.get_languages())

imagem = cv2.imread("print_magalu.JPG")

caminho = r"C:\Users\Python\AppData\Local\Programs\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
texto = pytesseract.image_to_string(imagem, lang="por") #
print(texto)
