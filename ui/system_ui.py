from PyQt5.QtWidgets import QPushButton


class SystemUI:
    def __init__(self):
        self.stop_button = None
        self.start_button = None

    def add_system_buttons(self, parent):
        self.start_button = QPushButton(parent)
        self.start_button.setText("Start")
        self.start_button.setGeometry(10, 10, 100, 30)

        self.stop_button = QPushButton(parent)
        self.stop_button.setText("Stop")
        self.stop_button.setGeometry(120, 10, 100, 30)
