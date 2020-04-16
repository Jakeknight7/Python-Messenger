import LoginGui
import messengerGui
#import client
from PyQt5 import QtCore, QtGui, QtWidgets


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #messenger = messengerGui.Messenger()
    #messenger.show()
    login_form = LoginGui.LoginPage()
    login_form.show()
    sys.exit(app.exec_())


main()