#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2 # importar o opencv -> para instalar rode pip install opencv-python
import mediapipe as mp # para instalar rode pip install mediapipe

webcam = cv2.VideoCapture(0) # para conectar o python com a nossa webcam.

reconhecimento_rosto = mp.solutions.face_detection # ativando a solução de reconhecimento de rosto
desenho = mp.solutions.drawing_utils # ativando a solução de desenho
reconhecedor_rosto = reconhecimento_rosto.FaceDetection() # criando o item que consegue ler uma imagem e reconhecer os rostos ali dentro

while webcam.isOpened():
    validacao, frame = webcam.read() # lê a imagem da webcam
    if not validacao:
        break
    imagem = frame
    lista_rostos = reconhecedor_rosto.process(imagem) # usa o reconhecedor para criar uma lista com os rostos reconhecidos
    
    if lista_rostos.detections: # caso algum rosto tenha sido reconhecido
        for rosto in lista_rostos.detections: # para cada rosto que foi reconhecido
            desenho.draw_detection(imagem, rosto) # desenha o rosto na imagem
    
    cv2.imshow("Rostos na sua webcam", imagem) # mostra a imagem da webcam para a gente
    if cv2.waitKey(5) == 27: # ESC # garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da webcam
        break
webcam.release() # encerra a conexão com a webcam
cv2.destroyAllWindows() # fecha a janela que mostra o que a webcam está vendo


# In[ ]:




