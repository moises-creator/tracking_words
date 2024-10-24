import cv2
import mediapipe as mp
import numpy as np
import math
import time

import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from hand_tracking_module import VanzeDetector

capture = cv2.VideoCapture(0)
capture2 = cv2.VideoCapture(0)
# configuração do codec de vídeo e resolução

capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
cam_width = 1920
cam_height = 1080
capture.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

while True:
    _, img = capture.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




