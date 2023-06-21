from view.home import HomeView

class HomeController:
    def __init__(self):
        super().__init__()

        self.view = HomeView(self)
    
    def close_menu(self):
        self.view._setup_menu_ui.move(200, 300)