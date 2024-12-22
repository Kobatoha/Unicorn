from PyQt5.QtWidgets import QFrame, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class ProfileUI:
    def __init__(self):
        self.profile_buttons = None
        self.profile_frames = None
        self.profile_labels = None
        self.profile_line_edits = None

    def create_profile_widgets(self, parent):
        profile_labels = {
            'label_profiles': {'object_name': 'label_profiles', 'rect': [170, 390, 111, 16], 'text': 'Profiles'},
        }

        self.profile_labels = {}

        for key, properties in profile_labels.items():
            label = QLabel(parent)
            rect = properties['rect']
            label.setGeometry(rect[0], rect[1], rect[2], rect[3])
            label.setObjectName(properties['object_name'])
            label.setText(properties['text'])
            label.setStyleSheet("background: none;")

            self.profile_labels[key] = label

        font = QFont()
        font.setBold(False)
        font.setWeight(50)

        profile_frames = {
            'line_profiles': {'object_name': 'line_profiles', 'rect': [209, 390, 71, 20]},
        }

        self.profile_frames = {}

        for key, properties in profile_frames.items():
            frame = QFrame(parent)
            rect = properties['rect']
            frame.setGeometry(rect[0], rect[1], rect[2], rect[3])
            frame.setObjectName(properties['object_name'])
            frame.setFrameShape(QFrame.HLine)
            frame.setFrameShadow(QFrame.Sunken)
            frame.setStyleSheet("background: none;")

            self.profile_frames[key] = frame

    def create_profile_buttons(self, parent):
        button_font = QFont()
        button_font.setBold(False)
        button_font.setPointSize(8)

        profile_buttons = {
            'profile_1': {'object_name': 'push_button_profile_1', 'rect': [240, 420, 50, 20], 'text': 'profile 1'},
            'profile_2': {'object_name': 'push_button_profile_2', 'rect': [240, 450, 50, 20], 'text': 'profile 2'},
            'profile_3': {'object_name': 'push_button_profile_3', 'rect': [240, 480, 50, 20], 'text': 'profile 3'},
            'save': {'object_name': 'push_button_save', 'rect': [170, 510, 51, 31], 'text': 'save\n profile 1'},
            'load': {'object_name': 'push_button_load', 'rect': [230, 510, 51, 31], 'text': 'load\n profile 1'},
        }

        self.profile_buttons = {}

        for key, properties in profile_buttons.items():
            button = QPushButton(parent)
            rect = properties['rect']
            button.setGeometry(rect[0], rect[1], rect[2], rect[3])
            button.setFont(button_font)
            button.setObjectName(properties['object_name'])
            button.setText(properties['text'])
            button.setStyleSheet("background-color: rgb(255, 239, 220);")

            self.profile_buttons[key] = button

        self.profile_buttons['load'].hide()

    def create_profile_line_edits(self, parent):
        profile_line_edits = {
            'profile_1': {'object_name': 'line_edit_profile_1', 'rect': [170, 420, 60, 20]},
            'profile_2': {'object_name': 'line_edit_profile_2', 'rect': [170, 450, 60, 20]},
            'profile_3': {'object_name': 'line_edit_profile_3', 'rect': [170, 480, 60, 20]},
        }

        self.profile_line_edits = {}

        for key, properties in profile_line_edits.items():
            line_edit = QLineEdit(parent)
            rect = properties['rect']
            line_edit.setGeometry(rect[0], rect[1], rect[2], rect[3])
            line_edit.setObjectName(properties['object_name'])
            line_edit.setStyleSheet("background-color: rgb(239, 239, 239);")
            line_edit.setAlignment(Qt.AlignCenter | Qt.AlignHCenter)

            self.profile_line_edits[key] = line_edit
