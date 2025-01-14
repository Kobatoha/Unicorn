from PyQt5 import QtCore, QtGui, QtWidgets


class BaseUI:
    def __init__(self, main_setup):
        self.central_widget = None
        self.main_setup = main_setup

    def setup_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowTitle("Unicorn")
        main_window.setWindowIcon(QtGui.QIcon("resources/images/unicorn.png"))
        main_window.resize(380, 600)
        main_window.setMinimumSize(QtCore.QSize(165, 380))
        main_window.setMaximumSize(QtCore.QSize(380, 600))
        main_window.setStyleSheet("background-image: url('resources/images/bg_image.jpg');")

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        main_window.setCentralWidget(self.central_widget)
