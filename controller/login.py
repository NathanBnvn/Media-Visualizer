
from view.login import LogInView

class LogInController:
    def __init__(self, main):
        super().__init__()

        self.view = LogInView(self)
        self.main = main

    def login(self):
        # if username & password in database then
        # self.main._enter_the_app()
        # else show an error window 
        # that invite people to sign up
        # self.main._enter_the_app()
        pass
    
    def register(self):
        # if fields empty show message explaining
        # that the subscription start here 
        self.main._to_page(1, True)
    
    def access_to_home(self):
        self.main._to_page(2, True)