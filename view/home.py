from PySide6 import QtWidgets, QtGui, QtCore
from pathlib import Path

# from .style import StyleTheme

class HomeView(QtWidgets.QWidget):
    def __init__(self, home_controller):
        super().__init__()
        self.home_controller = home_controller
        self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.show()


    def setup_ui(self):
        self.layout_window = QtWidgets.QHBoxLayout()
        self.layout_main = QtWidgets.QVBoxLayout()
        
        self.layout_header = self._setup_header_ui()
        self.layout_menu = self._setup_menu_ui()
        self.layout_body = self._setup_body_ui()

        self.layout_main.addLayout(self.layout_header)
        self.layout_main.addLayout(self.layout_body)

        # self.layout_window.addLayout(self.layout_menu)
        self.layout_window.addLayout(self.layout_main)
        self.layout_window.setContentsMargins(0, 10, 0, 10)
        self.setLayout(self.layout_window)


    def _setup_header_ui(self):
        self.layout_header = QtWidgets.QVBoxLayout()
        self.layout_action = QtWidgets.QHBoxLayout()

        self.label_username = QtWidgets.QLabel("User pseudo")
        self.button_add_folder = QtWidgets.QPushButton()
        self.button_show_filter = QtWidgets.QPushButton()
        self.button_show_hierarchy = QtWidgets.QPushButton()
        self.button_edit_profile = QtWidgets.QPushButton("Edit profile")
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setClearButtonEnabled(True)
        self.separator = QtWidgets.QFrame()
        self.separator.setFrameShape(QtWidgets.QFrame.HLine) # type: ignore

        self.button_add_folder.setIcon(QtGui.QIcon("media/plus_icon.svg"))
        self.button_show_filter.setIcon(QtGui.QIcon("media/filter_icon.svg"))
        self.button_show_hierarchy.setIcon(QtGui.QIcon("media/hierarchy_icon.svg"))

        self.layout_action.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout_header.addWidget(self.label_username)
        self.layout_action.addWidget(self.button_add_folder)
        self.layout_action.addWidget(self.button_show_filter)
        self.layout_action.addWidget(self.button_show_hierarchy)
        self.layout_action.addStretch()
        self.layout_action.addWidget(self.button_edit_profile)
        self.layout_action.addStretch()
        self.layout_action.addWidget(self.search_bar)
        self.layout_action.setContentsMargins(15, 0, 15, 0)
        self.layout_header.addLayout(self.layout_action)
        self.layout_header.addWidget(self.separator)

        return self.layout_header


    def _setup_menu_ui(self):
        self.layout_menu = QtWidgets.QHBoxLayout()
        self.layout_menu_content = QtWidgets.QVBoxLayout()
        # self.path = Path(__file__).resolve().parent
        #self.model = QtWidgets.QFileSystemModel()
        #self.model.setRootPath(QtCore.QDir(f"{self.path}").currentPath())
        #self.tree =  QtWidgets.QTreeView()
        #self.tree.setModel(self.model)
        
        self.line = QtWidgets.QFrame()
        self.line.setFrameShape(QtWidgets.QFrame.VLine) # type: ignore
        
        self.button_close = QtWidgets.QPushButton()
        
        self.layout_menu.addLayout(self.layout_menu_content)
        self.layout_menu.addWidget(self.button_close)
        self.layout_menu.addWidget(self.line)
        
        return self.layout_menu


    def _setup_body_ui(self):
        self.layout_body = QtWidgets.QGridLayout()
        self.image_folder_main_icon = QtWidgets.QLabel()
        self.image_folder_second_icon = QtWidgets.QLabel()
        self.image_folder_third_icon = QtWidgets.QLabel()
        return self.layout_body


    def setup_css(self):
        self.setStyleSheet("background-color: rgb(21, 3, 39)")
        self._setup_header_css()
        self._setup_menu_css()


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
            width: 25px;
            height: 25px;
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
            max-width: 200px;
        """
        self.setMinimumSize(QtCore.QSize(700, 500))
        self.layout_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.separator.setStyleSheet(frame_style)

        self.label_username.setStyleSheet(label_username_style)
        self.label_username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.button_add_folder.setStyleSheet(round_button_style)
        self.button_show_filter.setStyleSheet(round_button_style)
        self.button_show_hierarchy.setStyleSheet(round_button_style)
        self.button_edit_profile.setStyleSheet(edit_button_style)
        self.search_bar.setStyleSheet(search_bar_style)
    

    def _setup_menu_css(self):
        line_style = """
            border: none;
            border-right: 10px solid red;
        """
        self.line.setStyleSheet(line_style)


    def setup_connection(self):
        pass
