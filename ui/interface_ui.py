from PyQt5.QtWidgets import QLabel, QFrame
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt


class InterfaceUI:
    def __init__(self):
        self.hottime_labels = None
        self.interface_labels = None
        self.interface_frames = None

    def create_interface_widgets(self, parent):
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setPointSize(7)

        interface_frames = {
            'line_tuning_keys_1': {'object_name': 'line_tuning_keys_1', 'rect': [69, 0, 81, 20]},
            'line_tuning_keys_2': {'object_name': 'line_tuning_keys_2', 'rect': [170, 0, 111, 20]},
            # 'line_half_window': {'object_name': 'line_half_window', 'rect': [150, 20, 20, 300]},
            'line_icons_1': {'object_name': 'line_icons_1', 'rect': [50, 370, 101, 20]},
            'line_icons_2': {'object_name': 'line_icons_2', 'rect': [170, 370, 111, 20]},
        }

        self.interface_frames = {}

        for key, properties in interface_frames.items():
            frame = QFrame(parent)
            rect = properties['rect']
            frame.setGeometry(rect[0], rect[1], rect[2], rect[3])
            frame.setObjectName(properties['object_name'])
            frame.setFrameShape(QFrame.HLine)
            frame.setFrameShadow(QFrame.Sunken)
            frame.setStyleSheet("background: none;")

            self.interface_frames[key] = frame

        interface_labels = {
            'label_tuning_keys': {'object_name': 'label_tuning_keys', 'rect': [10, 0, 61, 16], 'text': 'Tuning keys'},
            'label_icons': {'object_name': 'label_icons', 'rect': [10, 370, 41, 16], 'text': 'Icons'},
            'label_information_actions': {
                'object_name': 'label_information_actions',
                'rect': [50, 550, 201, 16],
                'text': 'information'
            },
        }

        self.interface_labels = {}

        for key, properties in interface_labels.items():
            label = QLabel(parent)
            rect = properties['rect']
            label.setGeometry(rect[0], rect[1], rect[2], rect[3])
            label.setObjectName(properties['object_name'])
            label.setFont(font)
            label.setStyleSheet("background: none;")
            label.setAlignment(Qt.AlignCenter)
            label.setText(properties['text'])

            self.interface_labels[key] = label

    def create_hottime_widgets(self, parent):
        font = QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)

        interface_labels = {
            'label_hottime': {
                'object_name': 'label_hottime',
                'rect': [20, 390, 31, 31],
                'text': None,
                'pixmap': 'resources/images/hot_time_off.png'
            },
            'label_hottime_2': {
                'object_name': 'label_hottime_2',
                'rect': [10, 420, 51, 16],
                'text': 'Hot Time',
                'pixmap': None
            },
        }

        self.hottime_labels = {}

        for key, properties in interface_labels.items():
            label = QLabel(parent)
            rect = properties['rect']
            label.setGeometry(rect[0], rect[1], rect[2], rect[3])
            label.setPixmap(QPixmap(properties['pixmap']))
            label.setObjectName(properties['object_name'])
            label.setFont(font)
            label.setStyleSheet("background: none;")
            label.setAlignment(Qt.AlignCenter)
            label.setScaledContents(True)
            label.setText(properties['text'])

            self.hottime_labels[key] = label
