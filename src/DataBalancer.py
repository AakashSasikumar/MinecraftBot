import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

trainingDataPath = './Data/trainingDataColor-full3.npy'

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

"""
This was result I got for trainingDataColor-full

Counter({'[0, 1, 0, 0]': 6108, '[0, 1, 0, 1]': 1866, '[0, 1, 1, 0]': 1240,
'[1, 1, 0, 0]': 939, '[0, 0, 0, 0]': 561, '[1, 1, 0, 1]': 477,
'[0, 1, 1, 1]': 370, '[0, 0, 1, 0]': 234, '[1, 0, 0, 0]': 201,
'[0, 0, 0, 1]': 4})

"""

"""
This was result I got for trainingDataColor-full2
Counter({'[0, 1, 0, 0]': 7024, '[0, 1, 0, 1]': 1597, '[1, 1, 0, 0]': 1549,
'[0, 1, 1, 0]': 857, '[0, 0, 0, 0]': 415, '[0, 1, 1, 1]': 185,
'[1, 0, 0, 0]': 184, '[0, 0, 1, 0]': 93, '[1, 1, 0, 1]': 92,
'[0, 0, 0, 1]': 3, '[1, 1, 1, 1]': 1})

"""

"""
This was result I got for trainingDataColor-full3
Counter({'[0, 1, 0, 0]': 6762, '[0, 1, 0, 1]': 1351, '[1, 1, 0, 0]': 1245,
'[0, 1, 1, 0]': 1127, '[0, 0, 0, 0]': 606, '[0, 0, 1, 0]': 299,
'[0, 1, 1, 1]': 258, '[1, 1, 0, 1]': 224, '[1, 0, 0, 0]': 102,
'[0, 0, 0, 1]': 25, '[1, 1, 1, 1]': 1})

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
            leftUpSpace + rightUpSpace
# + None

finalDataPath = 'Data/test/balancedTrainingDataColor-p3.npy'
np.save(finalDataPath, finalData)
print(len(finalData))
