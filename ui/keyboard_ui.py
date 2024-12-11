from PyQt5.QtWidgets import QCheckBox, QLineEdit
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from logic.state_manager import *


class KeyboardUi:
    def __init__(self):
        self.line_edit_f1 = None
        self.line_edit_f2 = None
        self.line_edit_f3 = None
        self.line_edit_f4 = None
        self.line_edit_f5 = None

        self.line_edit_q = None
        self.line_edit_w = None
        self.line_edit_e = None
        self.line_edit_r = None
        self.line_edit_t = None

        self.check_box_f1 = None
        self.check_box_f2 = None
        self.check_box_f3 = None
        self.check_box_f4 = None
        self.check_box_f5 = None

        self.check_box_q = None
        self.check_box_w = None
        self.check_box_e = None
        self.check_box_r = None
        self.check_box_t = None

        self.line_edit_1 = None
        self.line_edit_2 = None
        self.line_edit_3 = None
        self.line_edit_4 = None
        self.line_edit_5 = None
        self.line_edit_6 = None
        self.line_edit_7 = None
        self.line_edit_8 = None
        self.line_edit_9 = None
        self.line_edit_tilda = None

        self.check_box_1 = None
        self.check_box_2 = None
        self.check_box_3 = None
        self.check_box_4 = None
        self.check_box_5 = None
        self.check_box_6 = None
        self.check_box_7 = None
        self.check_box_8 = None
        self.check_box_9 = None
        self.check_box_tilda = None

    def add_keyboard_left_line_edits(self, parent):
        self.line_edit_f1 = QLineEdit(parent)
        self.line_edit_f1.setGeometry(QRect(30, 20, 60, 20))
        self.line_edit_f1.setObjectName("line_edit_f1")

        self.line_edit_f2 = QLineEdit(parent)
        self.line_edit_f2.setGeometry(QRect(30, 50, 60, 20))
        self.line_edit_f2.setObjectName("line_edit_f2")

        self.line_edit_f3 = QLineEdit(parent)
        self.line_edit_f3.setGeometry(QRect(30, 80, 60, 20))
        self.line_edit_f3.setObjectName("line_edit_f3")

        self.line_edit_f4 = QLineEdit(parent)
        self.line_edit_f4.setGeometry(QRect(30, 110, 60, 20))
        self.line_edit_f4.setObjectName("line_edit_f4")

        self.line_edit_f5 = QLineEdit(parent)
        self.line_edit_f5.setGeometry(QRect(30, 140, 60, 20))
        self.line_edit_f5.setObjectName("line_edit_f5")

        self.line_edit_q = QLineEdit(parent)
        self.line_edit_q.setGeometry(QRect(30, 170, 60, 20))
        self.line_edit_q.setObjectName("line_edit_q")

        self.line_edit_w = QLineEdit(parent)
        self.line_edit_w.setGeometry(QRect(30, 200, 60, 20))
        self.line_edit_w.setObjectName("line_edit_w")

        self.line_edit_e = QLineEdit(parent)
        self.line_edit_e.setGeometry(QRect(30, 230, 60, 20))
        self.line_edit_e.setObjectName("line_edit_e")

        self.line_edit_r = QLineEdit(parent)
        self.line_edit_r.setGeometry(QRect(30, 260, 60, 20))
        self.line_edit_r.setObjectName("line_edit_r")

        self.line_edit_t = QLineEdit(parent)
        self.line_edit_t.setGeometry(QRect(30, 290, 60, 20))
        self.line_edit_t.setObjectName("line_edit_t")

    def add_keyboard_left_check_boxes(self, parent):
        check_box_font = QFont()
        check_box_font.setBold(True)
        check_box_font.setWeight(75)

        self.check_box_f1 = QCheckBox(parent)
        self.check_box_f1.setGeometry(QRect(100, 20, 40, 20))
        self.check_box_f1.setText("F1")
        self.check_box_f1.setFont(check_box_font)
        self.check_box_f1.setObjectName("check_box_f1")
        self.check_box_f1.setStyleSheet("background: none;")

        self.check_box_f2 = QCheckBox(parent)
        self.check_box_f2.setGeometry(QRect(100, 50, 40, 20))
        self.check_box_f2.setFont(check_box_font)
        self.check_box_f2.setObjectName("check_box_f2")
        self.check_box_f2.setText("F2")
        self.check_box_f2.setStyleSheet("background: none;")

        self.check_box_f3 = QCheckBox(parent)
        self.check_box_f3.setGeometry(QRect(100, 80, 40, 20))
        self.check_box_f3.setFont(check_box_font)
        self.check_box_f3.setObjectName("check_box_f3")
        self.check_box_f3.setText("F3")
        self.check_box_f3.setStyleSheet("background: none;")

        self.check_box_f4 = QCheckBox(parent)
        self.check_box_f4.setGeometry(QRect(100, 110, 40, 20))
        self.check_box_f4.setFont(check_box_font)
        self.check_box_f4.setObjectName("check_box_f4")
        self.check_box_f4.setText("F4")
        self.check_box_f4.setStyleSheet("background: none;")

        self.check_box_f5 = QCheckBox(parent)
        self.check_box_f5.setGeometry(QRect(100, 140, 40, 20))
        self.check_box_f5.setFont(check_box_font)
        self.check_box_f5.setObjectName("check_box_f5")
        self.check_box_f5.setText("F5")
        self.check_box_f5.setStyleSheet("background: none;")

        self.check_box_q = QCheckBox(parent)
        self.check_box_q.setGeometry(QRect(100, 170, 40, 20))
        self.check_box_q.setFont(check_box_font)
        self.check_box_q.setObjectName("check_box_q")
        self.check_box_q.setText("Q")
        self.check_box_q.setStyleSheet("background: none;")

        self.check_box_w = QCheckBox(parent)
        self.check_box_w.setGeometry(QRect(100, 200, 40, 20))
        self.check_box_w.setFont(check_box_font)
        self.check_box_w.setObjectName("check_box_w")
        self.check_box_w.setText("W")
        self.check_box_w.setStyleSheet("background: none;")

        self.check_box_e = QCheckBox(parent)
        self.check_box_e.setGeometry(QRect(100, 230, 40, 20))
        self.check_box_e.setFont(check_box_font)
        self.check_box_e.setObjectName("check_box_e")
        self.check_box_e.setText("E")
        self.check_box_e.setStyleSheet("background: none;")

        self.check_box_r = QCheckBox(parent)
        self.check_box_r.setGeometry(QRect(100, 260, 40, 20))
        self.check_box_r.setFont(check_box_font)
        self.check_box_r.setObjectName("check_box_r")
        self.check_box_r.setText("R")
        self.check_box_r.setStyleSheet("background: none;")

        self.check_box_t = QCheckBox(parent)
        self.check_box_t.setGeometry(QRect(100, 290, 40, 20))
        self.check_box_t.setFont(check_box_font)
        self.check_box_t.setObjectName("check_box_t")
        self.check_box_t.setText("T")
        self.check_box_t.setStyleSheet("background: none;")

    def add_keyboard_right_line_edits(self, parent):
        self.line_edit_1 = QLineEdit(parent)
        self.line_edit_1.setGeometry(QRect(180, 20, 60, 20))
        self.line_edit_1.setObjectName("line_edit_1")

        self.line_edit_2 = QLineEdit(parent)
        self.line_edit_2.setGeometry(QRect(180, 50, 60, 20))
        self.line_edit_2.setObjectName("line_edit_2")

        self.line_edit_3 = QLineEdit(parent)
        self.line_edit_3.setGeometry(QRect(180, 80, 60, 20))
        self.line_edit_3.setObjectName("line_edit_3")

        self.line_edit_4 = QLineEdit(parent)
        self.line_edit_4.setGeometry(QRect(180, 110, 60, 20))
        self.line_edit_4.setObjectName("line_edit_4")

        self.line_edit_5 = QLineEdit(parent)
        self.line_edit_5.setGeometry(QRect(180, 140, 60, 20))
        self.line_edit_5.setObjectName("line_edit_5")

        self.line_edit_6 = QLineEdit(parent)
        self.line_edit_6.setGeometry(QRect(180, 170, 60, 20))
        self.line_edit_6.setObjectName("line_edit_6")

        self.line_edit_7 = QLineEdit(parent)
        self.line_edit_7.setGeometry(QRect(180, 200, 60, 20))
        self.line_edit_7.setObjectName("line_edit_7")

        self.line_edit_8 = QLineEdit(parent)
        self.line_edit_8.setGeometry(QRect(180, 230, 60, 20))
        self.line_edit_8.setObjectName("line_edit_8")

        self.line_edit_9 = QLineEdit(parent)
        self.line_edit_9.setGeometry(QRect(180, 260, 60, 20))
        self.line_edit_9.setObjectName("line_edit_9")

        self.line_edit_tilda = QLineEdit(parent)
        self.line_edit_tilda.setGeometry(QRect(180, 290, 60, 20))
        self.line_edit_tilda.setObjectName("line_edit_tilda")

    def add_keyboard_right_check_boxes(self, parent):
        check_box_font = QFont()
        check_box_font.setBold(True)
        check_box_font.setWeight(75)

        self.check_box_1 = QCheckBox(parent)
        self.check_box_1.setGeometry(QRect(250, 20, 40, 20))

        self.check_box_1.setFont(check_box_font)
        self.check_box_1.setObjectName("check_box_1")
        self.check_box_1.setText("1")
        self.check_box_1.setStyleSheet("background: none;")

        self.check_box_2 = QCheckBox(parent)
        self.check_box_2.setGeometry(QRect(250, 50, 40, 20))
        self.check_box_2.setFont(check_box_font)
        self.check_box_2.setObjectName("check_box_2")
        self.check_box_2.setText("2")
        self.check_box_2.setStyleSheet("background: none;")

        self.check_box_3 = QCheckBox(parent)
        self.check_box_3.setGeometry(QRect(250, 80, 40, 20))
        self.check_box_3.setFont(check_box_font)
        self.check_box_3.setObjectName("check_box_3")
        self.check_box_3.setText("3")
        self.check_box_3.setStyleSheet("background: none;")

        self.check_box_4 = QCheckBox(parent)
        self.check_box_4.setGeometry(QRect(250, 110, 40, 20))
        self.check_box_4.setFont(check_box_font)
        self.check_box_4.setObjectName("check_box_4")
        self.check_box_4.setText("4")
        self.check_box_4.setStyleSheet("background: none;")

        self.check_box_5 = QCheckBox(parent)
        self.check_box_5.setGeometry(QRect(250, 140, 40, 20))
        self.check_box_5.setFont(check_box_font)
        self.check_box_5.setObjectName("check_box_5")
        self.check_box_5.setText("5")
        self.check_box_5.setStyleSheet("background: none;")

        self.check_box_6 = QCheckBox(parent)
        self.check_box_6.setGeometry(QRect(250, 170, 40, 20))
        self.check_box_6.setFont(check_box_font)
        self.check_box_6.setObjectName("check_box_6")
        self.check_box_6.setText("6")
        self.check_box_6.setStyleSheet("background: none;")

        self.check_box_7 = QCheckBox(parent)
        self.check_box_7.setGeometry(QRect(250, 200, 40, 20))
        self.check_box_7.setFont(check_box_font)
        self.check_box_7.setObjectName("check_box_7")
        self.check_box_7.setText("7")
        self.check_box_7.setStyleSheet("background: none;")

        self.check_box_8 = QCheckBox(parent)
        self.check_box_8.setGeometry(QRect(250, 230, 40, 20))
        self.check_box_8.setFont(check_box_font)
        self.check_box_8.setObjectName("check_box_8")
        self.check_box_8.setText("8")
        self.check_box_8.setStyleSheet("background: none;")

        self.check_box_9 = QCheckBox(parent)
        self.check_box_9.setGeometry(QRect(250, 260, 40, 20))
        self.check_box_9.setFont(check_box_font)
        self.check_box_9.setObjectName("check_box_9")
        self.check_box_9.setText("9")
        self.check_box_9.setStyleSheet("background: none;")

        self.check_box_tilda = QCheckBox(parent)
        self.check_box_tilda.setGeometry(QRect(250, 290, 40, 20))
        self.check_box_tilda.setFont(check_box_font)
        self.check_box_tilda.setObjectName("check_box_tilda")
        self.check_box_tilda.setText("`")
        self.check_box_tilda.setStyleSheet("background: none;")
