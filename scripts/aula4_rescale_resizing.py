import cv2 
import numpy as np

cap = cv2.VideoCapture('assets/videos/dog.mp4')

#criar função que faz o rescale para cada frame individual

def rescale_frame(frame: np.array, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def resize_frame(width: int, height: int):
    cap.set(3, width)
    cap.set(4, height)


img = cv2.imread('assets/fotos/cat.jpg')
# cv2.imshow('Janela do gato', img)

# resize_img = rescale_frame(img, scale=0.2)
# cv2.imshow('Janela do gato', resize_img)
# cv2.waitKey(0)

# live video 

while True:
    _, frame = cap.read()
    frame_resized = rescale_frame(frame, scale=0.2)
    cv2.imshow('video do doguinho', frame_resized)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
