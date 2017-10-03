from KeyInput import W, A, S, D, SPACE, pressKey, releaseKey
import time
from win32api import GetCursorPos

while True:
    x, y = GetCursorPos()
    print(x, y)
