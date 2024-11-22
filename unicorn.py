import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QDrag
from PyQt5.QtCore import QSize, Qt, QMimeData, QTimer
import pyautogui
import datetime
import random
from keyboard import add_hotkey
from pynput.keyboard import Key, Controller
import win32gui
import win32api
import win32con
from Ui_MainWindow import Ui_MainWindow
import json
from PyQt5.QtWidgets import QMessageBox
import redss


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
        if 'profile 1' in self.pushButton_save.text():
            settings = {
                'profile': self.lineEdit_profile1.text(),

                'edit_f1': self.lineEdit_f1.text(),
                'edit_f2': self.lineEdit_f2.text(),
                'edit_f3': self.lineEdit_f3.text(),
                'edit_f4': self.lineEdit_f4.text(),
                'edit_f5': self.lineEdit_f5.text(),
                'edit_Q': self.lineEdit_Q.text(),
                'edit_W': self.lineEdit_W.text(),
                'edit_E': self.lineEdit_E.text(),
                'edit_R': self.lineEdit_R.text(),
                'edit_fT': self.lineEdit_T.text(),

                'checkbox_f1': self.checkBox_f1.isChecked(),
                'checkbox_f2': self.checkBox_f2.isChecked(),
                'checkbox_f3': self.checkBox_f3.isChecked(),
                'checkbox_f4': self.checkBox_f4.isChecked(),
                'checkbox_f5': self.checkBox_f5.isChecked(),
                'checkbox_Q': self.checkBox_Q.isChecked(),
                'checkbox_W': self.checkBox_W.isChecked(),
                'checkbox_E': self.checkBox_E.isChecked(),
                'checkbox_R': self.checkBox_R.isChecked(),
                'checkbox_T': self.checkBox_T.isChecked(),

                'edit_1': self.lineEdit_1.text(),
                'edit_2': self.lineEdit_2.text(),
                'edit_3': self.lineEdit_3.text(),
                'edit_4': self.lineEdit_4.text(),
                'edit_5': self.lineEdit_5.text(),
                'edit_6': self.lineEdit_6.text(),
                'edit_7': self.lineEdit_7.text(),
                'edit_8': self.lineEdit_8.text(),
                'edit_9': self.lineEdit_9.text(),
                'edit_tilda': self.lineEdit_tilda.text(),

                'checkbox_1': self.checkBox_1.isChecked(),
                'checkbox_2': self.checkBox_2.isChecked(),
                'checkbox_3': self.checkBox_3.isChecked(),
                'checkbox_4': self.checkBox_4.isChecked(),
                'checkbox_5': self.checkBox_5.isChecked(),
                'checkbox_6': self.checkBox_6.isChecked(),
                'checkbox_7': self.checkBox_7.isChecked(),
                'checkbox_8': self.checkBox_8.isChecked(),
                'checkbox_9': self.checkBox_9.isChecked(),
                'checkbox_tilda': self.checkBox_tilda.isChecked(),
            }
            with open('settings_profile1.json', 'w') as file:
                json.dump(settings, file)
        elif 'profile 2' in self.pushButton_save.text():
            settings = {
                'profile': self.lineEdit_profile2.text(),

                'edit_f1': self.lineEdit_f1.text(),
                'edit_f2': self.lineEdit_f2.text(),
                'edit_f3': self.lineEdit_f3.text(),
                'edit_f4': self.lineEdit_f4.text(),
                'edit_f5': self.lineEdit_f5.text(),
                'edit_Q': self.lineEdit_Q.text(),
                'edit_W': self.lineEdit_W.text(),
                'edit_E': self.lineEdit_E.text(),
                'edit_R': self.lineEdit_R.text(),
                'edit_fT': self.lineEdit_T.text(),

                'checkbox_f1': self.checkBox_f1.isChecked(),
                'checkbox_f2': self.checkBox_f2.isChecked(),
                'checkbox_f3': self.checkBox_f3.isChecked(),
                'checkbox_f4': self.checkBox_f4.isChecked(),
                'checkbox_f5': self.checkBox_f5.isChecked(),
                'checkbox_Q': self.checkBox_Q.isChecked(),
                'checkbox_W': self.checkBox_W.isChecked(),
                'checkbox_E': self.checkBox_E.isChecked(),
                'checkbox_R': self.checkBox_R.isChecked(),
                'checkbox_T': self.checkBox_T.isChecked(),

                'edit_1': self.lineEdit_1.text(),
                'edit_2': self.lineEdit_2.text(),
                'edit_3': self.lineEdit_3.text(),
                'edit_4': self.lineEdit_4.text(),
                'edit_5': self.lineEdit_5.text(),
                'edit_6': self.lineEdit_6.text(),
                'edit_7': self.lineEdit_7.text(),
                'edit_8': self.lineEdit_8.text(),
                'edit_9': self.lineEdit_9.text(),
                'edit_tilda': self.lineEdit_tilda.text(),

                'checkbox_1': self.checkBox_1.isChecked(),
                'checkbox_2': self.checkBox_2.isChecked(),
                'checkbox_3': self.checkBox_3.isChecked(),
                'checkbox_4': self.checkBox_4.isChecked(),
                'checkbox_5': self.checkBox_5.isChecked(),
                'checkbox_6': self.checkBox_6.isChecked(),
                'checkbox_7': self.checkBox_7.isChecked(),
                'checkbox_8': self.checkBox_8.isChecked(),
                'checkbox_9': self.checkBox_9.isChecked(),
                'checkbox_tilda': self.checkBox_tilda.isChecked(),
            }
            with open('settings_profile2.json', 'w') as file:
                json.dump(settings, file)
        elif 'profile 3' in self.pushButton_save.text():
            settings = {
                'profile': self.lineEdit_profile3.text(),

                'edit_f1': self.lineEdit_f1.text(),
                'edit_f2': self.lineEdit_f2.text(),
                'edit_f3': self.lineEdit_f3.text(),
                'edit_f4': self.lineEdit_f4.text(),
                'edit_f5': self.lineEdit_f5.text(),
                'edit_Q': self.lineEdit_Q.text(),
                'edit_W': self.lineEdit_W.text(),
                'edit_E': self.lineEdit_E.text(),
                'edit_R': self.lineEdit_R.text(),
                'edit_fT': self.lineEdit_T.text(),

                'checkbox_f1': self.checkBox_f1.isChecked(),
                'checkbox_f2': self.checkBox_f2.isChecked(),
                'checkbox_f3': self.checkBox_f3.isChecked(),
                'checkbox_f4': self.checkBox_f4.isChecked(),
                'checkbox_f5': self.checkBox_f5.isChecked(),
                'checkbox_Q': self.checkBox_Q.isChecked(),
                'checkbox_W': self.checkBox_W.isChecked(),
                'checkbox_E': self.checkBox_E.isChecked(),
                'checkbox_R': self.checkBox_R.isChecked(),
                'checkbox_T': self.checkBox_T.isChecked(),

                'edit_1': self.lineEdit_1.text(),
                'edit_2': self.lineEdit_2.text(),
                'edit_3': self.lineEdit_3.text(),
                'edit_4': self.lineEdit_4.text(),
                'edit_5': self.lineEdit_5.text(),
                'edit_6': self.lineEdit_6.text(),
                'edit_7': self.lineEdit_7.text(),
                'edit_8': self.lineEdit_8.text(),
                'edit_9': self.lineEdit_9.text(),
                'edit_tilda': self.lineEdit_tilda.text(),

                'checkbox_1': self.checkBox_1.isChecked(),
                'checkbox_2': self.checkBox_2.isChecked(),
                'checkbox_3': self.checkBox_3.isChecked(),
                'checkbox_4': self.checkBox_4.isChecked(),
                'checkbox_5': self.checkBox_5.isChecked(),
                'checkbox_6': self.checkBox_6.isChecked(),
                'checkbox_7': self.checkBox_7.isChecked(),
                'checkbox_8': self.checkBox_8.isChecked(),
                'checkbox_9': self.checkBox_9.isChecked(),
                'checkbox_tilda': self.checkBox_tilda.isChecked(),
            }
            with open('settings_profile3.json', 'w') as file:
                json.dump(settings, file)

    def load_settings(self):
        self.init_profiles_json()
        self.load_profile()
        self.rename_profile()
        try:
            if 'profile 1' in self.pushButton_load.text():
                with open('settings_profile1.json', 'r') as file:
                    settings = json.load(file)

                    self.lineEdit_profile1.setText(settings.get('profile', '')),

                    self.lineEdit_f1.setText(settings.get('edit_f1', '')),
                    self.lineEdit_f2.setText(settings.get('edit_f2', '')),
                    self.lineEdit_f3.setText(settings.get('edit_f3', '')),
                    self.lineEdit_f4.setText(settings.get('edit_f4', '')),
                    self.lineEdit_f5.setText(settings.get('edit_f5', '')),
                    self.lineEdit_Q.setText(settings.get('edit_Q', '')),
                    self.lineEdit_W.setText(settings.get('edit_W', '')),
                    self.lineEdit_E.setText(settings.get('edit_E', '')),
                    self.lineEdit_R.setText(settings.get('edit_R', '')),
                    self.lineEdit_T.setText(settings.get('edit_T', '')),

                    self.checkBox_f1.setChecked(settings.get('checkbox_f1', '')),
                    self.checkBox_f2.setChecked(settings.get('checkbox_f2', '')),
                    self.checkBox_f3.setChecked(settings.get('checkbox_f3', '')),
                    self.checkBox_f4.setChecked(settings.get('checkbox_f4', '')),
                    self.checkBox_f5.setChecked(settings.get('checkbox_f5', '')),
                    self.checkBox_Q.setChecked(settings.get('checkbox_Q', '')),
                    self.checkBox_W.setChecked(settings.get('checkbox_W', '')),
                    self.checkBox_E.setChecked(settings.get('checkbox_E', '')),
                    self.checkBox_R.setChecked(settings.get('checkbox_R', '')),
                    self.checkBox_T.setChecked(settings.get('checkbox_T', '')),

                    self.lineEdit_1.setText(settings.get('edit_1', '')),
                    self.lineEdit_2.setText(settings.get('edit_2', '')),
                    self.lineEdit_3.setText(settings.get('edit_3', '')),
                    self.lineEdit_4.setText(settings.get('edit_4', '')),
                    self.lineEdit_5.setText(settings.get('edit_5', '')),
                    self.lineEdit_6.setText(settings.get('edit_6', '')),
                    self.lineEdit_7.setText(settings.get('edit_7', '')),
                    self.lineEdit_8.setText(settings.get('edit_8', '')),
                    self.lineEdit_9.setText(settings.get('edit_9', '')),
                    self.lineEdit_tilda.setText(settings.get('edit_tilda', '')),

                    self.checkBox_1.setChecked(settings.get('checkbox_1', '')),
                    self.checkBox_2.setChecked(settings.get('checkbox_2', '')),
                    self.checkBox_3.setChecked(settings.get('checkbox_3', '')),
                    self.checkBox_4.setChecked(settings.get('checkbox_4', '')),
                    self.checkBox_5.setChecked(settings.get('checkbox_5', '')),
                    self.checkBox_6.setChecked(settings.get('checkbox_6', '')),
                    self.checkBox_7.setChecked(settings.get('checkbox_7', '')),
                    self.checkBox_8.setChecked(settings.get('checkbox_8', '')),
                    self.checkBox_9.setChecked(settings.get('checkbox_9', '')),
                    self.checkBox_tilda.setChecked(settings.get('checkbox_tilda', ''))
            elif 'profile 2' in self.pushButton_load.text():
                with open('settings_profile2.json', 'r') as file:
                    settings = json.load(file)

                    self.lineEdit_profile2.setText(settings.get('profile', '')),

                    self.lineEdit_f1.setText(settings.get('edit_f1', '')),
                    self.lineEdit_f2.setText(settings.get('edit_f2', '')),
                    self.lineEdit_f3.setText(settings.get('edit_f3', '')),
                    self.lineEdit_f4.setText(settings.get('edit_f4', '')),
                    self.lineEdit_f5.setText(settings.get('edit_f5', '')),
                    self.lineEdit_Q.setText(settings.get('edit_Q', '')),
                    self.lineEdit_W.setText(settings.get('edit_W', '')),
                    self.lineEdit_E.setText(settings.get('edit_E', '')),
                    self.lineEdit_R.setText(settings.get('edit_R', '')),
                    self.lineEdit_T.setText(settings.get('edit_T', '')),

                    self.checkBox_f1.setChecked(settings.get('checkbox_f1', '')),
                    self.checkBox_f2.setChecked(settings.get('checkbox_f2', '')),
                    self.checkBox_f3.setChecked(settings.get('checkbox_f3', '')),
                    self.checkBox_f4.setChecked(settings.get('checkbox_f4', '')),
                    self.checkBox_f5.setChecked(settings.get('checkbox_f5', '')),
                    self.checkBox_Q.setChecked(settings.get('checkbox_Q', '')),
                    self.checkBox_W.setChecked(settings.get('checkbox_W', '')),
                    self.checkBox_E.setChecked(settings.get('checkbox_E', '')),
                    self.checkBox_R.setChecked(settings.get('checkbox_R', '')),
                    self.checkBox_T.setChecked(settings.get('checkbox_T', '')),

                    self.lineEdit_1.setText(settings.get('edit_1', '')),
                    self.lineEdit_2.setText(settings.get('edit_2', '')),
                    self.lineEdit_3.setText(settings.get('edit_3', '')),
                    self.lineEdit_4.setText(settings.get('edit_4', '')),
                    self.lineEdit_5.setText(settings.get('edit_5', '')),
                    self.lineEdit_6.setText(settings.get('edit_6', '')),
                    self.lineEdit_7.setText(settings.get('edit_7', '')),
                    self.lineEdit_8.setText(settings.get('edit_8', '')),
                    self.lineEdit_9.setText(settings.get('edit_9', '')),
                    self.lineEdit_tilda.setText(settings.get('edit_tilda', '')),

                    self.checkBox_1.setChecked(settings.get('checkbox_1', '')),
                    self.checkBox_2.setChecked(settings.get('checkbox_2', '')),
                    self.checkBox_3.setChecked(settings.get('checkbox_3', '')),
                    self.checkBox_4.setChecked(settings.get('checkbox_4', '')),
                    self.checkBox_5.setChecked(settings.get('checkbox_5', '')),
                    self.checkBox_6.setChecked(settings.get('checkbox_6', '')),
                    self.checkBox_7.setChecked(settings.get('checkbox_7', '')),
                    self.checkBox_8.setChecked(settings.get('checkbox_8', '')),
                    self.checkBox_9.setChecked(settings.get('checkbox_9', '')),
                    self.checkBox_tilda.setChecked(settings.get('checkbox_tilda', ''))
            elif 'profile 3' in self.pushButton_load.text():
                with open('settings_profile3.json', 'r') as file:
                    settings = json.load(file)

                    self.lineEdit_profile3.setText(settings.get('profile', '')),

                    self.lineEdit_f1.setText(settings.get('edit_f1', '')),
                    self.lineEdit_f2.setText(settings.get('edit_f2', '')),
                    self.lineEdit_f3.setText(settings.get('edit_f3', '')),
                    self.lineEdit_f4.setText(settings.get('edit_f4', '')),
                    self.lineEdit_f5.setText(settings.get('edit_f5', '')),
                    self.lineEdit_Q.setText(settings.get('edit_Q', '')),
                    self.lineEdit_W.setText(settings.get('edit_W', '')),
                    self.lineEdit_E.setText(settings.get('edit_E', '')),
                    self.lineEdit_R.setText(settings.get('edit_R', '')),
                    self.lineEdit_T.setText(settings.get('edit_T', '')),

                    self.checkBox_f1.setChecked(settings.get('checkbox_f1', '')),
                    self.checkBox_f2.setChecked(settings.get('checkbox_f2', '')),
                    self.checkBox_f3.setChecked(settings.get('checkbox_f3', '')),
                    self.checkBox_f4.setChecked(settings.get('checkbox_f4', '')),
                    self.checkBox_f5.setChecked(settings.get('checkbox_f5', '')),
                    self.checkBox_Q.setChecked(settings.get('checkbox_Q', '')),
                    self.checkBox_W.setChecked(settings.get('checkbox_W', '')),
                    self.checkBox_E.setChecked(settings.get('checkbox_E', '')),
                    self.checkBox_R.setChecked(settings.get('checkbox_R', '')),
                    self.checkBox_T.setChecked(settings.get('checkbox_T', '')),

                    self.lineEdit_1.setText(settings.get('edit_1', '')),
                    self.lineEdit_2.setText(settings.get('edit_2', '')),
                    self.lineEdit_3.setText(settings.get('edit_3', '')),
                    self.lineEdit_4.setText(settings.get('edit_4', '')),
                    self.lineEdit_5.setText(settings.get('edit_5', '')),
                    self.lineEdit_6.setText(settings.get('edit_6', '')),
                    self.lineEdit_7.setText(settings.get('edit_7', '')),
                    self.lineEdit_8.setText(settings.get('edit_8', '')),
                    self.lineEdit_9.setText(settings.get('edit_9', '')),
                    self.lineEdit_tilda.setText(settings.get('edit_tilda', '')),

                    self.checkBox_1.setChecked(settings.get('checkbox_1', '')),
                    self.checkBox_2.setChecked(settings.get('checkbox_2', '')),
                    self.checkBox_3.setChecked(settings.get('checkbox_3', '')),
                    self.checkBox_4.setChecked(settings.get('checkbox_4', '')),
                    self.checkBox_5.setChecked(settings.get('checkbox_5', '')),
                    self.checkBox_6.setChecked(settings.get('checkbox_6', '')),
                    self.checkBox_7.setChecked(settings.get('checkbox_7', '')),
                    self.checkBox_8.setChecked(settings.get('checkbox_8', '')),
                    self.checkBox_9.setChecked(settings.get('checkbox_9', '')),
                    self.checkBox_tilda.setChecked(settings.get('checkbox_tilda', ''))

        except FileNotFoundError:
            pass

    def activate_profile(self):
        if self.pushButton_startstop.text() == 'Stop':
            self.lineEdit_profile1.setDisabled(True)
            self.lineEdit_profile2.setDisabled(True)
            self.lineEdit_profile3.setDisabled(True)
        else:
            self.lineEdit_profile1.setDisabled(False)
            self.lineEdit_profile2.setDisabled(False)
            self.lineEdit_profile3.setDisabled(False)

    def load_profile(self):
        profiles = self.get_profiles()
        for profile in profiles:
            try:
                with open(profiles[profile], 'r') as file:
                    settings = json.load(file)
                    profile.setText(settings.get('profile', ''))
            except:
                pass

    def get_profiles(self):
        profiles = {
            self.lineEdit_profile1: 'settings_profile1.json',
            self.lineEdit_profile2: 'settings_profile2.json',
            self.lineEdit_profile3: 'settings_profile3.json'
        }
        return profiles

    def init_profiles_json(self):
        profiles = self.get_profiles()
        for profile in profiles:
            try:
                with open(profiles[profile], 'r') as file:
                    settings = json.load(file)
                    profile.setText(settings.get('profile', ''))
            except:
                settings = {
                    'profile': profiles[profile].split('.')[0].split('_')[1],

                    'edit_f1': '',
                    'edit_f2': '',
                    'edit_f3': '',
                    'edit_f4': '',
                    'edit_f5': '',
                    'edit_Q': '',
                    'edit_W': '',
                    'edit_E': '',
                    'edit_R': '',
                    'edit_fT': '',

                    'checkbox_f1': False,
                    'checkbox_f2': False,
                    'checkbox_f3': False,
                    'checkbox_f4': False,
                    'checkbox_f5': False,
                    'checkbox_Q': False,
                    'checkbox_W': False,
                    'checkbox_E': False,
                    'checkbox_R': False,
                    'checkbox_T': False,

                    'edit_1': '',
                    'edit_2': '',
                    'edit_3': '',
                    'edit_4': '',
                    'edit_5': '',
                    'edit_6': '',
                    'edit_7': '',
                    'edit_8': '',
                    'edit_9': '',
                    'edit_tilda': '',

                    'checkbox_1': False,
                    'checkbox_2': False,
                    'checkbox_3': False,
                    'checkbox_4': False,
                    'checkbox_5': False,
                    'checkbox_6': False,
                    'checkbox_7': False,
                    'checkbox_8': False,
                    'checkbox_9': False,
                    'checkbox_tilda': False,
                }
                with open(profiles[profile], 'w') as file:
                    json.dump(settings, file)

    def rename_profile(self):
        if self.lineEdit_profile1.text() != '':
            self.pushButton_profile1.setText(self.lineEdit_profile1.text())
        if self.lineEdit_profile2.text() != '':
            self.pushButton_profile2.setText(self.lineEdit_profile2.text())
        if self.lineEdit_profile3.text() != '':
            self.pushButton_profile3.setText(self.lineEdit_profile3.text())

    # functions
    def press_insert(self):
        self.pushButton_startstop.click()

    def hotkey_thread_insert(self):
        def on_insert():
            hwnd = int(self.lineEdit_window_id.text())
            active = redss.check_active_window_insert(hwnd)
            if active:
                self.press_insert()
        add_hotkey('INSERT', on_insert)

    def startstop(self):
        if self.pushButton_startstop.text() == 'Start':
            self.pushButton_startstop.setText('Stop')
            self.tray_icon.setIcon(QtGui.QIcon("images/icon_on.png"))
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
            self.toggle_tilda(self.checkBox_tilda.checkState())
            self.toggle_f1(self.checkBox_f1.checkState())
            self.toggle_f2(self.checkBox_f2.checkState())
            self.toggle_f3(self.checkBox_f3.checkState())
            self.toggle_f4(self.checkBox_f4.checkState())
            self.toggle_f5(self.checkBox_f5.checkState())
            self.toggle_Q(self.checkBox_Q.checkState())
            self.toggle_W(self.checkBox_W.checkState())
            self.toggle_E(self.checkBox_E.checkState())
            self.toggle_R(self.checkBox_R.checkState())
            self.toggle_T(self.checkBox_T.checkState())
            self.toggle_res(self.check_box_res.checkState())
            self.toggle_res_random(self.check_box_res_random.checkState())
            self.toggle_night_teleport(self.checkBox_night_teleport.checkState())
            self.toggle_night_teleport_solo(self.checkBox_night_teleport_solo.checkState())
            self.activate_profile()

        else:
            self.pushButton_startstop.setText('Start')
            self.tray_icon.setIcon(QtGui.QIcon("images/icon_off.png"))
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
            self.pressed_tilda = False
            self.pressed_f1 = False
            self.pressed_f2 = False
            self.pressed_f3 = False
            self.pressed_f4 = False
            self.pressed_f5 = False
            self.pressed_Q = False
            self.pressed_W = False
            self.pressed_E = False
            self.pressed_R = False
            self.pressed_T = False
            self.pressed_res = False
            self.pressed_res_random = False
            self.res_process = False
            self.pressed_night_teleport = False
            self.pressed_night_teleport_solo = False
            self.activate_profile()

    def paused_pressed(self):
        self.pressed_1 = False
        self.pressed_2 = False
        self.pressed_3 = False
        self.pressed_4 = False
        self.pressed_5 = False
        self.pressed_6 = False
        self.pressed_7 = False
        self.pressed_8 = False
        self.pressed_9 = False
        self.pressed_tilda = False
        self.pressed_f1 = False
        self.pressed_f2 = False
        self.pressed_f3 = False
        self.pressed_f4 = False
        self.pressed_f5 = False
        self.pressed_Q = False
        self.pressed_W = False
        self.pressed_E = False
        self.pressed_R = False
        self.pressed_T = False
        self.label_information_actions.setText('Continue clicking')

    def continue_pressed(self):
        self.toggle_1(self.checkBox_1.checkState())
        self.toggle_2(self.checkBox_2.checkState())
        self.toggle_3(self.checkBox_3.checkState())
        self.toggle_4(self.checkBox_4.checkState())
        self.toggle_5(self.checkBox_5.checkState())
        self.toggle_6(self.checkBox_6.checkState())
        self.toggle_7(self.checkBox_7.checkState())
        self.toggle_8(self.checkBox_8.checkState())
        self.toggle_9(self.checkBox_9.checkState())
        self.toggle_tilda(self.checkBox_tilda.checkState())
        self.toggle_f1(self.checkBox_f1.checkState())
        self.toggle_f2(self.checkBox_f2.checkState())
        self.toggle_f3(self.checkBox_f3.checkState())
        self.toggle_f4(self.checkBox_f4.checkState())
        self.toggle_f5(self.checkBox_f5.checkState())
        self.toggle_Q(self.checkBox_Q.checkState())
        self.toggle_W(self.checkBox_W.checkState())
        self.toggle_E(self.checkBox_E.checkState())
        self.toggle_R(self.checkBox_R.checkState())
        self.toggle_T(self.checkBox_T.checkState())
        self.label_information_actions.setText('Paused clicking')

    def profile_load(self):
        self.label_information_actions.setText('Load profile')

    def profile_save(self):
        self.label_information_actions.setText('Save profile')

    def profile1(self):
        self.pushButton_save.setText('save\n profile 1')
        self.pushButton_load.setText('load\n profile 1')
        self.load_settings()

    def profile2(self):
        self.pushButton_save.setText('save\n profile 2')
        self.pushButton_load.setText('load\n profile 2')
        self.load_settings()

    def profile3(self):
        self.pushButton_save.setText('save\n profile 3')
        self.pushButton_load.setText('load\n profile 3')
        self.load_settings()

    def update_hot_time_icon(self):
        while True:
            time_now = datetime.datetime.now().strftime('%H:%M')
            if '12:00' >= time_now <= '14:00' or '19:00' >= time_now <= '23:00':
                self.label_hottime.setPixmap(QtGui.QPixmap("images/hot_time_on.png"))
            else:
                self.label_hottime.setPixmap(QtGui.QPixmap("images/hot_time_off.png"))
            time.sleep(60)

    def update_located(self):
        id = self.label_id_window.text()
        if id in self.lineEdit_window_id.text():
            self.pushButton_located.setIcon(QtGui.QIcon('images/target_on.png'))
            self.label_information_actions.setText('Windows located')
        else:
            self.pushButton_located.setIcon(QtGui.QIcon('images/target_off.png'))

    def toggle_1(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._1_thread:
                self.pressed_1 = True
                self._1_thread = threading.Thread(target=self.press_1, daemon=True)
                self._1_thread.start()
        else:
            self.pressed_1 = False
            if self._1_thread and self._1_thread.is_alive():
                self._1_thread.join()
            self._1_thread = None

    def press_1(self):
        while self.pressed_1:
            interval = int(self.lineEdit_1.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 49, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 49, 0)
            time.sleep(interval / 1000)

        self._1_thread = None

    def toggle_2(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._2_thread:
                self.pressed_2 = True
                self._2_thread = threading.Thread(target=self.press_2, daemon=True)
                self._2_thread.start()
        else:
            self.pressed_2 = False
            if self._2_thread and self._2_thread.is_alive():
                self._2_thread.join()
            self._2_thread = None

    def press_2(self):
        while self.pressed_2:
            interval = int(self.lineEdit_2.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 50, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 50, 0)
            time.sleep(interval / 1000)

        self._2_thread = None

    def toggle_3(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._3_thread:
                self.pressed_3 = True
                self._3_thread = threading.Thread(target=self.press_3, daemon=True)
                self._3_thread.start()
        else:
            self.pressed_3 = False
            if self._3_thread and self._3_thread.is_alive():
                self._3_thread.join()
            self._3_thread = None

    def press_3(self):
        while self.pressed_3:
            interval = int(self.lineEdit_3.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 51, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 51, 0)
            time.sleep(interval / 1000)

        self._3_thread = None

    def toggle_4(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._4_thread:
                self.pressed_4 = True
                self._4_thread = threading.Thread(target=self.press_4, daemon=True)
                self._4_thread.start()
        else:
            self.pressed_4 = False
            if self._4_thread and self._4_thread.is_alive():
                self._4_thread.join()
            self._4_thread = None

    def press_4(self):
        while self.pressed_4:
            interval = int(self.lineEdit_4.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 52, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 52, 0)
            time.sleep(interval / 1000)

        self._4_thread = None

    def toggle_5(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._5_thread:
                self.pressed_5 = True
                self._5_thread = threading.Thread(target=self.press_5, daemon=True)
                self._5_thread.start()
        else:
            self.pressed_5 = False
            if self._5_thread and self._5_thread.is_alive():
                self._5_thread.join()
            self._5_thread = None

    def press_5(self):
        while self.pressed_5:
            interval = int(self.lineEdit_5.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 53, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 53, 0)
            time.sleep(interval / 1000)

        self._5_thread = None

    def toggle_6(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._6_thread:
                self.pressed_6 = True
                self._6_thread = threading.Thread(target=self.press_6, daemon=True)
                self._6_thread.start()
        else:
            self.pressed_6 = False
            if self._6_thread and self._6_thread.is_alive():
                self._6_thread.join()
            self._6_thread = None

    def press_6(self):
        while self.pressed_6:
            interval = int(self.lineEdit_6.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 54, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 54, 0)
            time.sleep(interval / 1000)

        self._6_thread = None

    def toggle_7(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._7_thread:
                self.pressed_7 = True
                self._7_thread = threading.Thread(target=self.press_7, daemon=True)
                self._7_thread.start()
        else:
            self.pressed_7 = False
            if self._7_thread and self._7_thread.is_alive():
                self._7_thread.join()
            self._7_thread = None

    def press_7(self):
        while self.pressed_7:
            interval = int(self.lineEdit_7.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 55, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 55, 0)
            time.sleep(interval / 1000)

        self._7_thread = None

    def toggle_8(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._8_thread:
                self.pressed_8 = True
                self._8_thread = threading.Thread(target=self.press_8, daemon=True)
                self._8_thread.start()
        else:
            self.pressed_8 = False
            if self._8_thread and self._8_thread.is_alive():
                self._8_thread.join()
            self._8_thread = None

    def press_8(self):
        while self.pressed_8:
            interval = int(self.lineEdit_8.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 56, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 56, 0)
            time.sleep(interval / 1000)

        self._8_thread = None

    def toggle_9(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._9_thread:
                self.pressed_9 = True
                self._9_thread = threading.Thread(target=self.press_9, daemon=True)
                self._9_thread.start()
        else:
            self.pressed_9 = False
            if self._9_thread and self._9_thread.is_alive():
                self._9_thread.join()
            self._9_thread = None

    def press_9(self):
        while self.pressed_9:
            interval = int(self.lineEdit_9.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 57, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 57, 0)
            time.sleep(interval / 1000)

        self._9_thread = None

    def toggle_tilda(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._tilda_thread:
                self.pressed_tilda = True
                self._tilda_thread = threading.Thread(target=self.press_tilda, daemon=True)
                self._tilda_thread.start()
        else:
            self.pressed_tilda = False
            if self._tilda_thread and self._tilda_thread.is_alive():
                self._tilda_thread.join()
            self._tilda_thread = None

    def press_tilda(self):
        while self.pressed_tilda:
            interval = int(self.lineEdit_tilda.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 192, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 192, 0)
            time.sleep(interval / 1000)

        self._tilda_thread = None

    def toggle_f1(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._f1_thread:
                self.pressed_f1 = True
                self._f1_thread = threading.Thread(target=self.press_f1, daemon=True)
                self._f1_thread.start()
        else:
            self.pressed_f1 = False
            if self._f1_thread and self._f1_thread.is_alive():
                self._f1_thread.join()
            self._f1_thread = None

    def press_f1(self):
        while self.pressed_f1:
            interval = int(self.lineEdit_f1.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F1, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F1, 0)
            time.sleep(interval / 1000)

        self._f1_thread = None

    def toggle_f2(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._f2_thread:
                self.pressed_f2 = True
                self._f2_thread = threading.Thread(target=self.press_f2, daemon=True)
                self._f2_thread.start()
        else:
            self.pressed_f2 = False
            if self._f2_thread and self._f2_thread.is_alive():
                self._f2_thread.join()
            self._f2_thread = None

    def press_f2(self):
        while self.pressed_f2:
            interval = int(self.lineEdit_f2.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F2, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F2, 0)
            time.sleep(interval / 1000)

        self._f2_thread = None

    def toggle_f3(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._f3_thread:
                self.pressed_f3 = True
                self._f3_thread = threading.Thread(target=self.press_f3, daemon=True)
                self._f3_thread.start()
        else:
            self.pressed_f3 = False
            if self._f3_thread and self._f3_thread.is_alive():
                self._f3_thread.join()
            self._f3_thread = None

    def press_f3(self):
        while self.pressed_f3:
            interval = int(self.lineEdit_f3.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F3, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F3, 0)
            time.sleep(interval / 1000)

        self._f3_thread = None

    def toggle_f4(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._f4_thread:
                self.pressed_f4 = True
                self._f4_thread = threading.Thread(target=self.press_f4, daemon=True)
                self._f4_thread.start()
        else:
            self.pressed_f4 = False
            if self._f4_thread and self._f4_thread.is_alive():
                self._f4_thread.join()
            self._f4_thread = None

    def press_f4(self):
        while self.pressed_f4:
            interval = int(self.lineEdit_f4.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F4, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F4, 0)
            time.sleep(interval / 1000)

        self._f4_thread = None

    def toggle_f5(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._f5_thread:
                self.pressed_f5 = True
                self._f5_thread = threading.Thread(target=self.press_f5, daemon=True)
                self._f5_thread.start()
        else:
            self.pressed_f5 = False
            if self._f5_thread and self._f5_thread.is_alive():
                self._f5_thread.join()
            self._f5_thread = None

    def press_f5(self):
        while self.pressed_f5:
            interval = int(self.lineEdit_f5.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_F5, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F5, 0)
            time.sleep(interval / 1000)

        self._f5_thread = None

    def toggle_Q(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._Q_thread:
                self.pressed_Q = True
                self._Q_thread = threading.Thread(target=self.press_Q, daemon=True)
                self._Q_thread.start()
        else:
            self.pressed_Q = False
            if self._Q_thread and self._Q_thread.is_alive():
                self._Q_thread.join()
            self._Q_thread = None

    def press_Q(self):
        while self.pressed_Q:
            interval = int(self.lineEdit_Q.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 81, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 81, 0)
            time.sleep(interval / 1000)

        self._Q_thread = None

    def toggle_W(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._W_thread:
                self.pressed_W = True
                self._W_thread = threading.Thread(target=self.press_W, daemon=True)
                self._W_thread.start()
        else:
            self.pressed_W = False
            if self._W_thread and self._W_thread.is_alive():
                self._W_thread.join()
            self._W_thread = None

    def press_W(self):
        while self.pressed_W:
            interval = int(self.lineEdit_W.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 87, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 87, 0)
            time.sleep(interval / 1000)

        self._W_thread = None

    def toggle_E(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._E_thread:
                self.pressed_E = True
                # self.press_E()
                self._E_thread = threading.Thread(target=self.press_E, daemon=True)
                self._E_thread.start()
        else:
            self.pressed_E = False
            if self._E_thread and self._E_thread.is_alive():
                self._E_thread.join()
            self._E_thread = None

    def press_E(self):
        while self.pressed_E:
            interval = int(self.lineEdit_E.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 69, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 69, 0)
            time.sleep(interval / 1000)

        self._E_thread = None

    def toggle_R(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._R_thread:
                self.pressed_R = True
                self._R_thread = threading.Thread(target=self.press_R, daemon=True)
                self._R_thread.start()
        else:
            self.pressed_R = False
            if self._R_thread and self._R_thread.is_alive():
                self._R_thread.join()
            self._R_thread = None

    def press_R(self):
        while self.pressed_R:
            interval = int(self.lineEdit_R.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 82, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 82, 0)
            time.sleep(interval / 1000)

        self._R_thread = None

    def toggle_T(self, state):
        if state == QtCore.Qt.Checked:
            if self.pushButton_startstop.text() == 'Stop' and not self._T_thread:
                self.pressed_T = True
                # self.press_T()
                self._T_thread = threading.Thread(target=self.press_T, daemon=True)
                self._T_thread.start()
        else:
            self.pressed_T = False
            if self._T_thread and self._T_thread.is_alive():
                self._T_thread.join()
            self._T_thread = None

    def press_T(self):
        while self.pressed_T:
            interval = int(self.lineEdit_T.text())
            hwnd = self.lineEdit_window_id.text()

            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, 84, 0)
            time.sleep(interval / 1000)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, 84, 0)
            time.sleep(interval / 1000)

        self._T_thread = None

    def toggle_res(self, state):
        if state == QtCore.Qt.Checked:
            print('toggle_res activated')
            self.check_box_res_random.setDisabled(True)
            if self.pushButton_startstop.text() == 'Stop' and not self._res_thread:
                self.pressed_res = True
                self._res_thread = threading.Thread(target=self.press_res, daemon=True)
                self._res_thread.start()
        else:
            self.check_box_res_random.setDisabled(False)
            self.pressed_res = False
            if self._res_thread and self._res_thread.is_alive():
                self._res_thread.join()
            self._res_thread = None
            self.label_res.setText("")

    def press_res(self):
        time.sleep(10)
        while self.pressed_res:
            try:
                hwnd = int(self.lineEdit_window_id.text())
                flag = redss.check_health_bar(hwnd)
                if flag:
                    self.res_process = True
                if flag and self.pressed_res:
                    redss.check_active_window(hwnd)
                    time.sleep(5)
                    rect_recovery_free_exp = redss.get_window_free_up(hwnd)
                    rect_recovery_agree = redss.get_window_free_agree(hwnd)
                    rect_recovery_pay_exp = redss.get_window_pay_agree(hwnd)
                    if self.pressed_res:
                        redss.send_left_click_pyautogui(hwnd, rect_recovery_free_exp[0], rect_recovery_free_exp[1])
                        time.sleep(2)
                        death = False
                        if self.pressed_res:
                            redss.send_left_click_pyautogui(hwnd, rect_recovery_agree[0], rect_recovery_agree[1])
                            time.sleep(1)
                            death = False
                            if self.pressed_res:
                                redss.send_left_click_pyautogui(hwnd, rect_recovery_pay_exp[0], rect_recovery_pay_exp[1])
                                time.sleep(5)
                                death = True
                    else:
                        break
                else:
                    death = False
                    self.res_process = False
                if death:
                    self.paused_pressed()
                    time.sleep(120)
                    if self.pressed_res:
                        redss.use_teleport(hwnd)
                        time.sleep(2)
                        self.continue_pressed()
                        self.res_process = False
                    else:
                        self.res_process = False
                        break

                respawn = random.randint(30000, 120000)
                total_seconds = respawn / 1000
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                print(datetime.datetime.now().strftime('%H:%M:%S'), f'Проверка через: {minutes} min. и {seconds} sec.')
                next_check = datetime.datetime.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
                self.label_information_actions.setText(f'Next check HP: {minutes} min. and {seconds} sec.')
                self.label_res.setText(f'Next: {next_check.strftime('%M:%S')}')

                for _ in range(int(total_seconds)):
                    if not self.pressed_res:
                        self.label_res.setText('')
                        break
                    time.sleep(1)
            except Exception as e:
                print(f'Произошла ошибка воскрешения, ждем 10 секунд для повтора: {e}')
                time.sleep(10)

        self._res_thread = None

    def toggle_res_random(self, state):
        if state == QtCore.Qt.Checked:
            print('toggle_res_random activated')
            self.check_box_res.setDisabled(True)
            if self.pushButton_startstop.text() == 'Stop' and not self._res_random_thread:
                self.pressed_res_random = True
                self._res_random_thread = threading.Thread(target=self.press_res_random, daemon=True)
                self._res_random_thread.start()
        else:
            self.check_box_res.setDisabled(False)
            self.pressed_res_random = False
            if self._res_random_thread and self._res_random_thread.is_alive():
                self._res_random_thread.join()
            self._res_random_thread = None
            self.label_res_random.setText("")

    def press_res_random(self):
        time.sleep(10)
        while self.pressed_res_random:
            try:
                hwnd = int(self.lineEdit_window_id.text())
                flag = redss.check_health_bar(hwnd)
                if flag:
                    self.res_process = True
                if flag and self.pressed_res_random:
                    redss.check_active_window(hwnd)
                    time.sleep(5)
                    rect_recovery_free_exp = redss.get_window_free_up(hwnd)
                    rect_recovery_agree = redss.get_window_free_agree(hwnd)
                    rect_recovery_pay_exp = redss.get_window_pay_agree(hwnd)
                    if self.pressed_res_random:
                        redss.send_left_click_pyautogui(hwnd, rect_recovery_free_exp[0], rect_recovery_free_exp[1])
                        time.sleep(2)
                        death = False
                        if self.pressed_res_random:
                            redss.send_left_click_pyautogui(hwnd, rect_recovery_agree[0], rect_recovery_agree[1])
                            time.sleep(1)
                            death = False
                            if self.pressed_res_random:
                                redss.send_left_click_pyautogui(hwnd, rect_recovery_pay_exp[0], rect_recovery_pay_exp[1])
                                time.sleep(5)
                                death = True
                    else:
                        break
                else:
                    death = False
                    self.res_process = False
                if death:
                    self.paused_pressed()
                    time.sleep(120)
                    if self.pressed_res_random:
                        redss.use_teleport_random(hwnd)
                        time.sleep(2)
                        self.continue_pressed()
                        self.res_process = False
                    else:
                        self.res_process = False
                        break

                self.res_process = False
                respawn = random.randint(30000, 120000)
                total_seconds = respawn / 1000
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                print(datetime.datetime.now().strftime('%H:%M:%S'), f'Проверка через: {minutes} min. и {seconds} sec.')
                next_check = datetime.datetime.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
                self.label_information_actions.setText(f'Next check HP: {minutes} min. and {seconds} sec.')
                self.label_res_random.setText(f'Next: {next_check.strftime('%M:%S')}')

                for _ in range(int(total_seconds)):
                    if not self.pressed_res_random:
                        self.label_res_random.setText('')
                        break
                    time.sleep(1)
            except Exception as e:
                print(f'Произошла ошибка воскрешения, ждем 10 секунд для повтора: {e}')
                time.sleep(10)

        self._res_random_thread = None

    def toggle_night_teleport(self, state):
        if state == QtCore.Qt.Checked:
            print('toggle_night_teleport activated')
            self.checkBox_night_teleport_solo.setDisabled(True)
            if self.pushButton_startstop.text() == 'Stop' and not self._night_teleport_thread:
                self.pressed_night_teleport = True
                self._night_teleport_thread = threading.Thread(target=self.press_night_teleport, daemon=True)
                self._night_teleport_thread.start()
        else:
            self.checkBox_night_teleport_solo.setDisabled(False)
            self.pressed_night_teleport = False
            if self._night_teleport_thread and self._night_teleport_thread.is_alive():
                self._night_teleport_thread.join()
            self._night_teleport_thread = None
            self.label_night_teleport.setText("")

    def press_night_teleport(self):
        respawn = 720000
        total_seconds = respawn / 1000
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        print(datetime.datetime.now().strftime('%H:%M:%S'), f'Проверка через: {minutes} min. и {seconds} sec.')
        next_check = datetime.datetime.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
        self.label_information_actions.setText(f'Next check HP: {minutes} min. and {seconds} sec.')
        self.label_night_teleport.setText(f'Next: {next_check.strftime('%M:%S')}')
        for _ in range(int(total_seconds)):
            if not self.pressed_night_teleport:
                self.label_night_teleport.setText('')
                break
            time.sleep(1)
        while self.pressed_night_teleport:
            try:
                if not self.res_process:
                    self.paused_pressed()
                    hwnd = int(self.lineEdit_window_id.text())
                    time.sleep(1)
                    redss.use_teleport_random(hwnd)
                    time.sleep(1)
                    self.continue_pressed()

                respawn = 720000
                total_seconds = respawn / 1000
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                print(datetime.datetime.now().strftime('%H:%M:%S'), f'Проверка через: {minutes} min. и {seconds} sec.')
                next_check = datetime.datetime.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
                self.label_information_actions.setText(f'Next check HP: {minutes} min. and {seconds} sec.')
                self.label_night_teleport.setText(f'Next: {next_check.strftime('%M:%S')}')

                for _ in range(int(total_seconds)):
                    if not self.pressed_night_teleport:
                        self.label_night_teleport.setText('')
                        break
                    time.sleep(1)
            except Exception as e:
                print(f'Произошла ошибка воскрешения, ждем 10 секунд для повтора: {e}')
                time.sleep(10)

        self._night_teleport_thread = None

    def toggle_night_teleport_solo(self, state):
        if state == QtCore.Qt.Checked:
            print('toggle_night_teleport_solo activated')
            self.checkBox_night_teleport.setDisabled(True)
            if self.pushButton_startstop.text() == 'Stop' and not self._night_teleport_solo_thread:
                self.pressed_night_teleport_solo = True
                self._night_teleport_solo_thread = threading.Thread(target=self.press_night_teleport_solo, daemon=True)
                self._night_teleport_solo_thread.start()
        else:
            self.checkBox_night_teleport.setDisabled(False)
            self.pressed_night_teleport_solo = False
            if self._night_teleport_solo_thread and self._night_teleport_solo_thread.is_alive():
                self._night_teleport_solo_thread.join()
            self._night_teleport_solo_thread = None
            self.label_night_teleport_solo.setText("")

    def press_night_teleport_solo(self):
        respawn = 720000
        total_seconds = respawn / 1000
        minutes = int(total_seconds // 60)
        seconds = int(total_seconds % 60)
        print(datetime.datetime.now().strftime('%H:%M:%S'), f'Проверка через: {minutes} min. и {seconds} sec.')
        next_check = datetime.datetime.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
        self.label_information_actions.setText(f'Next check HP: {minutes} min. and {seconds} sec.')
        self.label_night_teleport_solo.setText(f'Next: {next_check.strftime('%M:%S')}')
        for _ in range(int(total_seconds)):
            if not self.pressed_night_teleport_solo:
                self.label_night_teleport_solo.setText('')
                break
            time.sleep(1)
        while self.pressed_night_teleport_solo:
            try:
                if not self.res_process:
                    self.paused_pressed()
                    hwnd = int(self.lineEdit_window_id.text())
                    time.sleep(1)
                    redss.use_teleport(hwnd)
                    time.sleep(1)
                    self.continue_pressed()

                respawn = 720000
                total_seconds = respawn / 1000
                minutes = int(total_seconds // 60)
                seconds = int(total_seconds % 60)
                print(datetime.datetime.now().strftime('%H:%M:%S'), f'Проверка через: {minutes} min. и {seconds} sec.')
                next_check = datetime.datetime.now() + datetime.timedelta(minutes=minutes, seconds=seconds)
                self.label_information_actions.setText(f'Next check HP: {minutes} min. and {seconds} sec.')
                self.label_night_teleport_solo.setText(f'Next: {next_check.strftime('%M:%S')}')

                for _ in range(int(total_seconds)):
                    if not self.pressed_night_teleport_solo:
                        self.label_night_teleport_solo.setText('')
                        break
                    time.sleep(1)
            except Exception as e:
                print(f'Произошла ошибка воскрешения, ждем 10 секунд для повтора: {e}')
                time.sleep(10)

        self._night_teleport_solo_thread = None

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
    try:
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Main()
        ui.setupUi(MainWindow)
        thread = threading.Thread(target=ui.update_hot_time_icon)
        thread.start()
        thread_press_insert = threading.Thread(target=ui.hotkey_thread_insert, daemon=True)
        thread_press_insert.start()
        # thread_press_f11 = threading.Thread(target=ui.hotkey_thread_f11)
        # thread_press_f11.start()
        MainWindow.show()
        sys.exit(app.exec_())
    except:
        print('error name-main')
