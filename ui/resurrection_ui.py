from PyQt5.QtWidgets import QCheckBox, QLabel
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from logic.state_manager import *


class ResurrectionUI:
    def __init__(self):
        self.check_box_res_random_without_wait = None
        self.check_box_res_random = None
        self.check_box_res_without_wait = None
        self.check_box_res = None
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

    def add_resurrection_check_boxes(self, parent):
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        
        self.check_box_res = QCheckBox(parent)
        self.check_box_res.setGeometry(QRect(250, 320, 40, 20)) 
        self.check_box_res.setFont(font)
        self.check_box_res.setObjectName("check_box_res")
        self.check_box_res.setText("res")
        self.check_box_res.setStyleSheet("background: none;")
        self.check_box_res.setToolTip('Свободный телепорт должен быть на F11')

        self.check_box_res_without_wait = QCheckBox(parent)
        self.check_box_res_without_wait.setGeometry(QRect(350, 320, 20, 20))
        self.check_box_res_without_wait.setStyleSheet("background: none;")
        self.check_box_res_without_wait.setDisabled(True)
        self.check_box_res_without_wait.setToolTip('Перезалет по точке через 5 секунд после реса')

        self.check_box_res_random = QCheckBox(parent)
        self.check_box_res_random.setGeometry(QRect(250, 350, 85, 20))
        self.check_box_res_random.setFont(font)
        self.check_box_res_random.setObjectName("check_box_res_random")
        self.check_box_res_random.setText("res random")
        self.check_box_res_random.setStyleSheet("background: none;")
        self.check_box_res_random.setToolTip('Свободный телепорт должен быть на F7, F8, F9, F10, F11')

        self.check_box_res_random_without_wait = QCheckBox(parent)
        self.check_box_res_random_without_wait.setGeometry(QRect(350, 350, 20, 20))
        self.check_box_res_random_without_wait.setStyleSheet("background: none;")
        self.check_box_res_random_without_wait.setDisabled(True)
        self.check_box_res_random_without_wait.setToolTip('Перезалет по точке через 5 секунд после реса')