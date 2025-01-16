from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QFont


class TeleportUI:
    def __init__(self):
        self.teleport_check_boxes = None

    def create_teleport_check_boxes(self, parent):
        check_box_font = QFont()
        check_box_font.setBold(True)
        check_box_font.setWeight(75)

        teleport_check_boxes = {
            'night_teleport': {
                'object_name': 'check_box_night_teleport',
                'rect': [100, 350, 40, 20],
                'text': 'TP5',
                'tool_tip': 'Летает на свободный телепорт каждые 12 минут. '
                            'Свободный телепорт должен быть на F7, F8, F9, F10, F11',
                'disabled': False
            },
            'night_teleport_solo': {
                'object_name': 'check_box_night_teleport_solo',
                'rect': [100, 320, 40, 20],
                'text': 'TP1',
                'tool_tip': 'Летает на свободный телепорт каждые 12 минут. '
                            'Свободный телепорт должен быть на F11',
                'disabled': False
            }
        }

        self.teleport_check_boxes = {}

        for key, properties in teleport_check_boxes.items():
            check_box = QCheckBox(parent)
            rect = properties['rect']
            check_box.setGeometry(rect[0], rect[1], rect[2], rect[3])
            check_box.setFont(check_box_font)
            check_box.setObjectName(properties['object_name'])
            check_box.setText(properties['text'])
            check_box.setStyleSheet("background: none;")
            check_box.setDisabled(properties['disabled'])
            check_box.setToolTip(properties['tool_tip'])

            self.teleport_check_boxes[key] = check_box

    def add_teleport_widgets(self, parent):
        self.create_teleport_check_boxes(parent)
