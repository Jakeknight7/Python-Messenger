import LoginGui
import messengerGui
#import client
from PyQt5 import QtCore, QtGui, QtWidgets
import socket_connection


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #messenger = messengerGui.Messenger()
    #messenger.show()
    socket = socket_connection.Connection().socket_connection
    login_form = LoginGui.LoginPage(socket)
    login_form.show()
    sys.exit(app.exec_())


main()