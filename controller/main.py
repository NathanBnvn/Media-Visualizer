from PySide6 import QtWidgets, QtCore

from .login import LogInController
from .register import RegisterController
from .home import HomeController

class MainController:
    def __init__(self):
        super().__init__()

        self.login = LogInController(self)
        self.register = RegisterController(self)
        self.home = HomeController()
        
        self.main_layout = QtWidgets.QVBoxLayout()
        self.stacked_layout = QtWidgets.QStackedLayout()

        self.stacked_layout.addWidget(self.login.view)
        self.stacked_layout.addWidget(self.register.view)
        self.stacked_layout.addWidget(self.home.view)
        self.main_layout.addLayout(self.stacked_layout)


    def _to_page(self, page_stack:int, next: bool):
        if next:
            self.stacked_layout.setCurrentIndex(
                self.stacked_layout.currentIndex()+ page_stack
                )
        else:
            self.stacked_layout.setCurrentIndex(
                self.stacked_layout.currentIndex()- page_stack
            )
