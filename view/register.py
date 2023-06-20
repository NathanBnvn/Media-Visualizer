from PySide6 import QtWidgets, QtGui, QtCore

class RegisterView(QtWidgets.QWidget):
    def __init__(self, register_controller):
        super().__init__()

        self.register_controller = register_controller
        self.setWindowTitle("Media Visualizer - Sign up")
        self.setup_ui()
        self.setup_css()
        self.setup_connection()
        self.show()


    def setup_ui(self):
        self.layout_main = QtWidgets.QVBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()
        
        self.button_back_to_login = QtWidgets.QPushButton()
        self.button_back_to_login.setIcon(QtGui.QIcon("media/return_icon.svg"))
        self.button_back_to_login.setIconSize(QtCore.QSize(15, 15))
        
        self.button_add_picture = QtWidgets.QPushButton()
        self.line_edit_mail = QtWidgets.QLineEdit()
        self.line_edit_mail.setPlaceholderText("Mail address")
        self.line_edit_confirm_password = QtWidgets.QLineEdit()
        self.line_edit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password) # type: ignore
        self.line_edit_confirm_password.setPlaceholderText("Confirm password")
        self.button_signup = QtWidgets.QPushButton("Sign up")

        self.form_layout.addWidget(self.button_add_picture)
        self.form_layout.addWidget(self.line_edit_mail)
        self.form_layout.addWidget(self.line_edit_confirm_password)
        self.form_layout.addWidget(self.button_signup)

        self.layout_main.addWidget(self.button_back_to_login)
        self.layout_main.addLayout(self.form_layout)
        self.layout_main.setSpacing(0)

        self.setLayout(self.layout_main)
        return self.layout_main


    def setup_css(self):
        register_widget_style = """
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
        line_edit_style = """
            height: 35px;
            border: none;
            border-radius: 10px;
            background-color: rgb(36, 19, 53);
            padding-left: 10px;
        """
        self.setStyleSheet(register_widget_style)
        self.setMinimumSize(QtCore.QSize(700, 500))

        self.button_back_to_login.setFixedSize(25, 25)
        self.line_edit_mail.setStyleSheet(line_edit_style)
        self.line_edit_confirm_password.setStyleSheet(line_edit_style)
        self.button_signup.setStyleSheet(button_style)

        self.line_edit_mail.setFixedWidth(420)
        self.line_edit_confirm_password.setFixedWidth(420)
    
        self.form_layout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def setup_connection(self):
        self.button_back_to_login.clicked.connect(self.register_controller.back_to_login)
        self.button_add_picture.clicked.connect(self.register_controller.select_profile_picture)
        self.button_signup.clicked.connect(self.register_controller.sign_up)
