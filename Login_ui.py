# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.resize(440, 304)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_form.sizePolicy().hasHeightForWidth())
        login_form.setSizePolicy(sizePolicy)
        login_form.setMinimumSize(QtCore.QSize(440, 304))
        login_form.setMaximumSize(QtCore.QSize(440, 304))
        self.groupBox = QtWidgets.QGroupBox(login_form)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 201, 281))
        self.groupBox.setObjectName("groupBox")
        self.username_label = QtWidgets.QLabel(self.groupBox)
        self.username_label.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.groupBox)
        self.password_label.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.password_label.setObjectName("password_label")
        self.username_input = QtWidgets.QLineEdit(self.groupBox)
        self.username_input.setGeometry(QtCore.QRect(70, 80, 113, 20))
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(self.groupBox)
        self.password_input.setGeometry(QtCore.QRect(70, 130, 113, 20))
        self.password_input.setObjectName("password_input")
        self.login_button = QtWidgets.QPushButton(self.groupBox)
        self.login_button.setGeometry(QtCore.QRect(60, 230, 75, 23))
        self.login_button.setObjectName("login_button")
        self.existing_user_error_label = QtWidgets.QLabel(self.groupBox)
        self.existing_user_error_label.setGeometry(QtCore.QRect(6, 40, 191, 20))
        self.existing_user_error_label.setText("")
        self.existing_user_error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.existing_user_error_label.setObjectName("existing_user_error_label")
        self.groupBox_2 = QtWidgets.QGroupBox(login_form)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 10, 211, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.new_username_label = QtWidgets.QLabel(self.groupBox_2)
        self.new_username_label.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.new_username_label.setObjectName("new_username_label")
        self.new_password_label = QtWidgets.QLabel(self.groupBox_2)
        self.new_password_label.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.new_password_label.setObjectName("new_password_label")
        self.confirm_password_label = QtWidgets.QLabel(self.groupBox_2)
        self.confirm_password_label.setGeometry(QtCore.QRect(10, 180, 51, 31))
        self.confirm_password_label.setWordWrap(True)
        self.confirm_password_label.setObjectName("confirm_password_label")
        self.new_username_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.new_username_input.setGeometry(QtCore.QRect(70, 80, 113, 20))
        self.new_username_input.setObjectName("new_username_input")
        self.new_password_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.new_password_input.setGeometry(QtCore.QRect(70, 130, 113, 20))
        self.new_password_input.setObjectName("new_password_input")
        self.confirm_password_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.confirm_password_input.setGeometry(QtCore.QRect(70, 180, 113, 20))
        self.confirm_password_input.setObjectName("confirm_password_input")
        self.create_account_button = QtWidgets.QPushButton(self.groupBox_2)
        self.create_account_button.setGeometry(QtCore.QRect(60, 230, 91, 23))
        self.create_account_button.setObjectName("create_account_button")
        self.new_user_error_label = QtWidgets.QLabel(self.groupBox_2)
        self.new_user_error_label.setGeometry(QtCore.QRect(0, 40, 211, 21))
        self.new_user_error_label.setText("")
        self.new_user_error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.new_user_error_label.setObjectName("new_user_error_label")

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "Login"))
        self.groupBox.setTitle(_translate("login_form", "Existing User"))
        self.username_label.setText(_translate("login_form", "Username"))
        self.password_label.setText(_translate("login_form", "Password"))
        self.login_button.setText(_translate("login_form", "Log In"))
        self.groupBox_2.setTitle(_translate("login_form", "New User"))
        self.new_username_label.setText(_translate("login_form", "Username"))
        self.new_password_label.setText(_translate("login_form", "Password"))
        self.confirm_password_label.setText(_translate("login_form", "Confirm Password"))
        self.create_account_button.setText(_translate("login_form", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_form = QtWidgets.QWidget()
    ui = Ui_login_form()
    ui.setupUi(login_form)
    login_form.show()
    sys.exit(app.exec_())
