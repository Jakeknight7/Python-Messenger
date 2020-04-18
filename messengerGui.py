from PyQt5 import QtCore, QtGui, QtWidgets
import messenger_ui
import socket_connection


class Messenger(QtWidgets.QWidget):

    def __init__(self, username, socket):
        super().__init__()
        self.username = username
        self.ui = messenger_ui.Ui_messenger_main_window()
        self.ui.setupUi(self)
        self.ui.send_button.clicked.connect(self.send)
        self.socket = socket
        self.input_thread = InputQueue(self.socket)
        self.input_thread.signal.connect(self.message_received)
        # self.input_thread.start()

        self.message_prefix = "message:"

    def send(self):

        recipients = self.ui.recipients_input.text()
        if recipients == '':
            return

        message = self.ui.messenger_input_text.text()
        if message.strip() == '':
            return

        self.ui.messenger_input_text.clear()
        data = self.message_prefix + recipients + ':' + message
        transmit = data.encode('ascii')
        self.socket.send(transmit)

    def message_received(self, message):
        self.ui.display_messages_text.appendPlainText(message)
        #if message[:len(self.username)] == self.username:
            #self.ui.messenger_input_text.clear()


class InputQueue(QtCore.QThread):
    signal = QtCore.pyqtSignal('PyQt_PyObject')
    def __init__(self, socket):
        super().__init__()

        self.socket = socket

    def run(self):
        while True:
            try:
                data = self.socket.recv(1024)
                if data:
                    message = data.decode('ascii')
                    self.signal.emit(message)
            except ConnectionAbortedError:
                print("Connection aborted")


