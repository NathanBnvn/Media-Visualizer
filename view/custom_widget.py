from PySide6 import QtWidgets, QtGui, QtCore


class AllImageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def setup_ui(self):
        pass



class CategoryWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.setup_css()
    
    def setup_ui(self):
        self.layout_category = QtWidgets.QGridLayout()
        self.label_primary_image = QtWidgets.QLabel()
        self.label_second_image = QtWidgets.QLabel()
        self.label_third_image = QtWidgets.QLabel()

        self.layout_category.addWidget(self.label_primary_image)
        self.layout_category.addWidget(self.label_second_image)
        self.layout_category.addWidget(self.label_third_image)

    def setup_css(self):
        line_style = """
            border: 1px solid red;
        """
        self.label_primary_image.setStyleSheet(line_style)
        self.label_second_image.setStyleSheet(line_style)
        self.label_third_image.setStyleSheet(line_style)