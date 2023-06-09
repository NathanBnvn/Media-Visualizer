from PySide6 import QtWidgets, QtGui, QtCore

class SplashView(QtWidgets.QWidget):
    def __init__(self, loader_controller):
        super().__init__()

        self.loader_controller = loader_controller