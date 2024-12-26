from PyQt5.QtWidgets import QPushButton, QLabel, QSystemTrayIcon
from PyQt5.QtGui import QFont, QIcon


class SystemUI:
    def __init__(self):
        self.msg_box_active = False
        self.tray_icon = None
        self.system_buttons = None
        self.system_labels = None

    def create_system_buttons(self, parent):

        button_font = QFont()
        button_font.setPointSize(10)
        button_font.setBold(True)
        button_font.setWeight(75)

        system_buttons = {
            'startstop': {
                'object_name': 'startstop',
                'rect': [100, 490, 40, 40],
                'text': 'Start',
                'icon': '',
                'icon_size': None
            },
            'locate': {
                'object_name': 'locate',
                'rect': [30, 490, 41, 41],
                'text': '',
                'icon': 'resources/images/target_off.png',
                'icon_size': [40, 40]
            }
        }

        self.system_buttons = {}

        for key, properties in system_buttons.items():
            button = QPushButton(parent)
            rect = properties['rect']
            button.setGeometry(rect[0], rect[1], rect[2], rect[3])
            button.setFont(button_font)
            button.setObjectName(properties['object_name'])
            button.setText(properties['text'])
            button.setIcon(properties['icon'])
            button.setIconSize(properties['icon_size'])
            button.setStyleSheet("background-color: rgb(255, 239, 220);")

            self.system_buttons[key] = button

    def create_system_widgets(self, parent):

        font = QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)

        system_labels = {
            'label_startstop': {'object_name': 'label_startstop', 'rect': [95, 530, 50, 21], 'text': 'INSERT'},
            'label_hwnd': {'object_name': 'label_hwnd', 'rect': [25, 530, 50, 21], 'text': ''},
        }

        self.system_labels = {}

        for key, properties in system_labels.items():
            label = QLabel(parent)
            rect = properties['rect']
            label.setGeometry(rect[0], rect[1], rect[2], rect[3])
            label.setObjectName(properties['object_name'])
            label.setText(properties['text'])
            label.setFont(font)
            label.setStyleSheet("background: none;")

            self.system_labels[key] = label

        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon("resources/images/icon_off.png"))

        self.lineEdit_window_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_window_id.setGeometry(QtCore.QRect(40, 460, 90, 20))
        self.lineEdit_window_id.setObjectName("lineEdit_window_id")
        self.lineEdit_window_id.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.lineEdit_window_id.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)

    def add_system_widgets(self, parent):
        self.create_system_buttons(parent)
