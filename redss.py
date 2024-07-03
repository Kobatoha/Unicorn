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
import mouse
import random
from pywinauto import Desktop


def get_lineage_hwnd():
    windows = gw.getWindowsWithTitle('Lineage II')
    windows_hwnd = []
    for window in windows:
        print(f"Window Title: {window.title}, Window ID: {window._hWnd}")
        windows_hwnd.append(window._hWnd)
    return windows_hwnd


def get_lineage_windows():
    windows = gw.getWindowsWithTitle('Lineage II')
    return windows


def check_active_window(hwnd) -> bool:
    windows = get_lineage_windows()
    for window in windows:
        if window._hWnd == hwnd:
            active = window.isActive
            if not active:
                window.activate()


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

    for y in range(image.size[1]):
        for x in range(image.size[0]):
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


def get_mouse_position():
    print('У вас есть 5 секунд навести мышку в нужное место')
    time.sleep(5)

    x, y = pyautogui.position()

    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[0], rect[1]

    x_rel = x - x0
    y_rel = y - y0

    return x_rel, y_rel


def send_left_click_sm(hwnd, x, y):
    lParam = win32api.MAKELONG(x, y)

    # Отправляем сообщение о нажатии левой кнопки мыши
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, lParam)


def send_left_click_pyautogui(hwnd, x, y):
    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[0], rect[1]

    pyautogui.moveTo(x0 + x, y0 + y)
    time.sleep(2)
    pyautogui.leftClick()
    mouse.click('left')


def get_taskbar_icon():
    window_name = 'LaunchRes —1 запущенное окно'
    desktop = Desktop(backend="uia")
    taskbar = desktop.window(class_name='Shell_TrayWnd')
    icons = taskbar.descendants(control_type="Button", title='LaunchRes —1 запущенное окно')
    icon_l2 = [icon for icon in icons if window_name in icon.window_text()]
    time.sleep(2)
    icons[0].click_input()


if __name__ == '__main__':
    hwnd = get_lineage_hwnd()
    time.sleep(5)
    get = get_mouse_position()
    rect_recovery_exp = (910, 553)
    send_left_click_pyautogui(hwnd, rect_recovery_exp[0], rect_recovery_exp[1])
    time.sleep(2)
    rect_recovery_agree = (879, 567)
    send_left_click_pyautogui(hwnd, rect_recovery_agree[0], rect_recovery_agree[1])
