
from PyQt5 import QtCore, QtGui, QtWidgets
import Login_ui
import messengerGui
import socket_connection


class LoginPage(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Login_ui.Ui_login_form()
        self.ui.setupUi(self)
        self.ui.login_button.clicked.connect(self.login)
        self.ui.create_account_button.clicked.connect(self.new_user)
        self.socket = None

        self.new_user_prefix = "new_user:"
        self.existing_user_prefix = "existing_user:"

    def new_user(self):
        username = self.ui.new_username_input.text()
        password = self.ui.new_password_input.text()
        confirm_password = self.ui.confirm_password_input.text()

        if ' ' in username:
            return

        if len(password) > 5 and password == confirm_password:
            self.send_account_info(username, password, self.new_user_prefix)

    def login(self):
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        self.send_account_info(username, password, self.existing_user_prefix)

    def send_account_info(self, username, password, prefix):
        self.socket = socket_connection.Connection()
        message = prefix + username + ' ' + password
        byte_data = message.encode('ascii')
        self.socket.socket_connection.send(byte_data)
        data = self.socket.socket_connection.recv(32)
        return_message = data.decode('ascii')
        if return_message != 'Success':
            return
        self.messenger = messengerGui.Messenger(username)
        self.messenger.show()
        self.close()
        self.messenger.input_thread.start()
