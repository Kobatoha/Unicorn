from PyQt5.QtWidgets import QCheckBox, QLineEdit
from PyQt5.QtGui import QFont
from logic.state_manager import *


class KeyboardUI:
    def __init__(self):
        self.right_check_boxes = None
        self.right_line_edits = None
        self.left_check_boxes = None
        self.left_line_edits = None

    def create_keyboard_left_line_edits(self, parent):
        left_line_edits = {
            'f1': {'object_name': 'line_edit_f1', 'rect': [30, 20, 60, 20]},
            'f2': {'object_name': 'line_edit_f2', 'rect': [30, 50, 60, 20]},
            'f3': {'object_name': 'line_edit_f3', 'rect': [30, 80, 60, 20]},
            'f4': {'object_name': 'line_edit_f4', 'rect': [30, 110, 60, 20]},
            'f5': {'object_name': 'line_edit_f5', 'rect': [30, 140, 60, 20]},
            'q': {'object_name': 'line_edit_q', 'rect': [30, 170, 60, 20]},
            'w': {'object_name': 'line_edit_w', 'rect': [30, 200, 60, 20]},
            'e': {'object_name': 'line_edit_e', 'rect': [30, 230, 60, 20]},
            'r': {'object_name': 'line_edit_r', 'rect': [30, 260, 60, 20]},
            '-': {'object_name': 'line_edit_minus', 'rect': [30, 290, 60, 20]},
        }

        self.left_line_edits = {}

        for key, properties in left_line_edits.items():
            line_edit = QLineEdit(parent)
            rect = properties['rect']
            line_edit.setGeometry(rect[0], rect[1], rect[2], rect[3])
            line_edit.setObjectName(properties['object_name'])

            self.left_line_edits[key] = line_edit

    def create_keyboard_left_check_boxes(self, parent):
        check_box_font = QFont()
        check_box_font.setBold(True)
        check_box_font.setWeight(75)

        left_check_boxes = {
            'f1': {'object_name': 'check_box_f1', 'rect': [100, 20, 40, 20], 'text': 'F1'},
            'f2': {'object_name': 'check_box_f2', 'rect': [100, 50, 40, 20], 'text': 'F2'},
            'f3': {'object_name': 'check_box_f3', 'rect': [100, 80, 40, 20], 'text': 'F3'},
            'f4': {'object_name': 'check_box_f4', 'rect': [100, 110, 40, 20], 'text': 'F4'},
            '=': {'object_name': 'check_box_equal', 'rect': [100, 140, 40, 20], 'text': '='},
            'q': {'object_name': 'check_box_q', 'rect': [100, 170, 40, 20], 'text': 'Q'},
            'w': {'object_name': 'check_box_w', 'rect': [100, 200, 40, 20], 'text': 'W'},
            'e': {'object_name': 'check_box_e', 'rect': [100, 230, 40, 20], 'text': 'E'},
            'r': {'object_name': 'check_box_r', 'rect': [100, 260, 40, 20], 'text': 'R'},
            '-': {'object_name': 'check_box_minus', 'rect': [100, 290, 40, 20], 'text': '-'},
        }

        self.left_check_boxes = {}

        for key, properties in left_check_boxes.items():
            check_box = QCheckBox(parent)
            rect = properties['rect']
            check_box.setGeometry(rect[0], rect[1], rect[2], rect[3])
            check_box.setFont(check_box_font)
            check_box.setObjectName(properties['object_name'])
            check_box.setText(properties['text'])
            check_box.setStyleSheet("background: none;")

            self.left_check_boxes[key] = check_box

    def create_keyboard_right_line_edits(self, parent):
        right_line_edits = {
            '1': {'object_name': 'line_edit_1', 'rect': [180, 20, 60, 20]},
            '2': {'object_name': 'line_edit_2', 'rect': [180, 50, 60, 20]},
            '3': {'object_name': 'line_edit_3', 'rect': [180, 80, 60, 20]},
            '4': {'object_name': 'line_edit_4', 'rect': [180, 110, 60, 20]},
            '5': {'object_name': 'line_edit_5', 'rect': [180, 140, 60, 20]},
            '6': {'object_name': 'line_edit_6', 'rect': [180, 170, 60, 20]},
            '7': {'object_name': 'line_edit_7', 'rect': [180, 200, 60, 20]},
            '8': {'object_name': 'line_edit_8', 'rect': [180, 230, 60, 20]},
            '9': {'object_name': 'line_edit_9', 'rect': [180, 260, 60, 20]},
            'tilda': {'object_name': 'line_edit_tilda', 'rect': [180, 290, 60, 20]},
        }

        self.right_line_edits = {}

        for key, properties in right_line_edits.items():
            line_edit = QLineEdit(parent)
            rect = properties['rect']
            line_edit.setGeometry(rect[0], rect[1], rect[2], rect[3])
            line_edit.setObjectName(properties['object_name'])

            self.right_line_edits[key] = line_edit

    def create_keyboard_right_check_boxes(self, parent):
        check_box_font = QFont()
        check_box_font.setBold(True)
        check_box_font.setWeight(75)

        right_check_boxes = {
            '1': {'object_name': 'check_box_1', 'rect': [250, 20, 40, 20], 'text': '1'},
            '2': {'object_name': 'check_box_2', 'rect': [250, 50, 40, 20], 'text': '2'},
            '3': {'object_name': 'check_box_3', 'rect': [250, 80, 40, 20], 'text': '3'},
            '4': {'object_name': 'check_box_4', 'rect': [250, 110, 40, 20], 'text': '4'},
            '5': {'object_name': 'check_box_5', 'rect': [250, 140, 40, 20], 'text': '5'},
            '6': {'object_name': 'check_box_6', 'rect': [250, 170, 40, 20], 'text': '6'},
            '7': {'object_name': 'check_box_7', 'rect': [250, 200, 40, 20], 'text': '7'},
            '8': {'object_name': 'check_box_8', 'rect': [250, 230, 40, 20], 'text': '8'},
            '9': {'object_name': 'check_box_9', 'rect': [250, 260, 40, 20], 'text': '9'},
            'tilda': {'object_name': 'check_box_tilda', 'rect': [250, 290, 40, 20], 'text': '`'},
        }

        self.right_check_boxes = {}

        for key, properties in right_check_boxes.items():
            check_box = QCheckBox(parent)
            rect = properties['rect']
            check_box.setGeometry(rect[0], rect[1], rect[2], rect[3])
            check_box.setFont(check_box_font)
            check_box.setObjectName(properties['object_name'])
            check_box.setText(properties['text'])
            check_box.setStyleSheet("background: none;")

            self.right_check_boxes[key] = check_box
