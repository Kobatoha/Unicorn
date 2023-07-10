import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QDrag
from PyQt5.QtCore import QSize, Qt, QMimeData
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

    ### functions ###
    def press_f12(self):
        self.pushButton_startstop.click()

    def hotkey_thread(self):
        add_hotkey('F12', self.press_f12)

    def startstop(self):
        if self.pushButton_startstop.text() == 'Start':
            self.pushButton_startstop.setText('Stop')
            self.label_information_actions.setText("Started clicker")
            self.lineEdit_window_id.setDisabled(True)
            self.toggle_q(self.checkBox_q.checkState())
            self.toggle_w(self.checkBox_w.checkState())

        else:
            self.pushButton_startstop.setText('Start')
            self.label_information_actions.setText('Stopped clicker')
            self.lineEdit_window_id.setEnabled(True)
            self.q_pressed = False
            self.w_pressed = False

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

    def toggle_q(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.q_pressed = True
                self.press_q()
        else:
            self.q_pressed = False


    def press_q(self):
        if self.q_pressed:
            interval = int(self.lineEdit_q.text())
            self.keyboard.press('q')
            time.sleep(interval / 1000)
            self.keyboard.release('q')
            QtCore.QTimer.singleShot(interval, self.press_q)

    def toggle_w(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop':
                self.w_pressed = True
                self.press_w()
        else:
            self.w_pressed = False


    def press_w(self):
        if self.w_pressed:
            interval = int(self.lineEdit_w.text())
            self.keyboard.press('w')
            time.sleep(interval / 1000)
            self.keyboard.release('w')
            QtCore.QTimer.singleShot(interval, self.press_w)

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
    thread_press_f12 = threading.Thread(target=ui.hotkey_thread)
    thread_press_f12.start()
    thread_press_f11 = threading.Thread(target=ui.hotkey_thread_f11)
    thread_press_f11.start()
    MainWindow.show()
    sys.exit(app.exec_())
