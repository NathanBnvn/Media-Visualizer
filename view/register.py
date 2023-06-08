from PySide6 import QtWidgets, QtGui, QtCore

class RegisterView(QtWidgets.QWidget):
    def __init__(self, register_controller):
        super().__init__()

        self.register_controller = register_controller
        self.setWindowTitle("Media Visualizer - Sign Up")