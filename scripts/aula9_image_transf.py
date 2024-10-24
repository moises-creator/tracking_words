import cv2
import numpy as np

img = cv2.imread('assets/fotos/park.jpg')
cv2.imshow('Original', img)

# Definições de funcoes

def translate(img, x, y): 
    '''
    -x esquerda
    -y acima
    x direita
    y abaixo

    '''

    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    # coletamos as dimensions da imagem

    dimensions = (img.shape[1], img.shape[0])
    # retornar a função warpAffine

    return cv2.warpAffine(img, translation_matrix, dimensions)

# img_tr = translate(img, 100, 250)
# cv2.imshow('Translated', img_tr)

def rotate(img, angle, rotation_point=None):
    height, width = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotation_matrix, dimensions)

# rotated = rotate(img, 180)
# cv2.imshow('Rotated', rotated)

# Flipping: inverte um array em 2d

#flip = cv2.flip(img, 0) # flip vertical
#flip = cv2.flip(img, 1) # flip horizontal
#flip = cv2.flip(img, -1) # flip vertical e horizontal

#cv2.imshow('Flip', flip)

# Resizing e Cropping: redimensiona e corta a imagem

resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('Resized', resized)

cropped = img[100:400, 200:500]
cv2.imshow('Cropped', cropped)


cv2.waitKey(0)