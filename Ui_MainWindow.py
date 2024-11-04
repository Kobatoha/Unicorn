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
        MainWindow.setWindowIcon(QtGui.QIcon("images/unicorn.png"))
        MainWindow.resize(350, 600)
        MainWindow.setMinimumSize(QtCore.QSize(165, 360))
        MainWindow.setMaximumSize(QtCore.QSize(350, 600))
        MainWindow.setBaseSize(QtCore.QSize(350, 600))
        MainWindow.setStyleSheet("background-image: url('images/bg_image.jpg');")

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
        self.label_tuning_keys.setStyleSheet("background: none;")
        self.label_tuning_keys.setText("Tuning keys")

        self.line_tuning_keys_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_tuning_keys_1.setGeometry(QtCore.QRect(69, 0, 81, 20))
        self.line_tuning_keys_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_tuning_keys_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_tuning_keys_1.setStyleSheet("background: none;")
        self.line_tuning_keys_1.setObjectName("line_tuning_keys_1")

        self.line_tuning_keys_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_tuning_keys_2.setGeometry(QtCore.QRect(170, 0, 111, 20))
        self.line_tuning_keys_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_tuning_keys_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_tuning_keys_2.setStyleSheet("background: none;")
        self.line_tuning_keys_2.setObjectName("line_tuning_keys_2")

        self.line_half_window = QtWidgets.QFrame(self.centralwidget)
        self.line_half_window.setGeometry(QtCore.QRect(150, 20, 20, 300))
        self.line_half_window.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_half_window.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_half_window.setStyleSheet("background: none;")
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

        self.lineEdit_Q = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Q.setGeometry(QtCore.QRect(30, 170, 60, 20))
        self.lineEdit_Q.setObjectName("lineEdit_Q")

        self.lineEdit_W = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_W.setGeometry(QtCore.QRect(30, 200, 60, 20))
        self.lineEdit_W.setObjectName("lineEdit_W")

        self.lineEdit_E = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_E.setGeometry(QtCore.QRect(30, 230, 60, 20))
        self.lineEdit_E.setObjectName("lineEdit_E")

        self.lineEdit_R = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_R.setGeometry(QtCore.QRect(30, 260, 60, 20))
        self.lineEdit_R.setObjectName("lineEdit_R")

        self.lineEdit_T = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_T.setGeometry(QtCore.QRect(30, 290, 60, 20))
        self.lineEdit_T.setObjectName("lineEdit_T")

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
        self.checkBox_f1.setStyleSheet("background: none;")
        self.checkBox_f1.stateChanged.connect(self.toggle_f1)
        self.keyboard = Controller()
        self.pressed_f1 = False
        self._f1_thread = None

        self.checkBox_f2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f2.setGeometry(QtCore.QRect(100, 50, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f2.setFont(font)
        self.checkBox_f2.setObjectName("checkBox_f2")
        self.checkBox_f2.setText("F2")
        self.checkBox_f2.setStyleSheet("background: none;")
        self.checkBox_f2.stateChanged.connect(self.toggle_f2)
        self.keyboard = Controller()
        self.pressed_f2 = False
        self._f2_thread = None

        self.checkBox_f3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f3.setGeometry(QtCore.QRect(100, 80, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f3.setFont(font)
        self.checkBox_f3.setObjectName("checkBox_f3")
        self.checkBox_f3.setText("F3")
        self.checkBox_f3.setStyleSheet("background: none;")
        self.checkBox_f3.stateChanged.connect(self.toggle_f3)
        self.keyboard = Controller()
        self.pressed_f3 = False
        self._f3_thread = None

        self.checkBox_f4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f4.setGeometry(QtCore.QRect(100, 110, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f4.setFont(font)
        self.checkBox_f4.setObjectName("checkBox_f4")
        self.checkBox_f4.setText("F4")
        self.checkBox_f4.setStyleSheet("background: none;")
        self.checkBox_f4.stateChanged.connect(self.toggle_f4)
        self.keyboard = Controller()
        self.pressed_f4 = False
        self._f4_thread = None

        self.checkBox_f5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_f5.setGeometry(QtCore.QRect(100, 140, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_f5.setFont(font)
        self.checkBox_f5.setObjectName("checkBox_f5")
        self.checkBox_f5.setText("F5")
        self.checkBox_f5.setStyleSheet("background: none;")
        self.checkBox_f5.stateChanged.connect(self.toggle_f5)
        self.keyboard = Controller()
        self.pressed_f5 = False
        self._f5_thread = None

        self.checkBox_Q = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Q.setGeometry(QtCore.QRect(100, 170, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Q.setFont(font)
        self.checkBox_Q.setObjectName("checkBox_Q")
        self.checkBox_Q.setText("Q")
        self.checkBox_Q.setStyleSheet("background: none;")
        self.checkBox_Q.stateChanged.connect(self.toggle_Q)
        self.keyboard = Controller()
        self.pressed_Q = False
        self._Q_thread = None

        self.checkBox_W = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_W.setGeometry(QtCore.QRect(100, 200, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_W.setFont(font)
        self.checkBox_W.setObjectName("checkBox_W")
        self.checkBox_W.setText("W")
        self.checkBox_W.setStyleSheet("background: none;")
        self.checkBox_W.stateChanged.connect(self.toggle_W)
        self.keyboard = Controller()
        self.pressed_W = False
        self._W_thread = None

        self.checkBox_E = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_E.setGeometry(QtCore.QRect(100, 230, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_E.setFont(font)
        self.checkBox_E.setObjectName("checkBox_E")
        self.checkBox_E.setText("E")
        self.checkBox_E.setStyleSheet("background: none;")
        self.checkBox_E.stateChanged.connect(self.toggle_E)
        self.keyboard = Controller()
        self.pressed_E = False
        self._E_thread = None

        self.checkBox_R = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_R.setGeometry(QtCore.QRect(100, 260, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_R.setFont(font)
        self.checkBox_R.setObjectName("checkBox_R")
        self.checkBox_R.setText("R")
        self.checkBox_R.setStyleSheet("background: none;")
        self.checkBox_R.stateChanged.connect(self.toggle_R)
        self.keyboard = Controller()
        self.pressed_R = False
        self._R_thread = None

        self.checkBox_T = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_T.setGeometry(QtCore.QRect(100, 290, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_T.setFont(font)
        self.checkBox_T.setObjectName("checkBox_T")
        self.checkBox_T.setText("T")
        self.checkBox_T.setStyleSheet("background: none;")
        self.checkBox_T.stateChanged.connect(self.toggle_T)
        self.keyboard = Controller()
        self.pressed_T = False
        self._T_thread = None

        ### --------------------- ###
        ###   CheckBox 1-0 BLOCK  ###
        ### --------------------- ###
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(250, 20, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_1.setText("1")
        self.checkBox_1.setStyleSheet("background: none;")
        self.checkBox_1.stateChanged.connect(self.toggle_1)
        self.keyboard = Controller()
        self.pressed_1 = False
        self._1_thread = None

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(250, 50, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setText("2")
        self.checkBox_2.setStyleSheet("background: none;")
        self.checkBox_2.stateChanged.connect(self.toggle_2)
        self.keyboard = Controller()
        self.pressed_2 = False
        self._2_thread = None

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(250, 80, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setText("3")
        self.checkBox_3.setStyleSheet("background: none;")
        self.checkBox_3.stateChanged.connect(self.toggle_3)
        self.keyboard = Controller()
        self.pressed_3 = False
        self._3_thread = None

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 110, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setText("4")
        self.checkBox_4.setStyleSheet("background: none;")
        self.checkBox_4.stateChanged.connect(self.toggle_4)
        self.keyboard = Controller()
        self.pressed_4 = False
        self._4_thread = None

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(250, 140, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_5.setText("5")
        self.checkBox_5.setStyleSheet("background: none;")
        self.checkBox_5.stateChanged.connect(self.toggle_5)
        self.keyboard = Controller()
        self.pressed_5 = False
        self._5_thread = None

        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(250, 170, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_6.setText("6")
        self.checkBox_6.setStyleSheet("background: none;")
        self.checkBox_6.stateChanged.connect(self.toggle_6)
        self.keyboard = Controller()
        self.pressed_6 = False
        self._6_thread = None

        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(250, 200, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_7.setText("7")
        self.checkBox_7.setStyleSheet("background: none;")
        self.checkBox_7.stateChanged.connect(self.toggle_7)
        self.keyboard = Controller()
        self.pressed_7 = False
        self._7_thread = None

        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(250, 230, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_8.setText("8")
        self.checkBox_8.setStyleSheet("background: none;")
        self.checkBox_8.stateChanged.connect(self.toggle_8)
        self.keyboard = Controller()
        self.pressed_8 = False
        self._8_thread = None

        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(250, 260, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_9.setText("9")
        self.checkBox_9.setStyleSheet("background: none;")
        self.checkBox_9.stateChanged.connect(self.toggle_9)
        self.keyboard = Controller()
        self.pressed_9 = False
        self._9_thread = None

        self.checkBox_tilda = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_tilda.setGeometry(QtCore.QRect(250, 290, 40, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_tilda.setFont(font)
        self.checkBox_tilda.setObjectName("checkBox_tilda")
        self.checkBox_tilda.setText("`")
        self.checkBox_tilda.setStyleSheet("background: none;")
        self.checkBox_tilda.stateChanged.connect(self.toggle_tilda)
        self.keyboard = Controller()
        self.pressed_tilda = False
        self._tilda_thread = None

        ### --------------------- ###
        ###   LineEdit Q-V BLOCK  ###
        ### --------------------- ###
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(180, 20, 60, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 50, 60, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 80, 60, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 110, 60, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 140, 60, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 170, 60, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(180, 200, 60, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 230, 60, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(180, 260, 60, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.lineEdit_tilda = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tilda.setGeometry(QtCore.QRect(180, 290, 60, 20))
        self.lineEdit_tilda.setObjectName("lineEdit_tilda")

        self.label_res = QtWidgets.QLabel(self.centralwidget)
        self.label_res.setGeometry(QtCore.QRect(180, 320, 60, 20))
        self.label_res.setObjectName("lineEdit_res")
        self.label_res.setStyleSheet("background: none;")

        self.label_res_random = QtWidgets.QLabel(self.centralwidget)
        self.label_res_random.setGeometry(QtCore.QRect(180, 350, 60, 20))
        self.label_res_random.setObjectName("lineEdit_res_random")
        self.label_res_random.setStyleSheet("background: none;")

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
        self.label_icons.setStyleSheet("background: none;")

        self.line_icons_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_icons_1.setGeometry(QtCore.QRect(50, 370, 101, 20))
        self.line_icons_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_icons_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_icons_1.setObjectName("line_icons_1")
        self.line_icons_1.setStyleSheet("background: none;")

        self.line_icons_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_icons_2.setGeometry(QtCore.QRect(170, 370, 111, 20))
        self.line_icons_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_icons_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_icons_2.setObjectName("line_icons_2")
        self.line_icons_2.setStyleSheet("background: none;")

        ### hot time ###
        self.label_hottime = QtWidgets.QLabel(self.centralwidget)
        self.label_hottime.setGeometry(QtCore.QRect(20, 390, 31, 31))
        self.label_hottime.setPixmap(QtGui.QPixmap("images/hot_time_off.png"))
        self.label_hottime.setScaledContents(True)
        self.label_hottime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hottime.setObjectName("label_hottime")
        self.label_hottime.setStyleSheet("background: none;")

        self.label_hottime_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_hottime_2.setGeometry(QtCore.QRect(10, 420, 51, 16))
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
        self.label_hottime_2.setStyleSheet("background: none;")

        ### auto ressurection ###
        self.check_box_res = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box_res.setGeometry(QtCore.QRect(250, 320, 40, 20))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.check_box_res.setFont(font)
        self.check_box_res.setObjectName("check_box_res")
        self.check_box_res.setText("res")
        self.check_box_res.setStyleSheet("background: none;")
        self.check_box_res.stateChanged.connect(self.toggle_res)
        self.keyboard = Controller()
        self.pressed_res = False

        self._res_thread = None
        self.res_process = None

        ### auto ressurection 2###
        self.check_box_res_random = QtWidgets.QCheckBox(self.centralwidget)
        self.check_box_res_random.setGeometry(QtCore.QRect(250, 350, 85, 20))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.check_box_res_random.setFont(font)
        self.check_box_res_random.setObjectName("check_box_res_random")
        self.check_box_res_random.setText("res random")
        self.check_box_res_random.setStyleSheet("background: none;")
        self.check_box_res_random.stateChanged.connect(self.toggle_res_random)
        self.keyboard = Controller()
        self.pressed_res_random = False

        self._res_random_thread = None
        self.res_random_process = None

        ### --------------------- ###
        ###      Window BLOCK     ###
        ### --------------------- ###
        self.label_window = QtWidgets.QLabel(self.centralwidget)
        self.label_window.setGeometry(QtCore.QRect(10, 440, 51, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_window.setFont(font)
        self.label_window.setAlignment(QtCore.Qt.AlignCenter)
        self.label_window.setObjectName("label_window")
        self.label_window.setText("Window id")
        self.label_window.setStyleSheet("background: none;")

        self.line_window = QtWidgets.QFrame(self.centralwidget)
        self.line_window.setGeometry(QtCore.QRect(65, 440, 91, 20))
        self.line_window.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_window.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_window.setObjectName("line_window")
        self.line_window.setStyleSheet("background: none;")

        ### button start/stop ###
        self.pushButton_startstop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_startstop.setGeometry(QtCore.QRect(100, 490, 40, 40))
        self.pushButton_startstop.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_startstop.setFont(font)
        self.pushButton_startstop.setObjectName("pushButton_startstop")
        self.pushButton_startstop.setText('Start')
        self.pushButton_startstop.clicked.connect(self.startstop)

        self.label_hotkey_startstop = QtWidgets.QLabel(self.centralwidget)
        self.label_hotkey_startstop.setGeometry(QtCore.QRect(95, 530, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_hotkey_startstop.setFont(font)
        self.label_hotkey_startstop.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hotkey_startstop.setObjectName("label_hotkey_startstop")
        self.label_hotkey_startstop.setText('INSERT')
        self.label_hotkey_startstop.setStyleSheet("background: none;")

        ### button lockated ###
        self.pushButton_located = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_located.setGeometry(QtCore.QRect(30, 490, 41, 41))
        self.pushButton_located.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_located.setFont(font)
        self.pushButton_located.setObjectName("pushButton_located")
        self.pushButton_located.setIcon(QtGui.QIcon('images/target_off.png'))
        self.pushButton_located.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_located.clicked.connect(self.get_window_id)

        self.msg_box_active = False

        self.label_id_window = QtWidgets.QLabel(self.centralwidget)
        self.label_id_window.setGeometry(QtCore.QRect(25, 530, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_id_window.setFont(font)
        self.label_id_window.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_window.setObjectName("label_id_window")
        self.label_id_window.setText("")
        self.label_id_window.setStyleSheet("background: none;")

        self.lineEdit_window_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_window_id.setGeometry(QtCore.QRect(40, 460, 90, 20))
        self.lineEdit_window_id.setObjectName("lineEdit_window_id")
        self.lineEdit_window_id.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.lineEdit_window_id.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)

        ### --------------------- ###
        ###     profile BLOCK     ###
        ### --------------------- ###
        self.label_profiles = QtWidgets.QLabel(self.centralwidget)
        self.label_profiles.setGeometry(QtCore.QRect(170, 390, 111, 16))
        self.label_profiles.setObjectName("label_profiles")
        self.label_profiles.setText('Profiles')
        self.label_profiles.setStyleSheet("background: none;")

        self.pushButton_profile1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile1.setGeometry(QtCore.QRect(240, 420, 50, 20))
        self.pushButton_profile1.setStyleSheet("background-color: rgb(255, 239, 220);")
        self.pushButton_profile1.setObjectName("pushButton_profile1")
        self.pushButton_profile1.setText('profile 1')
        self.pushButton_profile1.clicked.connect(self.profile1)

        self.lineEdit_profile1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_profile1.setGeometry(QtCore.QRect(170, 420, 60, 20))
        self.lineEdit_profile1.setObjectName("lineEdit_window_id")
        self.lineEdit_profile1.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.lineEdit_profile1.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)

        self.pushButton_profile2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile2.setGeometry(QtCore.QRect(240, 450, 50, 20))
        self.pushButton_profile2.setStyleSheet("background-color: rgb(255, 239, 220);")
        self.pushButton_profile2.setObjectName("pushButton_profile2")
        self.pushButton_profile2.setText('profile 2')
        self.pushButton_profile2.clicked.connect(self.profile2)

        self.lineEdit_profile2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_profile2.setGeometry(QtCore.QRect(170, 450, 60, 20))
        self.lineEdit_profile2.setObjectName("lineEdit_window_id")
        self.lineEdit_profile2.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.lineEdit_profile2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)

        self.pushButton_profile3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_profile3.setGeometry(QtCore.QRect(240, 480, 50, 20))
        self.pushButton_profile3.setStyleSheet("background-color: rgb(255, 239, 220);")
        self.pushButton_profile3.setObjectName("pushButton_profile3")
        self.pushButton_profile3.setText('profile 3')
        self.pushButton_profile3.clicked.connect(self.profile3)

        self.lineEdit_profile3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_profile3.setGeometry(QtCore.QRect(170, 480, 60, 20))
        self.lineEdit_profile3.setObjectName("lineEdit_window_id")
        self.lineEdit_profile3.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.lineEdit_profile3.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)

        self.line_profiles = QtWidgets.QFrame(self.centralwidget)
        self.line_profiles.setGeometry(QtCore.QRect(209, 390, 71, 20))
        self.line_profiles.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_profiles.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_profiles.setObjectName("line_profiles")
        self.line_profiles.setStyleSheet("background: none;")

        ### button save ###
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(170, 510, 51, 31))
        self.pushButton_save.setStyleSheet("background-color: rgb(255, 239, 220);")
        font_save = QtGui.QFont()
        font_save.setPointSize(8)
        # font_save.setBold(False)
        # font_save.setWeight(75)
        self.pushButton_save.setFont(font_save)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.setText('save\n profile 1')
        self.pushButton_save.clicked.connect(self.save_settings)

        ### button load ###
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setGeometry(QtCore.QRect(230, 510, 51, 31))
        self.pushButton_load.setStyleSheet("background-color: rgb(255, 239, 220);")
        self.pushButton_load.setFont(font_save)
        self.pushButton_load.setObjectName("pushButton_load")
        self.pushButton_load.setText('load\n profile 1')
        self.pushButton_load.clicked.connect(self.load_settings)
        self.pushButton_load.hide()

        self.load_settings()

        ###   ---------------------------  ###
        ###  menubar and statusbar BLOCK   ###
        ###   ---------------------------  ###
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet("background: none;")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusbar.setFixedHeight(22)
        self.statusbar.setStyleSheet("background: none;")

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
        self.label_information_actions.setStyleSheet("background: none;")
