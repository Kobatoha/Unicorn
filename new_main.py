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
        self.create_widgets(self.central_widget)
        self.add_widgets(self.central_widget)

    def create_widgets(self, parent):
        self.create_resurrection_widgets(parent)
        self.create_interface_widgets(parent)
        self.create_hottime_widgets(parent)

    def add_widgets(self, parent):
        self.add_profile_widgets(parent)
        self.add_keyboard(parent)

    def load_setting(self):
        pass

    def run(self):
        self.MainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.run()
    sys.exit(app.exec_())
