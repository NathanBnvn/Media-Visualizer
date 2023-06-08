from PySide6 import QtWidgets, QtGui, QtCore

# from .style import StyleTheme

class HomeView(QtWidgets.QWidget):
    def __init__(self, home_controller):
        super().__init__()
        self.home_controller = home_controller
        self.setWindowTitle("Media Visualizer - Home")
        self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.show()
    
    def setup_ui(self):
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_body = self._setup_body_ui()
        self.layout_header = self._setup_header_ui()

        self.layout_main.addLayout(self.layout_header)
        self.layout_main.addLayout(self.layout_body)

        self.setLayout(self.layout_main)
    
    def _setup_header_ui(self):
        self.frame_header = QtWidgets.QFrame()
        self.layout_header = QtWidgets.QVBoxLayout()
        self.layout_main_header = QtWidgets.QVBoxLayout()

        self.label_username = QtWidgets.QLabel("User pseudo")
        self.layout_action = QtWidgets.QHBoxLayout()
        self.button_add_folder = QtWidgets.QPushButton()
        self.button_show_filter = QtWidgets.QPushButton()
        self.button_show_hierarchy = QtWidgets.QPushButton()
        self.button_edit_profile = QtWidgets.QPushButton("Edit profile")
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setClearButtonEnabled(True)

        self.button_add_folder.setIcon(QtGui.QIcon("media/plus_icon.svg"))
        self.button_show_filter.setIcon(QtGui.QIcon("media/filter_icon.svg"))
        self.button_show_hierarchy.setIcon(QtGui.QIcon("media/hierarchy_icon.svg"))

        self.layout_header.addWidget(self.label_username)
        self.layout_action.addWidget(self.button_add_folder)
        self.layout_action.addWidget(self.button_show_filter)
        self.layout_action.addWidget(self.button_show_hierarchy)
        self.layout_action.addWidget(self.button_edit_profile, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_action.addWidget(self.search_bar)
        self.layout_header.addLayout(self.layout_action)
        self.frame_header.setLayout(self.layout_header)
        self.layout_main_header.addWidget(self.frame_header)

        return self.layout_main_header


    def _setup_body_ui(self):
        self.layout_body = QtWidgets.QGridLayout()
        return self.layout_body

    def setup_css(self):
        self.setStyleSheet("background-color: gray")
        # rgb(21, 3, 39)
        self._setup_header_css()

    def _setup_header_css(self):
        frame_style = """
            border: none;
            border-bottom: 1px solid red;
        """
        label_username_style = """
            border: none;
            color: white;
        """
        round_button_style = """
            border: 1px solid red;
            border-radius: 13px;
            border-style: outset;
            width: 35px;
            height: 35px;
        """
        edit_button_style = """
            background-color: none;
            padding: 5px 35px;
            border: 1px solid red;
            border-radius: 10px;
            color: red;
            max-width: 200px;
        """
        search_bar_style = """
            background-color: rgb(29, 13, 46);
            padding: 5px 10px;
            border: 1px solid red;
            border-radius: 10px;
            max-width: 350px
        """
        self.frame_header.setStyleSheet(frame_style)
        self.setMinimumSize(QtCore.QSize(700, 500))

        self.label_username.setStyleSheet(label_username_style)
        self.label_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.button_add_folder.setStyleSheet(round_button_style)
        self.button_show_filter.setStyleSheet(round_button_style)
        self.button_show_hierarchy.setStyleSheet(round_button_style)
        self.button_edit_profile.setStyleSheet(edit_button_style)
        self.search_bar.setStyleSheet(search_bar_style)

        self.layout_main_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)


    def setup_connection(self):
        pass
