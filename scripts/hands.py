import cv2
import mediapipe as mp
import math
import numpy as np
import random

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=6)  # Limitar a detecção para duas mãos
mpDraw = mp.solutions.drawing_utils

class BouncingWord:
    def __init__(self, text, x, y, vx, vy, color):
        self.text = text
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.is_held = False  # Flag para indicar se a palavra está sendo "segurada"

    def draw(self, img):
        cv2.putText(img, self.text, (self.x, self.y), self.font, 1, self.color, 2, cv2.LINE_AA)

    def update(self, width, height):
        if not self.is_held:  # Atualiza apenas se a palavra não estiver sendo segurada
            self.x += self.vx
            self.y += self.vy

            text_size = cv2.getTextSize(self.text, self.font, 1, 2)[0]  # Tamanho da palavra

            if self.x <= 0 or self.x + text_size[0] >= width:
                self.vx = -self.vx
            if self.y - text_size[1] <= 0 or self.y >= height:
                self.vy = -self.vy

def bouncing_words():
    # largura e altura da janela
    width, height = 1080, 720

    cap = cv2.VideoCapture(0)

    words = ["LA", "PIS", "CO", "PO", "BA", "NA", "NA", "MAO"]
    bouncing_words_list = []

    for word in words:
        bouncing_word = BouncingWord(word, random.randint(50, width-150), random.randint(50, height-50),
                                      random.choice([-1, 1]) * random.randint(3, 6), random.choice([-1, 1]) * random.randint(3, 6),
                                      (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        bouncing_words_list.append(bouncing_word)

    selected_word = None  # Palavra que está sendo segurada

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        if not success:
            break

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        for bouncing_word in bouncing_words_list:
            bouncing_word.update(width, height)
            bouncing_word.draw(img)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                thumb_tip = handLms.landmark[4]
                index_tip = handLms.landmark[8]
                thumb_x, thumb_y = int(thumb_tip.x * width), int(thumb_tip.y * height)
                index_x, index_y = int(index_tip.x * width), int(index_tip.y * height)
                distance = math.hypot(index_x - thumb_x, index_y - thumb_y)

                if distance < 40:  # Se polegar e indicador estiverem próximos o suficiente
                    if selected_word is None:  # Se não estivermos segurando nenhuma palavra
                        # Encontrar a palavra mais próxima da área de contato
                        for word in bouncing_words_list:
                            word_x, word_y = word.x, word.y
                            text_size = cv2.getTextSize(word.text, word.font, 1, 2)[0]  # Tamanho da palavra
                            word_center_x = word_x + text_size[0] // 2
                            word_center_y = word_y - text_size[1] // 2

                            distance_to_word = math.hypot(word_center_x - index_x, word_center_y - index_y)
                            if distance_to_word < 50:  # Limite para detectar se a palavra está perto o suficiente
                                selected_word = word
                                word.is_held = True  # Marcar a palavra como "segurada"
                                break
                    else:
                        # Atualizar a posição da palavra com base na posição dos dedos
                        selected_word.x = index_x
                        selected_word.y = index_y
                else:
                    if selected_word:
                        selected_word.is_held = False  # Liberar a palavra
                        selected_word = None  # Nenhuma palavra mais está sendo segurada

        cv2.imshow("Bouncing Words", img)
        key = cv2.waitKey(30)
        if key == 27:  # Sair ao pressionar 'Esc'
            break

    cap.release()
    cv2.destroyAllWindows()

bouncing_words()
