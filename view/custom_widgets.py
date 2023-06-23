from typing import Optional
from PySide6 import QtWidgets, QtGui, QtCore


class AllMediaFolder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.folder_widget = self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.setLayout(self.folder_widget)

    def setup_ui(self):
        self.layout_main = QtWidgets.QGridLayout()
        self.label_image_first = QtWidgets.QLabel()
        self.label_image_second = QtWidgets.QLabel()
        self.label_image_third = QtWidgets.QLabel()
        self.label_image_fourth = QtWidgets.QLabel()
        self.label_image_fifth = QtWidgets.QLabel()

        self.label_title = QtWidgets.QLabel("All files")

        self.layout_main.addWidget(self.label_image_first, 0, 0)
        self.layout_main.addWidget(self.label_image_second, 0, 1)
        self.layout_main.addWidget(self.label_image_third, 0, 2)
        self.layout_main.addWidget(self.label_image_fourth, 0, 3)
        self.layout_main.addWidget(self.label_image_fifth, 0, 4)
        self.layout_main.addWidget(self.label_title, 1, 0, 1, 5)

        return self.layout_main
    
    def setup_css(self):
        line_style_1 = """
            border: 1px solid white;
        """
        label_title_style = """
            color: red;
        """
        self.label_title.setStyleSheet(label_title_style)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setMaximumHeight(36)
        self.label_image_first.setStyleSheet(line_style_1)
        self.label_image_second.setStyleSheet(line_style_1)
        self.label_image_third.setStyleSheet(line_style_1)
        self.label_image_fourth.setStyleSheet(line_style_1)
        self.label_image_fifth.setStyleSheet(line_style_1)

        self.layout_main.setSpacing(0)
    
    def setup_connection(self):
        pass


class Board(QtWidgets.QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.title = title

        self.folder_widget = self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.setLayout(self.folder_widget)
    
    def setup_ui(self):
        self.layout_main = QtWidgets.QGridLayout()
        self.label_image_first = QtWidgets.QLabel()
        self.label_image_second = QtWidgets.QLabel()
        self.label_image_third = QtWidgets.QLabel()
        self.label_title = QtWidgets.QLabel(self.title)

        self.layout_main.addWidget(self.label_image_first, 0, 0, 2, 2)
        self.layout_main.addWidget(self.label_image_second, 0, 2)
        self.layout_main.addWidget(self.label_image_third, 1, 2)
        self.layout_main.addWidget(self.label_title, 2, 0, 1, 3)
        
        return self.layout_main

    def setup_css(self):
        line_style_1 = """
            border: 1px solid white;
            border-top-left-radius: 35px;
            border-bottom-left-radius: 35px;
        """
        line_style_2 = """
            border: 1px solid white;
            border-top-right-radius: 35px;
        """
        line_style_3 = """
            border: 1px solid white;
            border-bottom-right-radius: 35px;
        """
        label_title_style = """
            color: white;
        """
        self.label_title.setStyleSheet(label_title_style)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setMaximumHeight(36)
        self.label_image_first.setStyleSheet(line_style_1)
        self.label_image_second.setStyleSheet(line_style_2)
        self.label_image_third.setStyleSheet(line_style_3)

        self.layout_main.setSpacing(0)
    
    def setup_connection(self):
        #self.label_image_first.mousePressEvent = 
        #self.label_image_second.mousePressEvent = 
        #self.label_image_third.mousePressEvent = 
        pass


class Folder(QtWidgets.QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.title = title

        self.subfolder_widget = self.setup_ui()
        self.setup_css()
        self.setLayout(self.subfolder_widget)
    
    def setup_ui(self):
        self.layout_main = QtWidgets.QGridLayout()

        self.label_image_first = QtWidgets.QLabel()
        # self.pixmap_first = QtGui.QPixmap()
        # self.label_image_first.setPixmap(self.pixmap_first)
        self.label_image_second = QtWidgets.QLabel()
        # self.pixmap_second = QtGui.QPixmap()
        # self.label_image_second.setPixmap(self.pixmap_second)
        self.label_image_third = QtWidgets.QLabel()
        # self.pixmap_third = QtGui.QPixmap()
        # self.label_image_third.setPixmap(self.pixmap_third)
        self.label_image_fourth = QtWidgets.QLabel()
        # self.pixmap_fourth = QtGui.QPixmap()
        # self.label_image_fourth.setPixmap(self.pixmap_fourth)
        self.label_image_fifth = QtWidgets.QLabel()
        # self.pixmap_fifth = QtGui.QPixmap()
        # self.label_image_fifth.setPixmap(self.pixmap_fifth)
        self.label_title = QtWidgets.QLabel(self.title)

        self.layout_main.addWidget(self.label_image_first, 0, 0, 2, 4)
        self.layout_main.addWidget(self.label_image_second, 3, 0)
        self.layout_main.addWidget(self.label_image_third, 3, 1)
        self.layout_main.addWidget(self.label_image_fourth, 3, 2)
        self.layout_main.addWidget(self.label_image_fifth, 3, 3)
        self.layout_main.addWidget(self.label_title, 4, 0, 1, 4)

        return self.layout_main
    
    def setup_css(self):
        line_style_1 = """
            border: 1px solid white;
            border-top-right-radius: 35px;
            border-top-left-radius: 35px;
        """
        line_style_2 = """
            border: 1px solid white;
            border-bottom-left-radius: 35px;
        """
        line_style_3 = """
            border: 1px solid white;
            border-bottom-right-radius: 35px;
        """
        line_style_4 = """
            border: 1px solid white;
        """
        label_title_style = """
            color: white;
        """
        self.label_title.setStyleSheet(label_title_style)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setMaximumHeight(36)
        self.label_image_first.setStyleSheet(line_style_1)
        self.label_image_second.setStyleSheet(line_style_2)
        self.label_image_third.setStyleSheet(line_style_4)
        self.label_image_fourth.setStyleSheet(line_style_4)
        self.label_image_fifth.setStyleSheet(line_style_3)

        self.layout_main.setSpacing(0)


    def setup_connection(self):
        pass


class Section(QtWidgets.QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.title = title
        self.folder = self.setup_ui()
        self.setup_css()
        self.setLayout(self.folder)
    
    def setup_ui(self):
        self.layout_main = QtWidgets.QGridLayout()
        self.label_image_first = QtWidgets.QLabel()
        self.label_image_second = QtWidgets.QLabel()
        self.label_image_third = QtWidgets.QLabel()
        self.label_title = QtWidgets.QLabel(self.title)

        self.layout_main.addWidget(self.label_image_first, 0, 0)
        self.layout_main.addWidget(self.label_image_second, 0, 1)
        self.layout_main.addWidget(self.label_image_third, 0, 2)
        self.layout_main.addWidget(self.label_title, 1, 0, 1, 3)

        return self.layout_main

    def setup_css(self):
        line_style_1 = """
            border: 1px solid white;
            border-top-left-radius: 35px;
            border-bottom-left-radius: 35px;
        """
        line_style_2 = """
            border: 1px solid white;
        """
        line_style_3 = """
            border: 1px solid white;
            border-top-right-radius: 35px;
            border-bottom-right-radius: 35px;
        """
        label_title_style = """
            color: white;
        """
        self.label_title.setStyleSheet(label_title_style)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setMaximumHeight(36)
        self.label_image_first.setStyleSheet(line_style_1)
        self.label_image_second.setStyleSheet(line_style_2)
        self.label_image_third.setStyleSheet(line_style_3)

        self.layout_main.setSpacing(0)


    def setup_connection(self):
        pass