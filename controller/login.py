
from view.login import LogInView

class LogInController:
    def __init__(self, main):
        super().__init__()

        self.view = LogInView(self)
        self.main = main

    def login(self):
        self.main._enter_the_app()
    
    def register(self):
        #self.main._enter_the_app()
        pass