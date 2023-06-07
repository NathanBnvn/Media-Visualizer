from PySide6 import QtWidgets

from .login import LogInController
from .home import HomeController

class MainController:
    def __init__(self):
        super().__init__()

        self.login = LogInController(self)
        self.home = HomeController()
        
        self.main_layout = QtWidgets.QVBoxLayout()
        self.stacked_layout = QtWidgets.QStackedLayout()

        self.stacked_layout.addWidget(self.login.view)
        self.stacked_layout.addWidget(self.home.view)
        self.main_layout.addLayout(self.stacked_layout)
    
    def _enter_the_app(self):
        self.stacked_layout.setCurrentIndex(self.stacked_layout.currentIndex()+1)