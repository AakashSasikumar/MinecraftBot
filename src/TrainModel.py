import numpy as np
import cv2
import time
import ScreenCapture as sc
from KeyPressRecorder import keyCheck
import os


def keysToOutput(keys):
    # [A, W, D, Space]
    output = [0, 0, 0, 0]    
    if 'W' in keys:
        output[1] = 1
        if ' ' in keys:
            output[3] = 1
        if 'D' in keys:
            output[2] = 1
        if 'A' in keys:
            output[0] = 1
        return output
    elif 'A' in keys:
        output[0] = 1
        return [1, 0, 0, 0]
    elif 'D' in keys:
        output[2] = 1
        return [0, 0, 1, 0]
    elif ' ' in keys:
        output[3] = 1
        return [0, 0, 0, 1]
    return output

trainingDataPath = '../Data/trainingDataColor-p1.npy'
if os.path.isfile(trainingDataPath):
    print("Loading previous data")
    trainingData = list(np.load(trainingDataFile))
else:
    print("File doesn't exist, fresh start")
    trainingData = []

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

i = 2
while(True):
    screenImage = cv2.resize(sc.getScreen(), (480, 270))
    keys = keyCheck()
    output = keysToOutput(keys)
    trainingData.append([screenImage, output])
    print(output)
    if len(trainingData) % 6000 == 0:
        print(len(trainingData))
        trainingDataPath = '../Data/trainingDataColor-p{}'.format(i)
        i += 1
        np.save(trainingDataFile, trainingData)
