# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_akun.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image_qrc, sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1090, 579)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 40, 1031, 511))
        self.frame.setStyleSheet("background-color: #c8c1a8;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1031, 80))
        self.frame_2.setStyleSheet("background-color: #fff6d6;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(-90, -30, 321, 131))
        self.frame_5.setStyleSheet("image: url(:/img/img/logo.png)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(790, 20, 221, 41))
        self.label_8.setStyleSheet("font-size : 13px;")
        self.label_8.setObjectName("label_8")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(600, 100, 391, 381))
        self.frame_4.setStyleSheet("background-color: white;\n"
"border-radius: 10;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 541, 31))
        self.label_4.setStyleSheet("font-weight: 500;\n"
"font-size: 25px;")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 351, 271))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setStyleSheet("border :none;\n"
"border-bottom: 1px solid;\n"
"color : #434343;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setStyleSheet("border :none;\n"
"border-bottom : 1px solid;\n"
"color : #434343;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setStyleSheet("border :none;\n"
"border-bottom : 1px solid;\n"
"color : #434343;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setStyleSheet("border :none;\n"
"border-bottom : 1px solid;\n"
"color : #434343;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 330, 121, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 127, 255);\n"
"    border-radius: 10px;\n"
"    color:#ffffff;\n"
"    font-size:15px;\n"
"    font-weight:500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(180, 181, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 127, 255); */\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(180, 330, 131, 41))
        self.label_5.setStyleSheet("font-size : 15px;\n"
"background-color : none;")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 330, 61, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: #1837ff;\n"
"font-size: 15px;\n"
"text-decoration:underline;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   color: rgb(179, 179, 179); \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    color: rgb(0, 0, 0); \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 541, 31))
        self.label_2.setStyleSheet("font-weight: 500;\n"
"font-size: 25px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 561, 211))
        self.label_3.setStyleSheet("font-weight: 500;\n"
"font-size: 25px;")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Dev By Muhamad Agil Nab\'han @2024"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p>Kesempatan tidak selalu datang dua kali...</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; color:#4d4d4d;\">Pendaftaran Akun</span></p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Nama Lengkap "))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Email Pendaftar"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Konfirmasi Password"))
        self.pushButton.setText(_translate("Form", "Buat"))
        self.label_5.setText(_translate("Form", "Sudah Punya Akun?"))
        self.pushButton_2.setText(_translate("Form", "Log in"))
        self.label_2.setToolTip(_translate("Form", "<html><head/><body><p>Kesempatan tidak selalu datang dua kali...</p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt; color:#4d4d4d;\">Kesempatan tidak selalu datang dua kali...</span></p></body></html>"))
        self.label_3.setToolTip(_translate("Form", "<html><head/><body><p>Kesempatan tidak selalu datang dua kali...</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:48pt; color:#f65737;\">Mari Bergabung</span></p><p><span style=\" font-size:48pt; color:#f65737;\"> Bersama Kami</span></p></body></html>"))
import image_qrc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
