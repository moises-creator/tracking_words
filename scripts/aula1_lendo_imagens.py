import cv2

# Função imread

img = cv2.imread('assets/fotos/cat.jpg')
img_grande = cv2.imread('assets/fotos/cat_large.jpg')
# Função imshow
cv2.imshow('Janela do gato', img)
cv2.imshow('Janela do gato grande', img_grande)

# Função waitKey
cv2.waitKey(0)