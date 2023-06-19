from typing import Optional
from PySide6 import QtWidgets, QtGui, QtCore
import PySide6.QtCore
import PySide6.QtWidgets


class AllMediaFolder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.folder_widget = self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.setLayout(self.folder_widget)

    def setup_ui(self):
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_second = QtWidgets.QHBoxLayout()
        self.label_image_first = QtWidgets.QLabel()
        self.label_image_second = QtWidgets.QLabel()
        self.label_image_third = QtWidgets.QLabel()
        self.label_image_fourth = QtWidgets.QLabel()
        self.label_image_fifth = QtWidgets.QLabel()

        self.label_title = QtWidgets.QLabel("All files")

        self.layout_second.addWidget(self.label_image_first)
        self.layout_second.addWidget(self.label_image_second)
        self.layout_second.addWidget(self.label_image_third)
        self.layout_second.addWidget(self.label_image_fourth)
        self.layout_second.addWidget(self.label_image_fifth)

        self.layout_main.addLayout(self.layout_second)
        self.layout_main.addWidget(self.label_title)

        return self.layout_main
    
    def setup_css(self):
        line_style_1 = """
            border: 1px solid red;
        """
        label_title_style = """
            color: white;
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
        self.layout_second.setSpacing(0)
    
    def setup_connection(self):
        pass


class MediaFolder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.folder_widget = self.setup_ui()
        self.setup_css()
        self.setLayout(self.folder_widget)
    
    def setup_ui(self):
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_top = QtWidgets.QHBoxLayout()
        self.layout_second = QtWidgets.QVBoxLayout()
        self.label_image_first = QtWidgets.QLabel()
        self.label_image_second = QtWidgets.QLabel()
        self.label_image_third = QtWidgets.QLabel()
        self.label_title = QtWidgets.QLabel("test")

        self.layout_top.addWidget(self.label_image_first)
        self.layout_second.addWidget(self.label_image_second)
        self.layout_second.addWidget(self.label_image_third)
        self.layout_top.addLayout(self.layout_second)
        self.layout_main.addLayout(self.layout_top)
        self.layout_main.addWidget(self.label_title)
        return self.layout_main

    def setup_css(self):
        line_style_1 = """
            border: 1px solid white;
        """
        label_title_style = """
            color: white;
        """
        self.label_title.setStyleSheet(label_title_style)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setMaximumHeight(36)
        self.label_image_first.setStyleSheet(line_style_1)
        self.label_image_second.setStyleSheet(line_style_1)
        self.label_image_third.setStyleSheet(line_style_1)

        self.layout_main.setSpacing(0)
        self.layout_second.setSpacing(0)
    
    def setup_connection(self):
        pass


class MediaSubfolder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.subfolder_widget = self.setup_ui()
        self.setup_css()
        self.setLayout(self.subfolder_widget)
    
    def setup_ui(self):
        self.layout_main = QtWidgets.QVBoxLayout()
        self.layout_second = QtWidgets.QHBoxLayout()

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
        self.label_title = QtWidgets.QLabel("title")

        self.layout_main.addWidget(self.label_image_first)
        self.layout_second.addWidget(self.label_image_second)
        self.layout_second.addWidget(self.label_image_third)
        self.layout_second.addWidget(self.label_image_fourth)
        self.layout_second.addWidget(self.label_image_fifth)
        self.layout_main.addLayout(self.layout_second)
        self.layout_main.addWidget(self.label_title)

        return self.layout_main
    
    def setup_css(self):
        line_style_1 = """
            border: 1px solid red;
        """

        label_title_style = """
            color: white;
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
        self.layout_second.setSpacing(0)

    def setup_connection(self):
        pass