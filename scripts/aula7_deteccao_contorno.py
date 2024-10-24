import cv2
import numpy as np

img = cv2.imread('assets/fotos/cats.jpg')
#cv2.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# 2. detecção de contornos

#a. borrar a imagem com GaussianBlur

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
#cv2.imshow('Blur', blur)

#b. detecção de bordas com Canny
canny = cv2.Canny(blur, 125, 175)
#cv2.imshow('Canny Edges', canny)

# Para uma melhor acurácia, use imagens binárias. 
# Métodos de Aproximação de Contornos
# cv2.RETR_LIST: Retorna todos os contornos
# cv2.RETR_EXTERNAL: Retorna apenas os contornos externos
# cv2.RETR_CCOMP: Retorna todos os contornos organizados em dois níveis

# cv2.CHAIN_APPROX_NONE: Armazena todos os pontos do contorno
# cv2.CHAIN_APPROX_SIMPLE: Comprime os pontos do contorno e armazena apenas os pontos extremos
# cv2.CHAIN_APPROX_TC89_L1: Aplica o algoritmo de aproximação de contornos de Tian-Chen
# cv2.CHAIN_APPROX_TC89_KCOS: Aplica o algoritmo de aproximação de contornos de Tian-Chen e Nevatia-Babu

contornos, hier = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contornos)} contornos encontrados!')

cv2.drawContours(blank, contornos, -1, (0,0,255), 1)
cv2.imshow('Contornos Desenhados', blank)


cv2.waitKey(0)