from PySide6 import QtWidgets, QtGui, QtCore

class LogInView(QtWidgets.QWidget):
    def __init__(self, login_controller):
        super().__init__()
        self.login_controller = login_controller
        self.setWindowTitle("Media Visualizer - Sign in")
        self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.show()


    def setup_ui(self):
        self.form_layout =  QtWidgets.QFormLayout()
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.setLayout(self.form_layout)
        
        self.label_title = QtWidgets.QLabel("Media Visualizer")
        self.line_edit_username = QtWidgets.QLineEdit()
        self.line_edit_username.setPlaceholderText("Username")
        self.line_edit_password = QtWidgets.QLineEdit()
        self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password) # type: ignore
        self.line_edit_password.setPlaceholderText("Password")
        self.button_register = QtWidgets.QPushButton("Sign up")
        self.button_login = QtWidgets.QPushButton("Sign in")
        self.button_visitor = QtWidgets.QPushButton("Sign up later")

        self.layout_buttons.addWidget(self.button_register)
        self.layout_buttons.addWidget(self.button_login)
        
        self.form_layout.addRow(self.label_title)
        self.form_layout.addRow(self.line_edit_username)
        self.form_layout.addRow(self.line_edit_password)
        self.form_layout.addRow(self.layout_buttons)
        self.form_layout.addRow(self.button_visitor)

        return self.form_layout


    def setup_css(self):
        login_widget_style = """
            background-color: rgb(21, 3, 39);
            color: rgb(240, 240, 240);
        """
        button_style = """
            border: 1px solid white;
            border-radius: 10px;
            height: 30px;
            max-width: 120px;
            min-width: 120px;
        """
        button_visitor_style = """
            color: rgba(255, 255, 255, 0.6)
        """
        line_edit_style = """
            height: 35px;
            border: none;
            border-radius: 10px;
            background-color: rgb(36, 19, 53);
            padding-left: 10px;
        """
        self.setStyleSheet(login_widget_style)
        self.setMinimumSize(QtCore.QSize(700, 500))

        self.line_edit_username.setStyleSheet(line_edit_style)
        self.line_edit_password.setStyleSheet(line_edit_style)
        self.button_login.setStyleSheet(button_style)
        self.button_register.setStyleSheet(button_style)
        self.button_visitor.setStyleSheet(button_visitor_style)

        self.label_title.setFont(QtGui.QFont("Good Timing", 35))
        self.label_title.setFixedWidth(420)
        self.line_edit_username.setFixedWidth(420)
        self.line_edit_password.setFixedWidth(420)
        self.button_register.setFixedWidth(420)
        self.button_visitor.setFixedSize(80, 30)
    
        self.form_layout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label_title.setMargin(25)
        self.layout_buttons.setContentsMargins(0, 25, 0, 15)


    def setup_connection(self):
        self.button_login.clicked.connect(self.login_controller.login)
        self.button_register.clicked.connect(self.login_controller.register)
        self.button_visitor.clicked.connect(self.login_controller.access_to_home)
