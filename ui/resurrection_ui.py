from PyQt5.QtWidgets import QCheckBox, QLabel
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont
from logic.state_manager import *


class ResurrectionUI:
    def __init__(self):
        self.resurrection_labels = None
        self.resurrection_check_boxes = None

    def create_resurrection_widgets(self, parent):
        font = QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)

        resurrection_labels = {
            'res': {'object_name': 'label_res', 'rect': [180, 320, 60, 20], 'text': ''},
            'res_random': {'object_name': 'label_res_random', 'rect': [180, 350, 60, 20], 'text': ''},
            'night_teleport': {'object_name': 'label_night_teleport', 'rect': [30, 350, 60, 20], 'text': ''},
            'night_teleport_solo': {'object_name': 'label_night_teleport_solo', 'rect': [30, 320, 60, 20], 'text': ''},
        }

        self.resurrection_labels = {}

        for key, properties in resurrection_labels.items():
            label = QLabel(parent)
            rect = properties['rect']
            label.setGeometry(rect[0], rect[1], rect[2], rect[3])
            label.setObjectName(properties['object_name'])
            label.setText(properties['text'])
            label.setFont(font)
            label.setStyleSheet("background: none;")

            self.resurrection_labels[key] = label

    def create_resurrection_check_boxes(self, parent):
        check_box_font = QFont()
        check_box_font.setBold(True)
        check_box_font.setWeight(75)

        resurrection_check_boxes = {
            'res': {
                'object_name': 'check_box_res', 
                'rect': [250, 320, 40, 20], 
                'text': 'res', 
                'tool_tip': 'Свободный телепорт должен быть на F11',
                'disabled': False
            },
            'res_without_wait': {
                'object_name': 'check_box_res_without_wait',
                'rect': [350, 320, 20, 20],
                'text': '',
                'tool_tip': 'Перезалет по точке через 5 секунд после реса',
                'disabled': True
            },
            'res_random': {
                'object_name': 'check_box_res_random',
                'rect': [250, 350, 85, 20],
                'text': 'res random',
                'tool_tip': 'Свободный телепорт должен быть на F7, F8, F9, F10, F11',
                'disabled': False
            },
            'res_random_without_wait': {
                'object_name': 'check_box_res_random_without_wait',
                'rect': [350, 350, 20, 20],
                'text': 'F4',
                'tool_tip': 'Перезалет по точке через 5 секунд после реса',
                'disabled': True
            }
        }

        self.resurrection_check_boxes = {}

        for key, properties in resurrection_check_boxes.items():
            check_box = QCheckBox(parent)
            rect = properties['rect']
            check_box.setGeometry(rect[0], rect[1], rect[2], rect[3])
            check_box.setFont(check_box_font)
            check_box.setObjectName(properties['object_name'])
            check_box.setText(properties['text'])
            check_box.setStyleSheet("background: none;")
            check_box.setDisabled(properties['disabled'])
            check_box.setToolTip(properties['tool_tip'])

            self.resurrection_check_boxes[key] = check_box

    def add_resurrection_widgets(self, parent):
        self.create_resurrection_check_boxes(parent)
        self.create_resurrection_widgets(parent)
