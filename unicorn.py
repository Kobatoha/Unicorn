import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QDrag
from PyQt5.QtCore import QSize, Qt, QMimeData, QTimer
import pyautogui
import datetime
from keyboard import add_hotkey
from pynput.keyboard import Key, Controller
import win32gui
import win32api
import win32con
from Ui_MainWindow import Ui_MainWindow
import json
from PyQt5.QtWidgets import QMessageBox


class Main(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_located)
        self.timer.start(5000)

        # Добавляем обработчик закрытия окна
        self.window = MainWindow
        self.window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint)
        self.window.closeEvent = self.closeEvent

    def closeEvent(self, event):
        # Вызываем функцию sys.exit() при закрытии окна
        QtWidgets.QApplication.closeAllWindows()
        QtWidgets.QApplication.exit()

    # settings file
    def save_settings(self):
        settings = {
            'edit_window_id': self.lineEdit_window_id.text(),

            'edit_f1': self.lineEdit_f1.text(),
            'edit_f2': self.lineEdit_f2.text(),
            'edit_f3': self.lineEdit_f3.text(),
            'edit_f4': self.lineEdit_f4.text(),
            'edit_f5': self.lineEdit_f5.text(),
            'edit_f6': self.lineEdit_f6.text(),
            'edit_f7': self.lineEdit_f7.text(),
            'edit_f8': self.lineEdit_f8.text(),
            'edit_f9': self.lineEdit_f9.text(),
            'edit_f10': self.lineEdit_f10.text(),

            'checkbox_f1': self.checkBox_f1.isChecked(),
            'checkbox_f2': self.checkBox_f2.isChecked(),
            'checkbox_f3': self.checkBox_f3.isChecked(),
            'checkbox_f4': self.checkBox_f4.isChecked(),
            'checkbox_f5': self.checkBox_f5.isChecked(),
            'checkbox_f6': self.checkBox_f6.isChecked(),
            'checkbox_f7': self.checkBox_f7.isChecked(),
            'checkbox_f8': self.checkBox_f8.isChecked(),
            'checkbox_f9': self.checkBox_f9.isChecked(),
            'checkbox_f10': self.checkBox_f10.isChecked(),

            'edit_1': self.lineEdit_1.text(),
            'edit_2': self.lineEdit_2.text(),
            'edit_3': self.lineEdit_3.text(),
            'edit_4': self.lineEdit_4.text(),
            'edit_5': self.lineEdit_5.text(),
            'edit_6': self.lineEdit_6.text(),
            'edit_7': self.lineEdit_7.text(),
            'edit_8': self.lineEdit_8.text(),
            'edit_9': self.lineEdit_9.text(),
            'edit_0': self.lineEdit_0.text(),

            'checkbox_1': self.checkBox_1.isChecked(),
            'checkbox_2': self.checkBox_2.isChecked(),
            'checkbox_3': self.checkBox_3.isChecked(),
            'checkbox_4': self.checkBox_4.isChecked(),
            'checkbox_5': self.checkBox_5.isChecked(),
            'checkbox_6': self.checkBox_6.isChecked(),
            'checkbox_7': self.checkBox_7.isChecked(),
            'checkbox_8': self.checkBox_8.isChecked(),
            'checkbox_9': self.checkBox_9.isChecked(),
            'checkbox_0': self.checkBox_0.isChecked(),
        }
        with open('settings.json', 'w') as file:
            json.dump(settings, file)

    def load_settings(self):
        try:
            with open('settings.json', 'r') as file:
                settings = json.load(file)

                self.lineEdit_window_id.setText(settings.get('edit_window_id', ''))

                self.lineEdit_f1.setText(settings.get('edit_f1', '')),
                self.lineEdit_f2.setText(settings.get('edit_f2', '')),
                self.lineEdit_f3.setText(settings.get('edit_f3', '')),
                self.lineEdit_f4.setText(settings.get('edit_f4', '')),
                self.lineEdit_f5.setText(settings.get('edit_f5', '')),
                self.lineEdit_f6.setText(settings.get('edit_f6', '')),
                self.lineEdit_f7.setText(settings.get('edit_f7', '')),
                self.lineEdit_f8.setText(settings.get('edit_f8', '')),
                self.lineEdit_f9.setText(settings.get('edit_f9', '')),
                self.lineEdit_f10.setText(settings.get('edit_f10', '')),

                self.checkBox_f1.setChecked(settings.get('checkbox_f1', '')),
                self.checkBox_f2.setChecked(settings.get('checkbox_f2', '')),
                self.checkBox_f3.setChecked(settings.get('checkbox_f3', '')),
                self.checkBox_f4.setChecked(settings.get('checkbox_f4', '')),
                self.checkBox_f5.setChecked(settings.get('checkbox_f5', '')),
                self.checkBox_f6.setChecked(settings.get('checkbox_f6', '')),
                self.checkBox_f7.setChecked(settings.get('checkbox_f7', '')),
                self.checkBox_f8.setChecked(settings.get('checkbox_f8', '')),
                self.checkBox_f9.setChecked(settings.get('checkbox_f9', '')),
                self.checkBox_f10.setChecked(settings.get('checkbox_f10', '')),

                self.lineEdit_1.setText(settings.get('edit_1', '')),
                self.lineEdit_2.setText(settings.get('edit_2', '')),
                self.lineEdit_3.setText(settings.get('edit_3', '')),
                self.lineEdit_4.setText(settings.get('edit_4', '')),
                self.lineEdit_5.setText(settings.get('edit_5', '')),
                self.lineEdit_6.setText(settings.get('edit_6', '')),
                self.lineEdit_7.setText(settings.get('edit_7', '')),
                self.lineEdit_8.setText(settings.get('edit_8', '')),
                self.lineEdit_9.setText(settings.get('edit_9', '')),
                self.lineEdit_0.setText(settings.get('edit_0', '')),

                self.checkBox_1.setChecked(settings.get('checkbox_1', '')),
                self.checkBox_2.setChecked(settings.get('checkbox_2', '')),
                self.checkBox_3.setChecked(settings.get('checkbox_3', '')),
                self.checkBox_4.setChecked(settings.get('checkbox_4', '')),
                self.checkBox_5.setChecked(settings.get('checkbox_5', '')),
                self.checkBox_6.setChecked(settings.get('checkbox_6', '')),
                self.checkBox_7.setChecked(settings.get('checkbox_7', '')),
                self.checkBox_8.setChecked(settings.get('checkbox_8', '')),
                self.checkBox_9.setChecked(settings.get('checkbox_9', '')),
                self.checkBox_0.setChecked(settings.get('checkbox_0', '')),

        except FileNotFoundError:
            pass

    ### functions ###
    def press_insert(self):
        self.pushButton_startstop.click()

    def hotkey_thread_insert(self):
        add_hotkey('INSERT', self.press_insert)

    def startstop(self):
        if self.pushButton_startstop.text() == 'Start':
            self.pushButton_startstop.setText('Stop')
            self.label_information_actions.setText("Started clicker")
            self.lineEdit_window_id.setDisabled(True)
            self.toggle_1(self.checkBox_1.checkState())
            self.toggle_2(self.checkBox_2.checkState())
            self.toggle_3(self.checkBox_3.checkState())
            self.toggle_4(self.checkBox_4.checkState())
            self.toggle_5(self.checkBox_5.checkState())
            self.toggle_6(self.checkBox_6.checkState())
            self.toggle_7(self.checkBox_7.checkState())
            self.toggle_8(self.checkBox_8.checkState())
            self.toggle_9(self.checkBox_9.checkState())
            self.toggle_0(self.checkBox_0.checkState())
            self.toggle_f1(self.checkBox_f1.checkState())
            self.toggle_f2(self.checkBox_f2.checkState())
            self.toggle_f3(self.checkBox_f3.checkState())
            self.toggle_f4(self.checkBox_f4.checkState())
            self.toggle_f5(self.checkBox_f5.checkState())
            self.toggle_f6(self.checkBox_f6.checkState())
            self.toggle_f7(self.checkBox_f7.checkState())
            self.toggle_f8(self.checkBox_f8.checkState())
            self.toggle_f9(self.checkBox_f9.checkState())
            self.toggle_f10(self.checkBox_f10.checkState())

        else:
            self.pushButton_startstop.setText('Start')
            self.label_information_actions.setText('Stopped clicker')
            self.lineEdit_window_id.setEnabled(True)
            self.pressed_1 = False
            self.pressed_2 = False
            self.pressed_3 = False
            self.pressed_4 = False
            self.pressed_5 = False
            self.pressed_6 = False
            self.pressed_7 = False
            self.pressed_8 = False
            self.pressed_9 = False
            self.pressed_0 = False
            self.pressed_f1 = False
            self.pressed_f2 = False
            self.pressed_f3 = False
            self.pressed_f4 = False
            self.pressed_f5 = False
            self.pressed_f6 = False
            self.pressed_f7 = False
            self.pressed_f8 = False
            self.pressed_f9 = False
            self.pressed_f10 = False

    def profile_load(self):
        self.label_information_actions.setText('Load profile')

    def profile_save(self):
        self.label_information_actions.setText('Save profile')

    def update_hot_time_icon(self):
        while True:
            time_now = datetime.datetime.now().strftime('%H:%M')
            if time_now >= '12:00' and time_now <= '14:00' or time_now >= '19:00' and time_now <= '23:00':
                self.label_hottime.setPixmap(QtGui.QPixmap("hot_time_on.png"))
            else:
                self.label_hottime.setPixmap(QtGui.QPixmap("hot_time_off.png"))
            time.sleep(60)

    def update_located(self):
        id = self.label_id_window.text()
        if id in self.lineEdit_window_id.text():
            self.pushButton_located.setIcon(QtGui.QIcon('target_on.png'))
            self.label_information_actions.setText('Windows located')
        else:
            self.pushButton_located.setIcon(QtGui.QIcon('target_off.png'))

    def toggle_1(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_1 = True
                self.press_1()
        else:
            self.pressed_1 = False

    def press_1(self):
        if self.pressed_1:
            interval = int(self.lineEdit_1.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 49, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 49, 0)
            QtCore.QTimer.singleShot(interval, self.press_1)

    def toggle_2(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_2 = True
                self.press_2()
        else:
            self.pressed_2 = False

    def press_2(self):
        if self.pressed_2:
            interval = int(self.lineEdit_2.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 50, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 50, 0)
            QtCore.QTimer.singleShot(interval, self.press_2)

    def toggle_3(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_3 = True
                self.press_3()
        else:
            self.pressed_3 = False

    def press_3(self):
        if self.pressed_3:
            interval = int(self.lineEdit_3.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 51, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 51, 0)
            QtCore.QTimer.singleShot(interval, self.press_3)

    def toggle_4(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_4 = True
                self.press_4()
        else:
            self.pressed_4 = False

    def press_4(self):
        if self.pressed_4:
            interval = int(self.lineEdit_4.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 52, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 52, 0)
            QtCore.QTimer.singleShot(interval, self.press_4)

    def toggle_5(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_5 = True
                self.press_5()
        else:
            self.pressed_5 = False

    def press_5(self):
        if self.pressed_5:
            interval = int(self.lineEdit_5.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 53, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 53, 0)
            QtCore.QTimer.singleShot(interval, self.press_5)

    def toggle_6(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_6 = True
                self.press_6()
        else:
            self.pressed_6 = False

    def press_6(self):
        if self.pressed_6:
            interval = int(self.lineEdit_6.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 54, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 54, 0)
            QtCore.QTimer.singleShot(interval, self.press_6)

    def toggle_7(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_7 = True
                self.press_7()
        else:
            self.pressed_7 = False

    def press_7(self):
        if self.pressed_7:
            interval = int(self.lineEdit_7.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 55, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 55, 0)
            QtCore.QTimer.singleShot(interval, self.press_7)

    def toggle_8(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_8 = True
                self.press_8()
        else:
            self.pressed_8 = False

    def press_8(self):
        if self.pressed_8:
            interval = int(self.lineEdit_8.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 56, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 56, 0)
            QtCore.QTimer.singleShot(interval, self.press_8)

    def toggle_9(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_9 = True
                self.press_9()
        else:
            self.pressed_9 = False

    def press_9(self):
        if self.pressed_9:
            interval = int(self.lineEdit_9.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 57, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 57, 0)
            QtCore.QTimer.singleShot(interval, self.press_9)

    def toggle_0(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_0 = True
                self.press_0()
        else:
            self.pressed_0 = False

    def press_0(self):
        if self.pressed_0:
            interval = int(self.lineEdit_0.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, 48, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, 48, 0)
            QtCore.QTimer.singleShot(interval, self.press_0)

    def toggle_f1(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f1 = True
                self.press_f1()
        else:
            self.pressed_f1 = False

    def press_f1(self):
        if self.pressed_f1:
            interval = int(self.lineEdit_f1.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F1, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F1, 0)
            QtCore.QTimer.singleShot(interval, self.press_f1)

    def toggle_f2(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f2 = True
                self.press_f2()
        else:
            self.pressed_f2 = False

    def press_f2(self):
        if self.pressed_f2:
            interval = int(self.lineEdit_f2.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F2, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F2, 0)
            QtCore.QTimer.singleShot(interval, self.press_f2)

    def toggle_f3(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f3 = True
                self.press_f3()
        else:
            self.pressed_f3 = False

    def press_f3(self):
        if self.pressed_f3:
            interval = int(self.lineEdit_f3.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F3, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F3, 0)
            QtCore.QTimer.singleShot(interval, self.press_f3)

    def toggle_f4(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f4 = True
                self.press_f4()
        else:
            self.pressed_f4 = False

    def press_f4(self):
        if self.pressed_f4:
            interval = int(self.lineEdit_f4.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F4, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F4, 0)
            QtCore.QTimer.singleShot(interval, self.press_f4)

    def toggle_f5(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f5 = True
                self.press_f5()
        else:
            self.pressed_f5 = False

    def press_f5(self):
        if self.pressed_f5:
            interval = int(self.lineEdit_f5.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F5, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F5, 0)
            QtCore.QTimer.singleShot(interval, self.press_f5)

    def toggle_f6(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f6 = True
                self.press_f6()
        else:
            self.pressed_f6 = False

    def press_f6(self):
        if self.pressed_f6:
            interval = int(self.lineEdit_f6.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F6, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F6, 0)
            QtCore.QTimer.singleShot(interval, self.press_f6)

    def toggle_f7(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f7 = True
                self.press_f7()
        else:
            self.pressed_f7 = False

    def press_f7(self):
        if self.pressed_f7:
            interval = int(self.lineEdit_f7.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F7, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F7, 0)
            QtCore.QTimer.singleShot(interval, self.press_f7)

    def toggle_f8(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f8 = True
                self.press_f8()
        else:
            self.pressed_f8 = False

    def press_f8(self):
        if self.pressed_f8:
            interval = int(self.lineEdit_f8.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F8, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F8, 0)
            QtCore.QTimer.singleShot(interval, self.press_f8)

    def toggle_f9(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f9 = True
                self.press_f9()
        else:
            self.pressed_f9 = False

    def press_f9(self):
        if self.pressed_f9:
            interval = int(self.lineEdit_f9.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F9, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F9, 0)
            QtCore.QTimer.singleShot(interval, self.press_f9)

    def toggle_f10(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.pressed_f10 = True
                self.press_f10()
        else:
            self.pressed_f10 = False

    def press_f10(self):
        if self.pressed_f10:
            interval = int(self.lineEdit_f10.text())
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYDOWN, win32con.VK_F10, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(self.lineEdit_window_id.text(), win32con.WM_KEYUP, win32con.VK_F10, 0)
            QtCore.QTimer.singleShot(interval, self.press_f10)

    def press_f11(self):
        self.pushButton_located.click()

    def hotkey_thread_f11(self):
        add_hotkey('F11', self.press_f11)

    def get_window_id(self):
        if self.msg_box_active:
            return

        # создаем сообщение с вопросом
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Изменить выбранное окно?")
        msg_box.setText("Вы хотите изменить выбранное окно?")
        yes_button = msg_box.addButton("Да", QMessageBox.YesRole)
        no_button = msg_box.addButton("Нет", QMessageBox.NoRole)

        # устанавливаем флаг активности диалогового окна
        self.msg_box_active = True

        # запускаем сообщение и ждем ответа пользователя
        msg_box.exec_()

        # сбрасываем флаг активности диалогового окна
        self.msg_box_active = False

        # если нажата кнопка "Да", то записываем значение в lineEdit_window_id
        if msg_box.clickedButton() == yes_button:
            x, y = win32api.GetCursorPos()
            coordinate = win32gui.WindowFromPoint((x, y))
            self.lineEdit_window_id.setText(str(coordinate))
            self.label_id_window.setText(str(coordinate))

        elif msg_box.clickedButton() == no_button:
            x, y = win32api.GetCursorPos()
            coordinate = win32gui.WindowFromPoint((x, y))
            self.label_id_window.setText(str(coordinate))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(MainWindow)
    thread = threading.Thread(target=ui.update_hot_time_icon)
    thread.start()
    thread_press_insert = threading.Thread(target=ui.hotkey_thread_insert)
    thread_press_insert.start()
    thread_press_f11 = threading.Thread(target=ui.hotkey_thread_f11)
    thread_press_f11.start()
    MainWindow.show()
    sys.exit(app.exec_())
