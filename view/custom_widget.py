from PySide6 import QtWidgets, QtGui, QtCore


class AllImageWidget(QtWidgets.QWidget):
    def __init__(self, QtWidgets):
        super().__init__()

    def setup_ui(self):
        pass



class CategoryWidget(QtWidgets.QWidget):
    def __init__(self, QtWidgets):
        super().__init__()

        self.setup_ui()
        self.setup_css()
    
    def setup_ui(self):
        self.layout_category = QtWidgets.QHBoxLayout()
        self.layout_second = QtWidgets.QVBoxLayout()
        self.label_primary_image = QtWidgets.QLabel()
        self.label_second_image = QtWidgets.QLabel()
        self.label_third_image = QtWidgets.QLabel()

        self.layout_category.addWidget(self.label_primary_image)
        self.layout_second.addWidget(self.label_second_image)
        self.layout_second.addWidget(self.label_third_image)
        self.layout_category.addLayout(self.layout_second)
        return self.layout_category

    def setup_css(self):
        line_style_1 = """
            border: 1px solid red;
        """

        self.label_primary_image.setStyleSheet(line_style_1)
        self.label_second_image.setStyleSheet(line_style_1)
        self.label_third_image.setStyleSheet(line_style_1)

        self.label_primary_image.setFixedWidth(140)
        self.label_primary_image.setFixedHeight(140)
        self.label_second_image.setFixedWidth(90)
        self.label_second_image.setFixedHeight(70)
        self.label_third_image.setFixedWidth(90)
        self.label_third_image.setFixedHeight(70)

        self.layout_category.setSpacing(0)
        self.layout_second.setSpacing(0)