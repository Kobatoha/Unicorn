from PyQt5.QtWidgets import QCheckBox, QLabel
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from logic.state_manager import *


class KeyboardUi:
    def __init__(self):
        self.label_night_teleport_solo = None
        self.label_night_teleport = None
        self.label_res_random = None
        self.label_res = None

    def add_resurrection_widgets(self, parent):
        self.label_res = QLabel(parent)
        self.label_res.setGeometry(QRect(180, 320, 60, 20))
        self.label_res.setObjectName("lineEdit_res")
        self.label_res.setStyleSheet("background: none;")

        self.label_res_random = QLabel(parent)
        self.label_res_random.setGeometry(QRect(180, 350, 60, 20))
        self.label_res_random.setObjectName("lineEdit_res_random")
        self.label_res_random.setStyleSheet("background: none;")

        self.label_night_teleport = QLabel(parent)
        self.label_night_teleport.setGeometry(QRect(30, 350, 60, 20))
        self.label_night_teleport.setObjectName("label_night_teleport")
        self.label_night_teleport.setStyleSheet("background: none;")

        self.label_night_teleport_solo = QLabel(parent)
        self.label_night_teleport_solo.setGeometry(QRect(30, 320, 60, 20))
        self.label_night_teleport_solo.setObjectName("label_night_teleport")
        self.label_night_teleport_solo.setStyleSheet("background: none;")
