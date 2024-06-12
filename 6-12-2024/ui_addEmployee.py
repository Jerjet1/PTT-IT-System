# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addEmployee.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QRegularExpression,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter, QRegularExpressionValidator,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_addEmployee(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 350)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.employeeName = QLabel(self.frame)
        self.employeeName.setObjectName(u"employeeName")

        self.horizontalLayout.addWidget(self.employeeName)

        self.employeeFNameInput = QLineEdit(self.frame)
        self.employeeFNameInput.setObjectName(u"employeeNameInput")
        self.employeeFNameInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout.addWidget(self.employeeFNameInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.employeeName_2 = QLabel(self.frame)
        self.employeeName_2.setObjectName(u"employeeName_2")

        self.horizontalLayout_2.addWidget(self.employeeName_2)

        self.employeeLNameInput_2 = QLineEdit(self.frame)
        self.employeeLNameInput_2.setObjectName(u"employeeNameInput_2")
        self.employeeLNameInput_2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.employeeLNameInput_2, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.address = QLabel(self.frame)
        self.address.setObjectName(u"address")

        self.horizontalLayout_3.addWidget(self.address)

        self.addressInput = QLineEdit(self.frame)
        self.addressInput.setObjectName(u"addressInput")
        self.addressInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_3.addWidget(self.addressInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.contactNumber = QLabel(self.frame)
        self.contactNumber.setObjectName(u"contactNumber")

        self.horizontalLayout_4.addWidget(self.contactNumber)
        self.contactNumberInput = QLineEdit(self.frame)
        self.contactNumberInput.setObjectName(u"contactNumberInput")
        self.contactNumberInput.setMinimumSize(QSize(250, 0))
        # regex = QRegularExpression("^\d{0,11}$")
        # validator = QRegularExpressionValidator(regex, self.contactNumberInput)
        # self.contactNumberInput.setValidator(validator)

        self.horizontalLayout_4.addWidget(self.contactNumberInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 119, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.confirmButton = QPushButton(Dialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_2.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.employeeName.setText(QCoreApplication.translate("Dialog", u"First Name", None))
        self.employeeName_2.setText(QCoreApplication.translate("Dialog", u"Last Name", None))
        self.address.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.contactNumber.setText(QCoreApplication.translate("Dialog", u"Contact Number", None))
        self.confirmButton.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

