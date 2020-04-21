from PyQt5 import QtCore, QtGui, QtWidgets
import messenger_ui
import os
try:
    import winsound
except:
    pass
import socket_connection


class Messenger(QtWidgets.QWidget):

    def __init__(self, username, socket):
        super().__init__()
        self.username = username
        self.ui = messenger_ui.Ui_messenger_main_window()
        self.ui.setupUi(self)
        self.ui.send_button.clicked.connect(self.send)
        self.ui.messenger_input_text.returnPressed.connect(self.send)
        self.ui.chats_tableWidget.cellClicked.connect(self.update_display)
        self.socket = socket
        self.input_thread = InputQueue(self.socket)
        self.input_thread.signal.connect(self.message_received)
        self.incomming_message_sound = 'Sound_clips/incoming_message.wav'
        # self.input_thread.start()
        self.message_prefix = "message:"


    def send(self):

        recipients = self.ui.recipients_input.text().strip(' ')
        if "," in recipients:
            recipients_list = sorted(recipients.split(','))
            sorted_recipients = ",".join(recipients_list)
        else:
            sorted_recipients = recipients
        if sorted_recipients == '':
            return

        message = self.ui.messenger_input_text.text()
        if message.strip(' ') == '':
            return

        # self.add_row(sorted_recipients)

        self.ui.messenger_input_text.clear()
        data = self.message_prefix + sorted_recipients + ':' + message
        transmit = data.encode('ascii')
        self.socket.send(transmit)

    def message_received(self, message):
        recipients = message.split(":")[0]
        recipients_list = recipients.split(",")
        if self.username in recipients_list:
            recipients_list.remove(self.username)
            recipients_list.append(message.split(":")[1].strip(' '))
            recipients_list = sorted(recipients_list)
            recipients = ",".join(recipients_list)
        message_text = message[len(message.split(":")[0]) +1:]
        chat_file = open("chats/" + recipients + ".txt", "a")
        chat_file.write(message_text + "\n")
        chat_file.close()
        if recipients == self.ui.recipients_input.text():
            self.ui.display_messages_text.appendPlainText(message_text)
        self.add_row(recipients)
        if message_text.split(':')[1] != self.username:
            try:
                winsound.PlaySound(self.incomming_message_sound, winsound.SND_ASYNC)
            except:
                pass
        #if message[:len(self.username)] == self.username:
            #self.ui.messenger_input_text.clear()

    def update_display(self):
        item = self.ui.chats_tableWidget.item(self.ui.chats_tableWidget.currentRow(), 0)
        if "," in self.ui.recipients_input.text():
            name = ",".join(sorted(self.ui.recipients_input.text().strip(' ').split(",")))
        else:
            name = self.ui.recipients_input.text()
        if item.text() == name:
            return
        # open chat file to read
        chat_file = open("chats/" + item.text() + ".txt", "r")
        messages = chat_file.read()
        self.ui.display_messages_text.clear()
        self.ui.display_messages_text.setPlainText(messages)
        chat_file.close()
        self.ui.recipients_input.setText(item.text())

        # TODO finish this
    def add_row(self, sorted_recipients):

        does_not_exist_flage = True
        # check to see if the row already exists
        for index in range(self.ui.chats_tableWidget.rowCount()):
            if sorted_recipients == self.ui.chats_tableWidget.item(index, 0).text():
                does_not_exist_flage = False
        if does_not_exist_flage is True:
            # add new row
            new_item = QtWidgets.QTableWidgetItem()
            row_count = self.ui.chats_tableWidget.rowCount()
            # add new row
            self.ui.chats_tableWidget.setRowCount(row_count + 1)
            self.ui.chats_tableWidget.setItem(0, row_count, new_item)

            # shift everything down
            for index in range(row_count):
                item_text = self.ui.chats_tableWidget.item(row_count - index - 1, 0).text()
                item = self.ui.chats_tableWidget.item(row_count - index, 0)
                item.setText(item_text)
            self.ui.chats_tableWidget.item(0, 0).setText(sorted_recipients)


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


