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
import ctypes
from ctypes import wintypes
from PIL import Image
import pytesseract
import cv2
import re


def get_hp_string(image: Image):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    recognized_text = pytesseract.image_to_string(image)

    return recognized_text


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


def check_active_window(hwnd):
    windows = get_lineage_windows()
    for window in windows:
        if window._hWnd == hwnd:
            active = window.isActive
            if not active:
                time.sleep(2)
                get_focus_lineage_window(hwnd)


def check_active_window_insert(hwnd):
    windows = get_lineage_windows()
    for window in windows:
        if window._hWnd == hwnd:
            active = window.isActive
            return active


def create_screenshot(hwnd, directory=r'C:\Games\LineageII Essence\Screenshot'):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 0x2C, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 0x2C, 0)
    directory = r'C:\l2essence\Screenshot'
    file = os.listdir(directory)[-1]
    return rf'{directory}\{file}'


def screenshot_window(hwnd, output_path="unishot.png"):
    # Получаем размеры окна
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left - 16
    height = bottom - top - 41

    # Получаем контекст устройства окна
    hwnd_dc = win32gui.GetWindowDC(hwnd)
    mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
    save_dc = mfc_dc.CreateCompatibleDC()

    # Создаем объект для сохранения битмапа
    save_bitmap = win32ui.CreateBitmap()
    save_bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
    save_dc.SelectObject(save_bitmap)

    # Копируем содержимое клиентской области в битмап
    save_dc.BitBlt((0, 0), (width, height), mfc_dc, (8, 31), win32con.SRCCOPY)

    # Конвертируем данные из битмапа в изображение Pillow
    bmp_info = save_bitmap.GetInfo()
    bmp_data = save_bitmap.GetBitmapBits(True)
    img = Image.frombuffer("RGB", (bmp_info['bmWidth'], bmp_info['bmHeight']), bmp_data, "raw", "BGRX", 0, 1)

    # Сохраняем изображение в файл
    img.save(output_path)
    # img.show()

    # Освобождаем ресурсы
    win32gui.DeleteObject(save_bitmap.GetHandle())
    save_dc.DeleteDC()
    mfc_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwnd_dc)

    return img


def get_window_size(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    height = bottom - top
    width = right - left
    return width, height


def get_window_to_village(hwnd, w=193, h=193, border=10):
    window_width, window_height = get_window_size(hwnd)

    center_x = window_width // 2
    center_y = window_height // 2 + border

    start_x = center_x - w // 2
    start_y = center_y - h // 2

    return (start_x, start_y, start_x + w, start_y + h)


def get_window_free_up(hwnd):
    rect = get_window_to_village(hwnd)
    width = rect[0]
    height = rect[1]

    w_up = width + 15
    h_up = height + 140

    w_down = w_up + 158
    h_down = h_up + 20
    random_w = random.randint(w_up, w_down)
    random_h = random.randint(h_up, h_down)

    return random_w, random_h


def get_window_free_agree(hwnd):
    rect = get_window_to_village(hwnd)
    width = rect[0]
    height = rect[1]

    w_up = width + 17
    h_up = height + 135

    w_down = w_up + 70
    h_down = h_up + 17
    random_w = random.randint(w_up, w_down)
    random_h = random.randint(h_up, h_down)

    return random_w, random_h


def get_window_pay_agree(hwnd):
    rect = get_window_to_village(hwnd)
    width = rect[0]
    height = rect[1]

    w_up = width + 6
    h_up = height + 175

    w_down = w_up + 75
    h_down = h_up + 15
    random_w = random.randint(w_up, w_down)
    random_h = random.randint(h_up, h_down)

    return random_w, random_h


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


def check_health_bar(hwnd):
    file = create_screenshot(hwnd)
    image = Image.open(file)
    x1, y1 = 63, 0
    x2, y2 = x1 + 345, y1 + 33
    death = False

    cropped_image = image.crop((x1, y1, x2, y2))

    red_pixels = get_red_pixels(cropped_image)
    if red_pixels <= 200:
        print('Боец погиб')
        death = True
    else:
        print('Боец еще в строю')
        death = False
        os.remove(file)

    time.sleep(2)
    return death


def grey_image_filter(image: str):
    cv2_image = cv2.imread(image)

    gray_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)

    _, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    cv2.imwrite("gray_image.png", threshold_image)
    return "gray_image.png"


def pattern_hp(string: str):
    pattern = r"(\d+)/(\d+)"

    matches = re.search(pattern, string)
    if matches:
        number1 = matches.group(1)  # Число до слэша
        number2 = matches.group(2)  # Число после слэша

        return number1, number2


def pattern_error_hp(string: str):
    pattern = r"(\d+)"

    match = re.search(pattern, string)
    return match.group()


def check_health_bar_string(hwnd):
    image = screenshot_window(hwnd)
    x1, y1 = 63, 0
    x2, y2 = x1 + 345, y1 + 33
    death = False

    file_name = 'hp_bar.png'
    cropped_image = image.crop((x1, y1, x2, y2))

    hp_color = get_red_pixels(cropped_image)
    # hp_string = get_hp_string(cropped_image)

    # if hp_string:
    #     try:
    #         current_hp, full_hp = pattern_hp(hp_string)
    #     except:
    #         error_hp = pattern_error_hp(hp_string)
    # else:
    #     current_hp, full_hp = 0, 0

    if hp_color == 0:
        print(f'Красных пикселей: {hp_color}')
        print(f'Боец погиб')
        death = True
    else:
        # print(f'Красных пикселей: {hp_color}')
        # print(f'Боец еще в строю')
        # print('-' * 60)
        death = False

    time.sleep(0.5)
    return death


def get_mouse_position():
    print('У вас есть 5 секунд навести мышку в нужное место')
    time.sleep(5)

    x, y = pyautogui.position()

    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[0], rect[1]

    x_rel = x - x0
    y_rel = y - y0

    return x_rel, y_rel


def send_left_click_pyautogui(hwnd, x, y):
    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[0], rect[1]

    pyautogui.moveTo(x0 + x, y0 + y, 0.25)
    time.sleep(1)
    pyautogui.leftClick()
    mouse.click('left')


def move_mouse(hwnd, x, y):
    rect = win32gui.GetWindowRect(hwnd)
    x0, y0 = rect[0], rect[1]

    pyautogui.moveTo(x0 + x, y0 + y, 0.25)


def get_focus_lineage_window(hwnd):
    desktop = Desktop(backend="uia")
    window = desktop.windows(title='Lineage II', handle=hwnd)[0].set_focus()


def free_res_rect():
    x = [852, 1006]
    y = [540, 555]
    new_x = random.randint(x[0], x[1])
    new_y = random.randint(y[0], y[1])

    return [new_x, new_y]


def res_agree_rect():
    x = [855, 915]
    y = [560, 573]
    new_x = random.randint(x[0], x[1])
    new_y = random.randint(y[0], y[1])

    return [new_x, new_y]


def res_agree_pay_rect():
    x = [845, 915]
    y = [599, 610]
    new_x = random.randint(x[0], x[1])
    new_y = random.randint(y[0], y[1])

    return [new_x, new_y]


def go_to_village(hwnd):
    flag = check_health_bar_string(hwnd)
    if flag:
        check_active_window(hwnd)
        time.sleep(0.5)
        rect_recovery_free_exp = get_window_free_up(hwnd)
        send_left_click_pyautogui(hwnd, rect_recovery_free_exp[0], rect_recovery_free_exp[1])
        time.sleep(0.5)
        rect_recovery_agree = get_window_free_agree(hwnd)
        send_left_click_pyautogui(hwnd, rect_recovery_agree[0], rect_recovery_agree[1])
        time.sleep(0.5)
        rect_recovery_pay_exp = get_window_pay_agree(hwnd)
        send_left_click_pyautogui(hwnd, rect_recovery_pay_exp[0], rect_recovery_pay_exp[1])
        time.sleep(0.5)
        return True
    return False


def use_teleport(hwnd):
    time.sleep(1)
    print('Летим на свободный телепорт')
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 122, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, 122, 0)


def use_teleport_random(hwnd):
    tp = ['f7', 'f8', 'f9', 'f10', 'f11']
    teleport = {
        'f7': 118,
        'f8': 119,
        'f9': 120,
        'f10': 121,
        'f11': 122
    }
    key = random.choice(tp)
    time.sleep(1)
    print(f'Летим на свободный телепорт ({key})')
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, teleport[key], 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, teleport[key], 0)


def night_use_teleport(hwnd):
    now = datetime.now().strftime('%H:%M')
    if '23:00' <= now <= '23:59' or '00:00' <= now <= '08:00':
        print('Перезалетаем на свободный телепорт')
        win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 122, 0)
        win32api.SendMessage(hwnd, win32con.WM_KEYUP, 122, 0)


if __name__ == '__main__':
    hwnd = get_lineage_hwnd()
    time.sleep(5)
    get = get_mouse_position()

