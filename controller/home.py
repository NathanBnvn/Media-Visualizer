from view.home import HomeView

class HomeController:
    def __init__(self):
        super().__init__()

        self.view = HomeView(self)
        pass