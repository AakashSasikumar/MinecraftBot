import numpy as np
import cv2
import time
import ScreenCapture as sc
from KeyPressRecorder import keyCheck
import os
from Alexnet import alexnet
from KeyInput import pressKey, releaseKey, W, A, D, SPACE


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

WIDTH = 160
HEIGHT = 90
LR = 0.001
EPOCH = 30
MODEL_NAME = 'MinecraftBot-{}-{}-{}-epochs.model'.format(LR, 'alexnet', EPOCH)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)
# print("down")
# pyautogui.keyDown(W)
# time.sleep(1)
# pyautogui.keyUp(W)
paused = False
while(True):
    if not paused:
        screenImage = cv2.resize(sc.getScreen(), (160, 90))
        prediction = model.predict([screenImage.reshape(WIDTH, HEIGHT, 1)])
        choice = np.around(prediction).astype(int).tolist()
        print(choice)

        # Up
        if choice == [[0., 1., 0., 0]]:
            print("Up")
            pressKey(W)
            releaseKey(SPACE)
            releaseKey(A)
            releaseKey(D)
            # time.sleep(0.5)

        # Up and Space
        if choice == [[0., 1., 0., 1.]]:
            print("Up and Space")
            pressKey(W)
            pressKey(SPACE)
            releaseKey(A)
            releaseKey(D)
        # Left and Up
        if choice == [[1., 1., 0., 0]]:
            print("Left and Up")
            pressKey(A)
            pressKey(W)
            releaseKey(SPACE)
            releaseKey(D)
        # Right and Up
        if choice == [[0., 1., 1., 0]]:
            print("Right and Up")
            pressKey(W)
            pa.keyDwon(D)
            releaseKey(A)
            releaseKey(SPACE)
        # # none
        # if choice == [[0., 0., 0., 0]]:
        #     print("none")
        #     releaseKey(W)
        #     releaseKey(SPACE)
        #     releaseKey(A)
        #     releaseKey(D)
        # Left
        if choice == [[1., 0., 0., 0]]:
            print("Left")
            pressKey(A)
            releaseKey(SPACE)
            releaseKey(W)
            releaseKey(D)
        # Right
        if choice == [[0., 0., 1., 0]]:
            print(" Right")
            pressKey(D)
            releaseKey(SPACE)
            releaseKey(A)
            releaseKey(W)
        # Right Up Space
        if choice == [[0., 1., 1., 1.]]:
            print("Right Up Space")
            pressKey(D)
            pressKey(SPACE)
            pressKey(W)
            releaseKey(D)
        # Left Up Space
        if choice == [[1., 1., 0., 1.]]:
            print("Left Up Space")
            pressKey(W)
            pressKey(A)
            pressKey(SPACE)
            releaseKey(D)
        # Space
        if choice == [[0., 0., 0., 1.]]:
            print("Space")
            pressKey(SPACE)
            releaseKey(W)
            releaseKey(A)
            releaseKey(D)

    keys = keyCheck()
    if 'T' in keys:
        if paused:
            paused = False
            time.sleep(1)
        else:
            paused = True
            releaseKey(SPACE)
            releaseKey(W)
            releaseKey(A)
            releaseKey(D)
