# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(870, 618)
        LoginPage.setMaximumSize(QSize(600, 600))
        LoginPage.setStyleSheet(u"QWidget{\n"
" background-color: rgb(183, 181, 151);\n"
"}")
        self.horizontalLayout = QHBoxLayout(LoginPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftHalf = QFrame(LoginPage)
        self.leftHalf.setObjectName(u"leftHalf")
        self.leftHalf.setMaximumSize(QSize(600, 600))
        self.leftHalf.setStyleSheet(u"QFrame{\n"
"background-color: rgb(107, 138, 122)\n"
"}")
        self.leftHalf.setFrameShape(QFrame.StyledPanel)
        self.leftHalf.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.leftHalf)
        self.gridLayout.setObjectName(u"gridLayout")
        self.techImage = QLabel(self.leftHalf)
        self.techImage.setObjectName(u"techImage")
        self.techImage.setPixmap(QPixmap(u"images/technicianBackground.png"))
        self.techImage.setScaledContents(True)

        self.gridLayout.addWidget(self.techImage, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.leftHalf)

        self.rightHalf = QFrame(LoginPage)
        self.rightHalf.setObjectName(u"rightHalf")
        self.rightHalf.setStyleSheet(u"QFrame{\n"
"background-color: rgb(107, 138, 122)\n"
"}")
        self.rightHalf.setFrameShape(QFrame.StyledPanel)
        self.rightHalf.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.rightHalf)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pttImage = QFrame(self.rightHalf)
        self.pttImage.setObjectName(u"pttImage")
        self.pttImage.setStyleSheet(u"QFrame{\n"
"background-color: rgb(183, 181, 151)\n"
"}")
        self.pttImage.setFrameShape(QFrame.StyledPanel)
        self.pttImage.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.pttImage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pttLogo = QLabel(self.pttImage)
        self.pttLogo.setObjectName(u"pttLogo")
        self.pttLogo.setMaximumSize(QSize(200, 200))
        self.pttLogo.setPixmap(QPixmap(u"images/ptt-logo.png"))
        self.pttLogo.setScaledContents(True)

        self.gridLayout_2.addWidget(self.pttLogo, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.pttImage)

        self.loginForm = QFrame(self.rightHalf)
        self.loginForm.setObjectName(u"loginForm")
        self.loginForm.setMaximumSize(QSize(500, 500))
        self.loginForm.setStyleSheet(u"QFrame{\n"
"background-color: rgb(183, 181, 151)\n"
"}")
        self.loginForm.setFrameShape(QFrame.StyledPanel)
        self.loginForm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.loginForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, 10, 25, 20)
        self.errorMessage = QLabel(self.loginForm)
        self.errorMessage.setObjectName(u"errorMessage")
        self.errorMessage.setMaximumSize(QSize(150, 50))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        self.errorMessage.setFont(font)
        self.errorMessage.setAlignment(Qt.AlignCenter)
        self.errorMessage.setWordWrap(True)
        self.errorMessage.setMargin(5)
        self.errorMessage.setIndent(40)

        self.verticalLayout_2.addWidget(self.errorMessage)

        self.user = QLineEdit(self.loginForm)
        self.user.setClearButtonEnabled(True)
        self.user.setObjectName(u"user")
        self.user.setMaximumSize(QSize(175, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        self.user.setFont(font1)
        self.user.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QLineEdit:pressed {\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"}")

        self.verticalLayout_2.addWidget(self.user)

        self.password = QLineEdit(self.loginForm)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)
        self.password.setObjectName(u"password")
        self.password.setMaximumSize(QSize(175, 16777215))
        self.password.setFont(font1)
        self.password.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"font-size: 16px;\n"
"}")

        self.verticalLayout_2.addWidget(self.password)

        self.loginButton = QPushButton(self.loginForm)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMaximumSize(QSize(500, 16777215))
        self.loginButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"margin-left: 25px;\n"
"margin-right:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.loginButton)


        self.verticalLayout.addWidget(self.loginForm)


        self.horizontalLayout.addWidget(self.rightHalf)


        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Main", None))
        self.techImage.setText("")
        self.pttLogo.setText("")
        self.errorMessage.setText("")
        self.user.setPlaceholderText(QCoreApplication.translate("LoginPage", u"User", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginPage", u"Sign In", None))
    # retranslateUi

