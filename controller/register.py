from PySide6 import QtWidgets, QtGui, QtCore
from view.register import RegisterView

class RegisterController(QtWidgets.QWidget):
    def __init__(self, main):
        super().__init__()

        self.view = RegisterView(self)
        self.main = main
    
    def back_to_login(self):
        self.main._to_page(1, False)

    def select_profile_picture(self):
        QtWidgets.QFileDialog.getOpenFileName(self, "Select picture", "c:\\desktop", "All FIles(*) ;; Images(*.jpeg)")

    def sign_up(self):
        print("3")