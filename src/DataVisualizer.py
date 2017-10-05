import numpy as np
import cv2

trainingDataFile = './Data/trainingDataColor-full.npy'
trainingData = np.load(trainingDataFile)

for data in trainingData:
    img = data[0]
    choice = data[1]
    cv2.imshow('test', img)
    print(choice)
    if cv2.waitKey(25) & 0XFF == ord('q'):
        cv2.destroyAllWindows()
        break
