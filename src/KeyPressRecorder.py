import win32api as wapi
import time

keyList = ["\b"]
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456879,.'APS$/\\":
    keyList.append(ch)


def keyCheck():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
            print(keys)
    return keys
