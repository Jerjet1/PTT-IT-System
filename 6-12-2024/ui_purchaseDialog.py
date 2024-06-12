# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchaseDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_purchaseDialog(object):
    def setupUi(self, purchaseDialog):
        if not purchaseDialog.objectName():
            purchaseDialog.setObjectName(u"purchaseDialog")
        purchaseDialog.resize(500, 550)
        self.verticalLayout_4 = QVBoxLayout(purchaseDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(purchaseDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)

        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_2.addWidget(self.lineEdit_8, 0, Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.frame)

        self.productInputs = QFrame(purchaseDialog)
        self.productInputs.setObjectName(u"productInputs")
        self.productInputs.setFrameShape(QFrame.StyledPanel)
        self.productInputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.productInputs)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cpu = QHBoxLayout()
        self.cpu.setObjectName(u"cpu")
        self.customerName = QLabel(self.productInputs)
        self.customerName.setObjectName(u"customerName")

        self.cpu.addWidget(self.customerName, 0, Qt.AlignLeft)

        self.technicianDropdown_3 = QComboBox(self.productInputs)
        self.technicianDropdown_3.addItem("")
        self.technicianDropdown_3.addItem("")
        self.technicianDropdown_3.setObjectName(u"technicianDropdown_3")
        self.technicianDropdown_3.setMinimumSize(QSize(250, 0))

        self.cpu.addWidget(self.technicianDropdown_3, 0, Qt.AlignBottom)

        self.lineEdit = QLineEdit(self.productInputs)
        self.lineEdit.setObjectName(u"lineEdit")

        self.cpu.addWidget(self.lineEdit, 0, Qt.AlignRight)


        self.verticalLayout_5.addLayout(self.cpu)

        self.gpu = QHBoxLayout()
        self.gpu.setObjectName(u"gpu")
        self.device = QLabel(self.productInputs)
        self.device.setObjectName(u"device")

        self.gpu.addWidget(self.device, 0, Qt.AlignLeft)

        self.technicianDropdown_2 = QComboBox(self.productInputs)
        self.technicianDropdown_2.addItem("")
        self.technicianDropdown_2.addItem("")
        self.technicianDropdown_2.setObjectName(u"technicianDropdown_2")
        self.technicianDropdown_2.setMinimumSize(QSize(250, 0))

        self.gpu.addWidget(self.technicianDropdown_2, 0, Qt.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.productInputs)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gpu.addWidget(self.lineEdit_2, 0, Qt.AlignRight)


        self.verticalLayout_5.addLayout(self.gpu)

        self.motherboard = QHBoxLayout()
        self.motherboard.setObjectName(u"motherboard")
        self.technician = QLabel(self.productInputs)
        self.technician.setObjectName(u"technician")

        self.motherboard.addWidget(self.technician, 0, Qt.AlignLeft)

        self.technicianDropdown = QComboBox(self.productInputs)
        self.technicianDropdown.addItem("")
        self.technicianDropdown.addItem("")
        self.technicianDropdown.setObjectName(u"technicianDropdown")
        self.technicianDropdown.setMinimumSize(QSize(250, 0))

        self.motherboard.addWidget(self.technicianDropdown, 0, Qt.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.productInputs)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.motherboard.addWidget(self.lineEdit_3, 0, Qt.AlignRight)


        self.verticalLayout_5.addLayout(self.motherboard)

        self.storage = QHBoxLayout()
        self.storage.setObjectName(u"storage")
        self.serviceType = QLabel(self.productInputs)
        self.serviceType.setObjectName(u"serviceType")

        self.storage.addWidget(self.serviceType, 0, Qt.AlignLeft)

        self.serviceTypeDropdown = QComboBox(self.productInputs)
        self.serviceTypeDropdown.addItem("")
        self.serviceTypeDropdown.addItem("")
        self.serviceTypeDropdown.addItem("")
        self.serviceTypeDropdown.setObjectName(u"serviceTypeDropdown")
        self.serviceTypeDropdown.setMinimumSize(QSize(250, 0))

        self.storage.addWidget(self.serviceTypeDropdown, 0, Qt.AlignHCenter)

        self.lineEdit_4 = QLineEdit(self.productInputs)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.storage.addWidget(self.lineEdit_4, 0, Qt.AlignRight)


        self.verticalLayout_5.addLayout(self.storage)

        self.ram = QHBoxLayout()
        self.ram.setObjectName(u"ram")
        self.serviceType_2 = QLabel(self.productInputs)
        self.serviceType_2.setObjectName(u"serviceType_2")

        self.ram.addWidget(self.serviceType_2, 0, Qt.AlignLeft)

        self.serviceTypeDropdown_2 = QComboBox(self.productInputs)
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.setObjectName(u"serviceTypeDropdown_2")
        self.serviceTypeDropdown_2.setMinimumSize(QSize(250, 0))

        self.ram.addWidget(self.serviceTypeDropdown_2, 0, Qt.AlignHCenter)

        self.lineEdit_5 = QLineEdit(self.productInputs)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.ram.addWidget(self.lineEdit_5, 0, Qt.AlignRight)


        self.verticalLayout_5.addLayout(self.ram)

        self.case_2 = QHBoxLayout()
        self.case_2.setObjectName(u"case_2")
        self.serviceType_3 = QLabel(self.productInputs)
        self.serviceType_3.setObjectName(u"serviceType_3")

        self.case_2.addWidget(self.serviceType_3, 0, Qt.AlignLeft)

        self.serviceTypeDropdown_3 = QComboBox(self.productInputs)
        self.serviceTypeDropdown_3.addItem("")
        self.serviceTypeDropdown_3.addItem("")
        self.serviceTypeDropdown_3.addItem("")
        self.serviceTypeDropdown_3.setObjectName(u"serviceTypeDropdown_3")
        self.serviceTypeDropdown_3.setMinimumSize(QSize(250, 0))

        self.case_2.addWidget(self.serviceTypeDropdown_3, 0, Qt.AlignHCenter)

        self.lineEdit_6 = QLineEdit(self.productInputs)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.case_2.addWidget(self.lineEdit_6, 0, Qt.AlignRight)


        self.verticalLayout_5.addLayout(self.case_2)

        self.components = QHBoxLayout()
        self.components.setObjectName(u"components")
        self.serviceType_4 = QLabel(self.productInputs)
        self.serviceType_4.setObjectName(u"serviceType_4")

        self.components.addWidget(self.serviceType_4, 0, Qt.AlignLeft)

        self.serviceTypeDropdown_4 = QComboBox(self.productInputs)
        self.serviceTypeDropdown_4.addItem("")
        self.serviceTypeDropdown_4.addItem("")
        self.serviceTypeDropdown_4.addItem("")
        self.serviceTypeDropdown_4.setObjectName(u"serviceTypeDropdown_4")
        self.serviceTypeDropdown_4.setMinimumSize(QSize(250, 0))

        self.components.addWidget(self.serviceTypeDropdown_4, 0, Qt.AlignHCenter)

        self.lineEdit_7 = QLineEdit(self.productInputs)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.components.addWidget(self.lineEdit_7, 0, Qt.AlignRight)


        self.verticalLayout_5.addLayout(self.components)


        self.verticalLayout_4.addWidget(self.productInputs)

        self.verticalSpacer = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.payment = QFrame(purchaseDialog)
        self.payment.setObjectName(u"payment")
        self.payment.setFrameShape(QFrame.StyledPanel)
        self.payment.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.payment)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.amount_paid = QHBoxLayout()
        self.amount_paid.setObjectName(u"amount_paid")
        self.amountPaid = QLabel(self.payment)
        self.amountPaid.setObjectName(u"amountPaid")

        self.amount_paid.addWidget(self.amountPaid, 0, Qt.AlignLeft)

        self.amountPaidInput = QLineEdit(self.payment)
        self.amountPaidInput.setObjectName(u"amountPaidInput")
        self.amountPaidInput.setMinimumSize(QSize(250, 0))

        self.amount_paid.addWidget(self.amountPaidInput, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.amount_paid)

        self.charge_2 = QHBoxLayout()
        self.charge_2.setObjectName(u"charge_2")
        self.charge = QLabel(self.payment)
        self.charge.setObjectName(u"charge")

        self.charge_2.addWidget(self.charge, 0, Qt.AlignLeft)

        self.chargeOutput = QLineEdit(self.payment)
        self.chargeOutput.setObjectName(u"chargeOutput")
        self.chargeOutput.setMinimumSize(QSize(250, 0))

        self.charge_2.addWidget(self.chargeOutput, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.charge_2)

        self.change_2 = QHBoxLayout()
        self.change_2.setObjectName(u"change_2")
        self.change = QLabel(self.payment)
        self.change.setObjectName(u"change")

        self.change_2.addWidget(self.change, 0, Qt.AlignLeft)

        self.changeOutput = QLineEdit(self.payment)
        self.changeOutput.setObjectName(u"changeOutput")
        self.changeOutput.setMinimumSize(QSize(250, 0))
        self.changeOutput.setReadOnly(True)

        self.change_2.addWidget(self.changeOutput, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.change_2)


        self.verticalLayout_4.addWidget(self.payment)

        self.verticalSpacer_2 = QSpacerItem(20, 24, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.confirmButton = QPushButton(purchaseDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_3.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(purchaseDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(purchaseDialog)

        QMetaObject.connectSlotsByName(purchaseDialog)
    # setupUi

    def retranslateUi(self, purchaseDialog):
        purchaseDialog.setWindowTitle(QCoreApplication.translate("purchaseDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("purchaseDialog", u"Customer Name", None))
        self.customerName.setText(QCoreApplication.translate("purchaseDialog", u"CPU", None))
        self.technicianDropdown_3.setItemText(0, QCoreApplication.translate("purchaseDialog", u"person1", None))
        self.technicianDropdown_3.setItemText(1, QCoreApplication.translate("purchaseDialog", u"person2", None))

        self.device.setText(QCoreApplication.translate("purchaseDialog", u"GPU", None))
        self.technicianDropdown_2.setItemText(0, QCoreApplication.translate("purchaseDialog", u"person1", None))
        self.technicianDropdown_2.setItemText(1, QCoreApplication.translate("purchaseDialog", u"person2", None))

        self.technician.setText(QCoreApplication.translate("purchaseDialog", u"Motherboard", None))
        self.technicianDropdown.setItemText(0, QCoreApplication.translate("purchaseDialog", u"person1", None))
        self.technicianDropdown.setItemText(1, QCoreApplication.translate("purchaseDialog", u"person2", None))

        self.serviceType.setText(QCoreApplication.translate("purchaseDialog", u"Storage", None))
        self.serviceTypeDropdown.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.serviceType_2.setText(QCoreApplication.translate("purchaseDialog", u"RAM", None))
        self.serviceTypeDropdown_2.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown_2.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown_2.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.serviceType_3.setText(QCoreApplication.translate("purchaseDialog", u"Case", None))
        self.serviceTypeDropdown_3.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown_3.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown_3.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.serviceType_4.setText(QCoreApplication.translate("purchaseDialog", u"Components", None))
        self.serviceTypeDropdown_4.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown_4.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown_4.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.amountPaid.setText(QCoreApplication.translate("purchaseDialog", u"Amount Paid", None))
        self.charge.setText(QCoreApplication.translate("purchaseDialog", u"Charge", None))
        self.change.setText(QCoreApplication.translate("purchaseDialog", u"Change", None))
        self.confirmButton.setText(QCoreApplication.translate("purchaseDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("purchaseDialog", u"Cancel", None))
    # retranslateUi

