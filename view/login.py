from PySide6 import QtWidgets, QtGui, QtCore

class LogInView(QtWidgets.QWidget):
    def __init__(self, login_controller):
        super().__init__()
        self.login_controller = login_controller
        self.setWindowTitle("Media Visualizer")
        self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.show()


    def setup_ui(self):
        self.form_layout =  QtWidgets.QFormLayout()
        self.setLayout(self.form_layout)
        
        self.label_title = QtWidgets.QLabel("Media Visualizer")
        self.line_edit_username = QtWidgets.QLineEdit()
        self.line_edit_username.setPlaceholderText("Username")
        self.line_edit_password = QtWidgets.QLineEdit()
        self.line_edit_password.setPlaceholderText("Password")
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.button_register = QtWidgets.QPushButton("Sign Up")
        self.button_login = QtWidgets.QPushButton("Sign In")

        self.layout_buttons.addWidget(self.button_register)
        self.layout_buttons.addWidget(self.button_login)
        
        self.form_layout.addRow(self.label_title)
        self.form_layout.addRow(self.line_edit_username)
        self.form_layout.addRow(self.line_edit_password)
        self.form_layout.addRow(self.layout_buttons)


    def setup_css(self):
        login_widget_style = """
            background-color: rgb(21, 3, 39);
            color: rgb(240, 240, 240);
        """
        title_style = """
        """
        button_style = """
            border: 1px solid white;
            border-radius: 10px;
            height: 30px;
            max-width: 200px;
            min-width: 200px;
        """
        line_edit_style = """
            height: 35px;
            border: none;
            border-radius: 10px;
            border-bottom: 5px;
            background-color: rgb(36, 19, 53);
            padding-left: 10px;
        """
        self.setStyleSheet(login_widget_style)
        self.setMinimumSize(QtCore.QSize(700, 500))

        self.label_title.setStyleSheet(title_style)
        self.line_edit_username.setStyleSheet(line_edit_style)
        self.line_edit_password.setStyleSheet(line_edit_style)
        self.button_login.setStyleSheet(button_style)
        self.button_register.setStyleSheet(button_style)

        self.label_title.setFont(QtGui.QFont("Good Timing", 35))
        self.label_title.setFixedWidth(400)
        self.line_edit_username.setFixedWidth(420)
        self.line_edit_password.setFixedWidth(420)
        self.button_register.setFixedWidth(300)
    
        self.form_layout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_title.setMargin(50)
        self.layout_buttons.setContentsMargins(0, 50, 0, 50)


    def setup_connection(self):
        self.button_login.clicked.connect(self.login_controller.login)
        self.button_register.clicked.connect(self.login_controller.register)
