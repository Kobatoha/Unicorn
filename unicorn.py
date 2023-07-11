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
from Ui_MainWindow import Ui_MainWindow


class Main(Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_located)
        self.timer.start(5000)


    ### settings file ###
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


    ### functions ###
    def press_f12(self):
        self.pushButton_startstop.click()

    def hotkey_thread_f12(self):
        add_hotkey('F12', self.press_f12)

    def startstop(self):
        if self.pushButton_startstop.text() == 'Start':
            self.pushButton_startstop.setText('Stop')
            self.label_information_actions.setText("Started clicker")
            self.lineEdit_window_id.setDisabled(True)
            self.toggle_1(self.checkBox_1.checkState())
            self.toggle_2(self.checkBox_2.checkState())

        else:
            self.pushButton_startstop.setText('Start')
            self.label_information_actions.setText('Stopped clicker')
            self.lineEdit_window_id.setEnabled(True)
            self.pressed_1 = False
            self.pressed_2 = False

    def profile_load(self):
        self.label_information_actions.setText('Load profile')

    def profile_save(self):
        self.label_information_actions.setText('Save profile')

    def update_hot_time_icon(self):
        while True:
            time_now = datetime.datetime.now().strftime('%H:%M')
            if time_now >= '12:00' and time_now <= '14:00' or time_now >= '19:00' and time_now <= '23:00':
                self.label_hottime.setPixmap(QtGui.QPixmap("../image/icons/hot_time_on.png"))
            else:
                self.label_hottime.setPixmap(QtGui.QPixmap("../image/icons/hot_time_off.png"))
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
            self.keyboard.press('1')
            time.sleep(interval / 1000)
            self.keyboard.release('1')
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
            self.keyboard.press('2')
            time.sleep(interval / 1000)
            self.keyboard.release('2')
            QtCore.QTimer.singleShot(interval, self.press_2)

    def press_f11(self):
        self.pushButton_located.click()

    def hotkey_thread_f11(self):
        add_hotkey('F11', self.press_f11)

    def get_window_id(self):
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
    thread_press_f12 = threading.Thread(target=ui.hotkey_thread_f12)
    thread_press_f12.start()
    thread_press_f11 = threading.Thread(target=ui.hotkey_thread_f11)
    thread_press_f11.start()
    MainWindow.show()
    sys.exit(app.exec_())
