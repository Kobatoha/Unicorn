from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont


class SystemUI:
    def __init__(self):
        self.system_buttons = None

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
                'icon': None,
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

    def create_system_widgets(self, parent):

        self.label_hotkey_startstop = QtWidgets.QLabel(self.centralwidget)
        self.label_hotkey_startstop.setGeometry(QtCore.QRect(95, 530, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_hotkey_startstop.setFont(font)
        self.label_hotkey_startstop.setAlignment(QtCore.Qt.AlignCenter)
        self.label_hotkey_startstop.setObjectName("label_hotkey_startstop")
        self.label_hotkey_startstop.setText('INSERT')
        self.label_hotkey_startstop.setStyleSheet("background: none;")

        self.tray_icon = QtWidgets.QSystemTrayIcon()
        self.tray_icon.setIcon(QtGui.QIcon("images/icon_off.png"))

        # Отображаем иконку
        self.tray_icon.show()

        ### button lockated ###


        self.msg_box_active = False

        self.label_id_window = QtWidgets.QLabel(self.centralwidget)
        self.label_id_window.setGeometry(QtCore.QRect(25, 530, 50, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_id_window.setFont(font)
        self.label_id_window.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_window.setObjectName("label_id_window")
        self.label_id_window.setText("")
        self.label_id_window.setStyleSheet("background: none;")

        self.lineEdit_window_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_window_id.setGeometry(QtCore.QRect(40, 460, 90, 20))
        self.lineEdit_window_id.setObjectName("lineEdit_window_id")
        self.lineEdit_window_id.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.lineEdit_window_id.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignHCenter)
