from PyQt5.QtWidgets import QLabel, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect


class InterfaceUi:
    def __init__(self):
        self.line_half_window = None
        self.line_tuning_keys_2 = None
        self.line_tuning_keys_1 = None
        self.label_tuning_keys = None

    def setup_ui(self, parent):
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        
        self.label_tuning_keys = QLabel(parent)
        self.label_tuning_keys.setGeometry(QRect(10, 0, 61, 16))

        self.label_tuning_keys.setFont(font)
        self.label_tuning_keys.setObjectName("label_tuning_keys")
        self.label_tuning_keys.setStyleSheet("background: none;")
        self.label_tuning_keys.setText("Tuning keys")

        self.line_tuning_keys_1 = QFrame(parent)
        self.line_tuning_keys_1.setGeometry(QRect(69, 0, 81, 20))
        self.line_tuning_keys_1.setFrameShape(QFrame.HLine)
        self.line_tuning_keys_1.setFrameShadow(QFrame.Sunken)
        self.line_tuning_keys_1.setStyleSheet("background: none;")
        self.line_tuning_keys_1.setObjectName("line_tuning_keys_1")

        self.line_tuning_keys_2 = QFrame(parent)
        self.line_tuning_keys_2.setGeometry(QRect(170, 0, 111, 20))
        self.line_tuning_keys_2.setFrameShape(QFrame.HLine)
        self.line_tuning_keys_2.setFrameShadow(QFrame.Sunken)
        self.line_tuning_keys_2.setStyleSheet("background: none;")
        self.line_tuning_keys_2.setObjectName("line_tuning_keys_2")

        self.line_half_window = QFrame(parent)
        self.line_half_window.setGeometry(QRect(150, 20, 20, 300))
        self.line_half_window.setFrameShape(QFrame.VLine)
        self.line_half_window.setFrameShadow(QFrame.Sunken)
        self.line_half_window.setStyleSheet("background: none;")
        self.line_half_window.setObjectName("line_half_window")
