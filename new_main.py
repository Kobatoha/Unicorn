import sys
from PyQt5 import QtWidgets
from ui.base_ui import BaseUI
from ui.system_ui import SystemUI
from ui.resurrection_ui import ResurrectionUI
from ui.keyboard_ui import KeyboardUI
from ui.interface_ui import InterfaceUI


class MainApp(BaseUI, SystemUI, ResurrectionUI, KeyboardUI, InterfaceUI):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setup_ui(self.MainWindow)
        self.add_widgets(self.central_widget)

    def add_widgets(self, parent):
        self.add_resurrection_widgets(parent)
        self.add_keyboard_left_line_edits(parent)
        self.add_keyboard_left_check_boxes(parent)
        self.add_keyboard_right_line_edits(parent)
        self.add_keyboard_right_check_boxes(parent)
        self.add_interface_widgets(parent)
        self.add_hottime_widgets(parent)

    def run(self):
        self.MainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.run()
    sys.exit(app.exec_())
