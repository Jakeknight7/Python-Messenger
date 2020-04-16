# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Messenger.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_messenger_main_window(object):
    def setupUi(self, messenger_main_window):
        messenger_main_window.setObjectName("messenger_main_window")
        messenger_main_window.resize(446, 427)
        self.centralwidget = QtWidgets.QWidget(messenger_main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.messenger_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.messenger_groupbox.setGeometry(QtCore.QRect(10, 10, 421, 391))
        self.messenger_groupbox.setObjectName("messenger_groupbox")
        self.display_messages_text = QtWidgets.QPlainTextEdit(self.messenger_groupbox)
        self.display_messages_text.setGeometry(QtCore.QRect(10, 50, 401, 221))
        self.display_messages_text.setReadOnly(True)
        self.display_messages_text.setObjectName("display_messages_text")
        self.send_button = QtWidgets.QPushButton(self.messenger_groupbox)
        self.send_button.setGeometry(QtCore.QRect(290, 280, 121, 101))
        self.send_button.setObjectName("send_button")
        self.recipients_input = QtWidgets.QLineEdit(self.messenger_groupbox)
        self.recipients_input.setGeometry(QtCore.QRect(70, 20, 341, 20))
        self.recipients_input.setObjectName("recipients_input")
        self.recipients_label = QtWidgets.QLabel(self.messenger_groupbox)
        self.recipients_label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.recipients_label.setObjectName("recipients_label")
        self.messenger_input_text = QtWidgets.QLineEdit(self.messenger_groupbox)
        self.messenger_input_text.setGeometry(QtCore.QRect(10, 280, 271, 101))
        self.messenger_input_text.setObjectName("messenger_input_text")
        #messenger_main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(messenger_main_window)
        self.statusbar.setObjectName("statusbar")
        #messenger_main_window.setStatusBar(self.statusbar)

        self.retranslateUi(messenger_main_window)
        QtCore.QMetaObject.connectSlotsByName(messenger_main_window)

    def retranslateUi(self, messenger_main_window):
        _translate = QtCore.QCoreApplication.translate
        messenger_main_window.setWindowTitle(_translate("messenger_main_window", "Messenger"))
        self.messenger_groupbox.setTitle(_translate("messenger_main_window", "Group Message"))
        self.send_button.setText(_translate("messenger_main_window", "Send Dat Shi"))
        self.recipients_label.setText(_translate("messenger_main_window", "Recipients"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    messenger_main_window = QtWidgets.QMainWindow()
    ui = Ui_messenger_main_window()
    ui.setupUi(messenger_main_window)
    messenger_main_window.show()
    sys.exit(app.exec_())
