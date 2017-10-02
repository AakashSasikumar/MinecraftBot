import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

trainingDataPath = 'Data/trainingData.npy'

trainingData = np.load(trainingDataPath)
df = pd.DataFrame(trainingData)
print(Counter(df[1].apply(str)))
"""

This was the result I got after playing for 30500 frames (GRAY and 160, 90)
Counter({'[0, 1, 0, 0]': 14641, '[0, 1, 0, 1]': 3379, '[1, 1, 0, 0]': 3199,
'[0, 1, 1, 0]': 2359,'[0, 0, 0, 0]': 2091, '[1, 0, 0, 0]': 1725,
'[0, 0, 1, 0]': 1466, '[0, 1, 1, 1]': 1058, '[1, 1, 0, 1]': 428,
'[0, 0, 0, 1]': 142, '[1, 1, 1, 1]': 9, '[1, 1, 1, 0]': 3})

"""

shuffle(trainingData)

up = []
left = []
leftUp = []
right = []
rightUp = []
space = []
upSpace = []
rightUpSpace = []
leftUpSpace = []
none = []


for data in trainingData:
    img = data[0]
    choice = data[1]
    # Up
    if choice == [0, 1, 0, 0]:
        up.append([img, choice])
    # Up and Space
    if choice == [0, 1, 0, 1]:
        upSpace.append([img, choice])
    # Left and Up
    if choice == [1, 1, 0, 0]:
        leftUp.append([img, choice])
    # Right and Up
    if choice == [0, 1, 1, 0]:
        rightUp.append([img, choice])
    # none
    if choice == [0, 0, 0, 0]:
        none.append([img, choice])
    # Left
    if choice == [1, 0, 0, 0]:
        left.append([img, choice])
    # Right
    if choice == [0, 0, 1, 0]:
        right.append([img, choice])
    # Right Up Space
    if choice == [0, 1, 1, 1]:
        rightUpSpace.append([img, choice])
    # Left Up Space
    if choice == [1, 1, 0, 1]:
        leftUpSpace.append([img, choice])
    # Space
    if choice == [0, 0, 0, 1]:
        space.append([img, choice])

    # remove these combinations
    # [A, W, D, Space] no idea how this came
    if choice == [1, 1, 1, 1]:
        continue
    # [A, W, D] no idea how this came either
    if choice == [1, 1, 1, 0]:
        continue

up = up[:len(upSpace)]

finalData = up + upSpace + right + left + rightUp + leftUp + space + \
            leftUpSpace + rightUpSpace + None

finalDataPath = 'Data/balancedTrainingData.npy'
np.save(finalDataPath, finalData)
print(len(finalData))
