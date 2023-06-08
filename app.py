from PySide6 import QtWidgets, QtCore
from controller.main import MainController

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.main = MainController()
        self.setLayout(self.main.main_layout)


if __name__=="__main__":
    app = QtWidgets.QApplication()
    win = App()
    app.exec()