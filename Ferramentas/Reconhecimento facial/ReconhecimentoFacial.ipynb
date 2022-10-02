{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fcb5e615",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2 # importar o opencv -> para instalar rode pip install opencv-python\n",
    "import mediapipe as mp # para instalar rode pip install mediapipe\n",
    "\n",
    "webcam = cv2.VideoCapture(0) # para conectar o python com a nossa webcam.\n",
    "\n",
    "reconhecimento_rosto = mp.solutions.face_detection # ativando a solução de reconhecimento de rosto\n",
    "desenho = mp.solutions.drawing_utils # ativando a solução de desenho\n",
    "reconhecedor_rosto = reconhecimento_rosto.FaceDetection() # criando o item que consegue ler uma imagem e reconhecer os rostos ali dentro\n",
    "\n",
    "while webcam.isOpened():\n",
    "    validacao, frame = webcam.read() # lê a imagem da webcam\n",
    "    if not validacao:\n",
    "        break\n",
    "    imagem = frame\n",
    "    lista_rostos = reconhecedor_rosto.process(imagem) # usa o reconhecedor para criar uma lista com os rostos reconhecidos\n",
    "    \n",
    "    if lista_rostos.detections: # caso algum rosto tenha sido reconhecido\n",
    "        for rosto in lista_rostos.detections: # para cada rosto que foi reconhecido\n",
    "            desenho.draw_detection(imagem, rosto) # desenha o rosto na imagem\n",
    "    \n",
    "    cv2.imshow(\"Rostos na sua webcam\", imagem) # mostra a imagem da webcam para a gente\n",
    "    if cv2.waitKey(5) == 27: # ESC # garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da webcam\n",
    "        break\n",
    "webcam.release() # encerra a conexão com a webcam\n",
    "cv2.destroyAllWindows() # fecha a janela que mostra o que a webcam está vendo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "033623d0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
