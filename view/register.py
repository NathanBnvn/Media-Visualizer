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
        self.form_layout = QtWidgets.QFormLayout()
        
        self.button_back_to_login = QtWidgets.QPushButton()
        self.button_add_picture = QtWidgets.QPushButton()
        self.line_edit_mail = QtWidgets.QLineEdit()
        self.line_edit_mail.setPlaceholderText("Mail adress")
        self.line_edit_confirm_password = QtWidgets.QLineEdit()
        self.line_edit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password) # type: ignore
        self.line_edit_confirm_password.setPlaceholderText("Confirm password")
        self.button_register = QtWidgets.QPushButton("Sign up")

        self.form_layout.addWidget(self.button_add_picture)
        self.form_layout.addWidget(self.line_edit_mail)
        self.form_layout.addWidget(self.line_edit_confirm_password)
        self.form_layout.addWidget(self.button_register)

        self.setLayout(self.form_layout)
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

    def setup_connection(self):
        pass
