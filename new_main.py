import sys
from PyQt5 import QtWidgets
from ui.base_ui import BaseUI
from ui.system_ui import SystemUI
from ui.resurrection_ui import ResurrectionUI
from ui.keyboard_ui import KeyboardUI
from ui.interface_ui import InterfaceUI
from ui.profile_ui import ProfileUI


class MainApp(BaseUI, SystemUI, ResurrectionUI, KeyboardUI, InterfaceUI, ProfileUI):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setup_ui(self.MainWindow)
        self.add_widgets(self.central_widget)

    def add_widgets(self, parent):
        self.create_resurrection_widgets(parent)
        self.create_keyboard_left_line_edits(parent)
        self.create_keyboard_left_check_boxes(parent)
        self.create_keyboard_right_line_edits(parent)
        self.create_keyboard_right_check_boxes(parent)
        self.create_interface_widgets(parent)
        self.create_hottime_widgets(parent)
        self.create_profile_buttons(parent)
        self.create_profile_widgets(parent)
        self.create_profile_line_edits(parent)

    def run(self):
        self.MainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.run()
    sys.exit(app.exec_())
