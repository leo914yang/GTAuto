import win32con
from PIL import ImageGrab
import cv2
import numpy as np
import win32gui
import win32api
import time
from tkinter import *
import threading


def math_img(Target, value=0.7):
    try:
        im = np.array(ImageGrab.grab())
        img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(Target, 0)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = value
        loc = np.where(res >= threshold)
        print(int(loc[1][0]), int(loc[0][0]))
        return int(loc[1][0]), int(loc[0][0])
    except Exception:
        print(Target, "not found")
        return 0, 0


def image_search_click(Target):
    windows_search(wdname=u"BlueStacks")
    time.sleep(2)
    x, y = math_img(Target)
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(1)


def windows_search(wdname):
    hwnd = win32gui.FindWindow(0, wdname)
    if not hwnd:
        print("找不到視窗，請確認窗口名稱:[%s]" % wdname)
        exit()
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)


def DrinkCoffee():
    image_search_click("adventure.png")
    time.sleep(1)

    image_search_click("stage.png")
    time.sleep(1)

    image_search_click("water.png")
    time.sleep(1)

    image_search_click("lv70.png")
    time.sleep(1)

    image_search_click("AutoRepeat.png")
    time.sleep(1)

    for i in range(7):
        image_search_click("plus.png")
        time.sleep(0.5)

    image_search_click("BattleStart.png")


localtime = time.localtime(time.time())
while True:
    if localtime.tm_hour == 12 and localtime.tm_min == 0:
        DrinkCoffee()
