from pathlib import Path

class StyleTheme:
    def __init__(self):
        super().__init__()

        self.path = Path(__file__).resolve().parent / 'media'
        self.primary_color = "rgb(21, 3, 39)"
        self.secondary_color = "rgb(29, 13, 46)"
        self.terciary_color = "red"
        print(self.path)
    
    def set_theme(self):


        pass
