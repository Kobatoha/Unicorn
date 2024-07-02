import time

from PIL import Image, ImageDraw
from datetime import datetime
import os
import pygetwindow as gw
import pyautogui
import win32gui
import win32ui
import win32con
import win32api

if not os.path.exists('screenshots'):
    os.makedirs('screenshots')


def get_lineage_hwnd():
    windows = gw.getWindowsWithTitle('Lineage II')
    windows_hwnd = []
    for window in windows:
        print(f"Window Title: {window.title}, Window ID: {window._hWnd}")
        windows_hwnd.append(window._hWnd)
    return windows_hwnd


def check_active_window():
    active = window.isActive
    return active


def create_screenshot(hwnd):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x2C, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x2C, 0)
    directory = r'C:\Games\LineageII Essence\Screenshot'
    file = os.listdir(directory)[-1]
    return rf'{directory}\{file}'


def get_red_pixels(image):
    pixels = image.load()

    desired_red_color = (112, 20, 7)

    red_pixels = []

    for y in range(cropped_image.size[1]):
        for x in range(cropped_image.size[0]):
            current_color = pixels[x, y]

            if abs(current_color[0] - desired_red_color[0]) < 20 and \
                    abs(current_color[1] - desired_red_color[1]) < 20 and \
                    abs(current_color[2] - desired_red_color[2]) < 20:
                red_pixels.append((x, y))

    return len(red_pixels)


def check_health_bar():
    file = create_screenshot(hwnd)
    image = Image.open(file)
    x1, y1 = 63, 0
    x2, y2 = x1 + 345, y1 + 33

    cropped_image = image.crop((x1, y1, x2, y2))

    red_pixels = get_red_pixels(cropped_image)
    if red_pixels <= 200:
        print('Боец погиб')
    else:
        print('Боец еще в строю')

    time.sleep(2)
    os.remove(file)
