from PySide6 import QtWidgets, QtGui, QtCore
from view.register import RegisterView

class RegisterController(QtWidgets.QWidget):
    def __init__(self, main):
        super().__init__()

        self.view = RegisterView(self)
        self.main = main
    
    def back_to_login(self):
        # if there is a mistake user can go back
        # or I create field with data alrealdy fill in
        # from the login page
        # or I can do both...
        print('🤔')

    def select_profile_picture(self):
        QtWidgets.QFileDialog.getOpenFileName(self, "Select picture", "c:\\desktop", "All Images")

    def sign_up(self):
        print("3")