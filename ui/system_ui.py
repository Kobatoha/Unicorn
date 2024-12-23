from PyQt5.QtWidgets import QPushButton


class SystemUI:
    def __init__(self):
        self.stop_button = None
        self.start_button = None

    def create_system_buttons(self, parent):

        self.pushButton_startstop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_startstop.setGeometry(QtCore.QRect(100, 490, 40, 40))
        self.pushButton_startstop.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_startstop.setFont(font)
        self.pushButton_startstop.setObjectName("pushButton_startstop")
        self.pushButton_startstop.setText('Start')
        self.pushButton_startstop.clicked.connect(self.startstop)

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
        self.pushButton_located = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_located.setGeometry(QtCore.QRect(30, 490, 41, 41))
        self.pushButton_located.setStyleSheet("background-color: rgb(255, 239, 220);")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_located.setFont(font)
        self.pushButton_located.setObjectName("pushButton_located")
        self.pushButton_located.setIcon(QtGui.QIcon('images/target_off.png'))
        self.pushButton_located.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_located.clicked.connect(self.get_window_id)

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
