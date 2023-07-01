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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Unicorn")
        MainWindow.resize(300, 600)
        MainWindow.setMinimumSize(QtCore.QSize(165, 600))
        MainWindow.setMaximumSize(QtCore.QSize(300, 600))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ### --------------------- ###
        ###   Turning Keys BLOCK  ###
        ### --------------------- ###
        ### turning keys ###
        self.label_tuning_keys = QtWidgets.QLabel(self.centralwidget)
        self.label_tuning_keys.setGeometry(QtCore.QRect(10, 0, 61, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_tuning_keys.setFont(font)
        self.label_tuning_keys.setObjectName("label_tuning_keys")
        self.label_tuning_keys.setText("Tuning keys")

        self.line_tuning_keys_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_tuning_keys_1.setGeometry(QtCore.QRect(69, 0, 81, 20))
        self.line_tuning_keys_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_tuning_keys_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_tuning_keys_1.setObjectName("line_tuning_keys_1")

        self.line_tuning_keys_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_tuning_keys_2.setGeometry(QtCore.QRect(170, 0, 111, 20))
        self.line_tuning_keys_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_tuning_keys_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_tuning_keys_2.setObjectName("line_tuning_keys_2")

        self.line_half_window = QtWidgets.QFrame(self.centralwidget)
        self.line_half_window.setGeometry(QtCore.QRect(150, 20, 20, 350))
        self.line_half_window.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_half_window.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_half_window.setObjectName("line_half_window")

        ### --------------------- ###
        ### LineEdit F1-F12 BLOCK ###
        ### --------------------- ###
        self.lineEdit_f1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f1.setGeometry(QtCore.QRect(30, 20, 60, 20))
        self.lineEdit_f1.setObjectName("lineEdit_f1")

        self.lineEdit_f2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f2.setGeometry(QtCore.QRect(30, 50, 60, 20))
        self.lineEdit_f2.setObjectName("lineEdit_f2")

        self.lineEdit_f3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f3.setGeometry(QtCore.QRect(30, 80, 60, 20))
        self.lineEdit_f3.setObjectName("lineEdit_f3")

        self.lineEdit_f4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f4.setGeometry(QtCore.QRect(30, 110, 60, 20))
        self.lineEdit_f4.setObjectName("lineEdit_f4")

        self.lineEdit_f5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f5.setGeometry(QtCore.QRect(30, 140, 60, 20))
        self.lineEdit_f5.setObjectName("lineEdit_f5")

        self.lineEdit_f6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f6.setGeometry(QtCore.QRect(30, 170, 60, 20))
        self.lineEdit_f6.setObjectName("lineEdit_f6")

        self.lineEdit_f7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f7.setGeometry(QtCore.QRect(30, 200, 60, 20))
        self.lineEdit_f7.setObjectName("lineEdit_f7")

        self.lineEdit_f8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f8.setGeometry(QtCore.QRect(30, 230, 60, 20))
        self.lineEdit_f8.setObjectName("lineEdit_f8")

        self.lineEdit_f9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f9.setGeometry(QtCore.QRect(30, 260, 60, 20))
        self.lineEdit_f9.setObjectName("lineEdit_f9")

        self.lineEdit_f10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f10.setGeometry(QtCore.QRect(30, 290, 60, 20))
        self.lineEdit_f10.setObjectName("lineEdit_f10")

        self.lineEdit_f11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f11.setGeometry(QtCore.QRect(30, 320, 60, 20))
        self.lineEdit_f11.setObjectName("lineEdit_f11")

        ### --------------------- ###
        ### CheckBox F1-F12 BLOCK ###
        ### --------------------- ###
        self.checkBox_f1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f1.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.checkBox_f1.setText("F1")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f1.setFont(font)
        self.checkBox_f1.setObjectName("checkBox_f1")

        self.checkBox_f2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f2.setGeometry(QtCore.QRect(100, 50, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f2.setFont(font)
        self.checkBox_f2.setObjectName("checkBox_f2")
        self.checkBox_f2.setText("F2")

        self.checkBox_f3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f3.setGeometry(QtCore.QRect(100, 80, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f3.setFont(font)
        self.checkBox_f3.setObjectName("checkBox_f3")
        self.checkBox_f3.setText("F3")

        self.checkBox_f4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f4.setGeometry(QtCore.QRect(100, 110, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f4.setFont(font)
        self.checkBox_f4.setObjectName("checkBox_f4")
        self.checkBox_f4.setText("F4")

        self.checkBox_f5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f5.setGeometry(QtCore.QRect(100, 140, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f5.setFont(font)
        self.checkBox_f5.setObjectName("checkBox_f5")
        self.checkBox_f5.setText("F5")

        self.checkBox_f6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f6.setGeometry(QtCore.QRect(100, 170, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f6.setFont(font)
        self.checkBox_f6.setObjectName("checkBox_f6")
        self.checkBox_f6.setText("F6")

        self.checkBox_f7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f7.setGeometry(QtCore.QRect(100, 200, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f7.setFont(font)
        self.checkBox_f7.setObjectName("checkBox_f7")
        self.checkBox_f7.setText("F7")

        self.checkBox_f8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f8.setGeometry(QtCore.QRect(100, 230, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f8.setFont(font)
        self.checkBox_f8.setObjectName("checkBox_f8")
        self.checkBox_f8.setText("F8")

        self.checkBox_f9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f9.setGeometry(QtCore.QRect(100, 260, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f9.setFont(font)
        self.checkBox_f9.setObjectName("checkBox_f9")
        self.checkBox_f9.setText("F9")

        self.checkBox_f10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f10.setGeometry(QtCore.QRect(100, 290, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f10.setFont(font)
        self.checkBox_f10.setObjectName("checkBox_f10")
        self.checkBox_f10.setText("F10")

        self.checkBox_f11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f11.setGeometry(QtCore.QRect(100, 320, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f11.setFont(font)
        self.checkBox_f11.setObjectName("checkBox_f11")
        self.checkBox_f11.setText("F11")


        ### --------------------- ###
        ###   CheckBox Q-V BLOCK  ###
        ### --------------------- ###
        self.checkBox_q = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_q.setGeometry(QtCore.QRect(250, 20, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_q.setFont(font)
        self.checkBox_q.setObjectName("checkBox_q")
        self.checkBox_q.setText("Q")
        self.checkBox_q.stateChanged.connect(self.toggle_q)
        self.keyboard = Controller()
        self.q_pressed = False

        self.checkBox_w = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_w.setGeometry(QtCore.QRect(250, 50, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_w.setFont(font)
        self.checkBox_w.setObjectName("checkBox_w")
        self.checkBox_w.setText("W")
        self.checkBox_w.stateChanged.connect(self.toggle_w)
        self.keyboard = Controller()
        self.w_pressed = False

        self.checkBox_e = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_e.setGeometry(QtCore.QRect(250, 80, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_e.setFont(font)
        self.checkBox_e.setObjectName("checkBox_e")
        self.checkBox_e.setText("E")

        self.checkBox_r = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_r.setGeometry(QtCore.QRect(250, 110, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_r.setFont(font)
        self.checkBox_r.setObjectName("checkBox_r")
        self.checkBox_r.setText("R")

        self.checkBox_a = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_a.setGeometry(QtCore.QRect(250, 140, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_a.setFont(font)
        self.checkBox_a.setObjectName("checkBox_a")
        self.checkBox_a.setText("A")

        self.checkBox_s = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_s.setGeometry(QtCore.QRect(250, 170, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_s.setFont(font)
        self.checkBox_s.setObjectName("checkBox_s")
        self.checkBox_s.setText("S")

        self.checkBox_d = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_d.setGeometry(QtCore.QRect(250, 200, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_d.setFont(font)
        self.checkBox_d.setObjectName("checkBox_d")
        self.checkBox_d.setText("D")

        self.checkBox_f = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f.setGeometry(QtCore.QRect(250, 230, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f.setFont(font)
        self.checkBox_f.setObjectName("checkBox_f")
        self.checkBox_f.setText("F")

        self.checkBox_z = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_z.setGeometry(QtCore.QRect(250, 260, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_z.setFont(font)
        self.checkBox_z.setObjectName("checkBox_z")
        self.checkBox_z.setText("Z")

        self.checkBox_x = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_x.setGeometry(QtCore.QRect(250, 290, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_x.setFont(font)
        self.checkBox_x.setObjectName("checkBox_x")
        self.checkBox_x.setText("X")

        self.checkBox_c = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_c.setGeometry(QtCore.QRect(250, 320, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_c.setFont(font)
        self.checkBox_c.setObjectName("checkBox_c")
        self.checkBox_c.setText("C")

        self.checkBox_v = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_v.setGeometry(QtCore.QRect(250, 350, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_v.setFont(font)
        self.checkBox_v.setObjectName("checkBox_v")
        self.checkBox_v.setText("V")

        ### --------------------- ###
        ###   LineEdit Q-V BLOCK  ###
        ### --------------------- ###
        self.lineEdit_q = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_q.setGeometry(QtCore.QRect(180, 20, 60, 20))
        self.lineEdit_q.setObjectName("lineEdit_q")
        self.lineEdit_q.setText('333')

        self.lineEdit_w = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_w.setGeometry(QtCore.QRect(180, 50, 60, 20))
        self.lineEdit_w.setObjectName("lineEdit_w")
        self.lineEdit_w.setText('333')

        self.lineEdit_e = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_e.setGeometry(QtCore.QRect(180, 80, 60, 20))
        self.lineEdit_e.setObjectName("lineEdit_e")
        self.lineEdit_e.setText('333')

        self.lineEdit_r = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_r.setGeometry(QtCore.QRect(180, 110, 60, 20))
        self.lineEdit_r.setObjectName("lineEdit_r")
        self.lineEdit_r.setText('333')

        self.lineEdit_a = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_a.setGeometry(QtCore.QRect(180, 140, 60, 20))
        self.lineEdit_a.setObjectName("lineEdit_a")
        self.lineEdit_a.setText('333')

        self.lineEdit_s = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_s.setGeometry(QtCore.QRect(180, 170, 60, 20))
        self.lineEdit_s.setObjectName("lineEdit_s")
        self.lineEdit_s.setText('333')

        self.lineEdit_d = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_d.setGeometry(QtCore.QRect(180, 200, 60, 20))
        self.lineEdit_d.setObjectName("lineEdit_d")
        self.lineEdit_d.setText('333')

        self.lineEdit_f = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f.setGeometry(QtCore.QRect(180, 230, 60, 20))
        self.lineEdit_f.setObjectName("lineEdit_f")
        self.lineEdit_f.setText('333')

        self.lineEdit_z = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_z.setGeometry(QtCore.QRect(180, 260, 60, 20))
        self.lineEdit_z.setObjectName("lineEdit_z")
        self.lineEdit_z.setText('333')

        self.lineEdit_x = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x.setGeometry(QtCore.QRect(180, 290, 60, 20))
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.lineEdit_x.setText('333')

        self.lineEdit_c = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_c.setGeometry(QtCore.QRect(180, 320, 60, 20))
        self.lineEdit_c.setObjectName("lineEdit_c")
        self.lineEdit_c.setText('333')

        self.lineEdit_v = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_v.setGeometry(QtCore.QRect(180, 350, 60, 20))
        self.lineEdit_v.setObjectName("lineEdit_v")
        self.lineEdit_v.setText('333')

        ### --------------------- ###
        ###      ICONS BLOCK      ###
        ### --------------------- ###
        ### icons ###
        self.label_icons = QtWidgets.QLabel(self.centralwidget)
        self.label_icons.setGeometry(QtCore.QRect(10, 370, 41, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_icons.setFont(font)
        self.label_icons.setAlignment(QtCore.Qt.AlignCenter)
        self.label_icons.setObjectName("label_icons")
        self.label_icons.setText("Icons")

        self.line_icons_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_icons_1.setGeometry(QtCore.QRect(50, 370, 101, 20))
        self.line_icons_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_icons_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_icons_1.setObjectName("line_icons_1")

        self.line_icons_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_icons_2.setGeometry(QtCore.QRect(170, 370, 111, 20))
        self.line_icons_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_icons_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_icons_2.setObjectName("line_icons_2")

        ### hot time ###
        self.label_hottime = QtWidgets.QLabel(self.centralwidget)
        self.label_hottime.setGeometry(QtCore.QRect(20, 400, 31, 31))
        self.label_hottime.setPixmap(QtGui.QPixmap("../image/icons/hot_time_off.png"))
        self.label_hottime.setScaledContents(True)
        self.label_hottime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hottime.setObjectName("label_hottime")

        self.label_hottime_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_hottime_2.setGeometry(QtCore.QRect(10, 430, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_hottime_2.setFont(font)
        self.label_hottime_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hottime_2.setObjectName("label_hottime_2")
        self.label_hottime_2.setText("Hot Time")



        ### lamps ###
        self.label_lamps = QtWidgets.QLabel(self.centralwidget)
        self.label_lamps.setGeometry(QtCore.QRect(70, 400, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_lamps.setFont(font)
        self.label_lamps.setPixmap(QtGui.QPixmap("../image/icons/lamps_on.png"))
        self.label_lamps.setScaledContents(True)
        self.label_lamps.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lamps.setObjectName("label_lamps")

        self.label_lamps_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_lamps_2.setGeometry(QtCore.QRect(60, 430, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_lamps_2.setFont(font)
        self.label_lamps_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lamps_2.setObjectName("label_lamps_2")
        self.label_lamps_2.setText("Lamps")

        ### sayha ###
        self.label_sayha = QtWidgets.QLabel(self.centralwidget)
        self.label_sayha.setGeometry(QtCore.QRect(120, 400, 31, 31))
        self.label_sayha.setText("")
        self.label_sayha.setPixmap(QtGui.QPixmap("../image/icons/sayha_on.png"))
        self.label_sayha.setScaledContents(True)
        self.label_sayha.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sayha.setObjectName("label_sayha")

        self.label_sayha_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sayha_2.setGeometry(QtCore.QRect(110, 430, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_sayha_2.setFont(font)
        self.label_sayha_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sayha_2.setObjectName("label_sayha_2")
        self.label_sayha_2.setText("Sayha")

        ### --------------------- ###
        ###      Window BLOCK     ###
        ### --------------------- ###
        ### window ###
        self.label_window = QtWidgets.QLabel(self.centralwidget)
        self.label_window.setGeometry(QtCore.QRect(10, 470, 51, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_window.setFont(font)
        self.label_window.setAlignment(QtCore.Qt.AlignCenter)
        self.label_window.setObjectName("label_window")
        self.label_window.setText("Window")

        self.line_window = QtWidgets.QFrame(self.centralwidget)
        self.line_window.setGeometry(QtCore.QRect(60, 470, 91, 20))
        self.line_window.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_window.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_window.setObjectName("line_window")

        ### start/stop ###
        self.pushButton_startstop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_startstop.setGeometry(QtCore.QRect(90, 490, 60, 40))
        self.pushButton_startstop.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_startstop.setFont(font)
        self.pushButton_startstop.setObjectName("pushButton_startstop")
        self.pushButton_startstop.setText('Start')
        # функция изменения цвета кнопки при нажатии
        self.pushButton_startstop.clicked.connect(self.startstop)

        self.label_hotkey_startstop = QtWidgets.QLabel(self.centralwidget)
        self.label_hotkey_startstop.setGeometry(QtCore.QRect(90, 530, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_hotkey_startstop.setFont(font)
        self.label_hotkey_startstop.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hotkey_startstop.setObjectName("label_hotkey_startstop")
        self.label_hotkey_startstop.setText('press F12')

        ### button lockated ###
        self.pushButton_located = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_located.setGeometry(QtCore.QRect(20, 490, 61, 41))
        self.pushButton_located.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_located.setFont(font)
        self.pushButton_located.setObjectName("pushButton_located")
        self.pushButton_located.clicked.connect(self.get_window_id)

        self.label_id_window = QtWidgets.QLabel(self.centralwidget)
        self.label_id_window.setGeometry(QtCore.QRect(20, 530, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_id_window.setFont(font)
        self.label_id_window.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_window.setObjectName("label_id_window")
        self.label_id_window.setText("id window")

        ### --------------------- ###
        ###     profile BLOCK     ###
        ### --------------------- ###
        self.label_profiles = QtWidgets.QLabel(self.centralwidget)
        self.label_profiles.setGeometry(QtCore.QRect(170, 390, 111, 16))
        self.label_profiles.setObjectName("label_profiles")
        self.label_profiles.setText('Profiles')

        self.pushButton_profile1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile1.setGeometry(QtCore.QRect(170, 420, 111, 21))
        self.pushButton_profile1.setStyleSheet("background-color: rgb(255, 239, 220);")
        self.pushButton_profile1.setObjectName("pushButton_profile1")
        self.pushButton_profile1.setText('profile 1')

        self.pushButton_profile2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile2.setGeometry(QtCore.QRect(170, 450, 111, 21))
        self.pushButton_profile2.setStyleSheet("background-color: rgb(255, 239, 220);")
        self.pushButton_profile2.setObjectName("pushButton_profile2")
        self.pushButton_profile2.setText('profile 2')

        self.pushButton_profile3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile3.setGeometry(QtCore.QRect(170, 480, 111, 21))
        self.pushButton_profile3.setStyleSheet("background-color: rgb(255, 239, 220);")
        self.pushButton_profile3.setObjectName("pushButton_profile3")
        self.pushButton_profile3.setText('profile 3')

        self.line_profiles = QtWidgets.QFrame(self.centralwidget)
        self.line_profiles.setGeometry(QtCore.QRect(209, 390, 71, 20))
        self.line_profiles.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_profiles.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_profiles.setObjectName("line_profiles")

        ### button save ###
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(170, 510, 51, 31))
        self.pushButton_save.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.setText('save')
        self.pushButton_save.clicked.connect(self.profile_save)

        ### button load ###
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(230, 510, 51, 31))
        self.pushButton_load.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_load.setFont(font)
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_load.setText('load')
        self.pushButton_load.clicked.connect(self.profile_load)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ### --------------------- ###
        ###  info.actions BLOCK   ###
        ### --------------------- ###
        self.label_information_actions = QtWidgets.QLabel(self.centralwidget)
        self.label_information_actions.setGeometry(QtCore.QRect(50, 550, 201, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_information_actions.setFont(font)
        self.label_information_actions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_information_actions.setObjectName("label_information_actions")

    ### functions ###
    def press_f12(self):
        self.pushButton_startstop.click()

    def hotkey_thread(self):
        add_hotkey('F12', self.press_f12)

    def startstop(self):
        if self.pushButton_startstop.text() == 'Start':
            self.pushButton_startstop.setText('Stop')
            self.label_information_actions.setText("Started clicker")
            self.toggle_q(self.checkBox_q.checkState())
            self.toggle_w(self.checkBox_w.checkState())

        else:
            self.pushButton_startstop.setText('Start')
            self.label_information_actions.setText('Stopped clicker')
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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    thread = threading.Thread(target=ui.update_hot_time_icon)
    thread.start()
    thread_press_f12 = threading.Thread(target=ui.hotkey_thread)
    thread_press_f12.start()
    thread_press_f11 = threading.Thread(target=ui.hotkey_thread_f11)
    thread_press_f11.start()
    MainWindow.show()
    sys.exit(app.exec_())
