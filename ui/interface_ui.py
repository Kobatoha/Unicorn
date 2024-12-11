from PyQt5.QtWidgets import QLabel, QFrame
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QRect, Qt


class InterfaceUi:
    def __init__(self):
        self.label_hottime_2 = None
        self.label_hottime = None
        self.line_icons_2 = None
        self.line_icons_1 = None
        self.label_icons = None
        self.line_half_window = None
        self.line_tuning_keys_2 = None
        self.line_tuning_keys_1 = None
        self.label_tuning_keys = None

    def add_interface_widgets(self, parent):
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

        self.label_icons = QLabel(parent)
        self.label_icons.setGeometry(QRect(10, 370, 41, 16))
        self.label_icons.setFont(font)
        self.label_icons.setAlignment(Qt.AlignCenter)
        self.label_icons.setObjectName("label_icons")
        self.label_icons.setText("Icons")
        self.label_icons.setStyleSheet("background: none;")

        self.line_icons_1 = QFrame(parent)
        self.line_icons_1.setGeometry(QRect(50, 370, 101, 20))
        self.line_icons_1.setFrameShape(QFrame.HLine)
        self.line_icons_1.setFrameShadow(QFrame.Sunken)
        self.line_icons_1.setObjectName("line_icons_1")
        self.line_icons_1.setStyleSheet("background: none;")

        self.line_icons_2 = QFrame(parent)
        self.line_icons_2.setGeometry(QRect(170, 370, 111, 20))
        self.line_icons_2.setFrameShape(QFrame.HLine)
        self.line_icons_2.setFrameShadow(QFrame.Sunken)
        self.line_icons_2.setObjectName("line_icons_2")
        self.line_icons_2.setStyleSheet("background: none;")

    def add_hottime_widgets(self, parent):
        font = QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.label_hottime = QLabel(parent)
        self.label_hottime.setGeometry(QRect(20, 390, 31, 31))
        self.label_hottime.setPixmap(QPixmap("resources/images/hot_time_off.png"))
        self.label_hottime.setScaledContents(True)
        self.label_hottime.setAlignment(Qt.AlignCenter)
        self.label_hottime.setObjectName("label_hottime")
        self.label_hottime.setStyleSheet("background: none;")

        self.label_hottime_2 = QLabel(parent)
        self.label_hottime_2.setGeometry(QRect(10, 420, 51, 16))
        self.label_hottime_2.setFont(font)
        self.label_hottime_2.setAlignment(Qt.AlignCenter)
        self.label_hottime_2.setObjectName("label_hottime_2")
        self.label_hottime_2.setText("Hot Time")
        self.label_hottime_2.setStyleSheet("background: none;")