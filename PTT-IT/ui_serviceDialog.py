# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serviceDialog.ui'
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

class Ui_serviceReportDialog(object):
    def setupUi(self, serviceReportDialog):
        if not serviceReportDialog.objectName():
            serviceReportDialog.setObjectName(u"serviceReportDialog")
        serviceReportDialog.resize(500, 500)
        self.verticalLayout_8 = QVBoxLayout(serviceReportDialog)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.serviceDetails = QFrame(serviceReportDialog)
        self.serviceDetails.setObjectName(u"serviceDetails")
        self.serviceDetails.setFrameShape(QFrame.StyledPanel)
        self.serviceDetails.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.serviceDetails)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.customerName_2 = QLabel(self.serviceDetails)
        self.customerName_2.setObjectName(u"customerName_2")

        self.horizontalLayout_8.addWidget(self.customerName_2)

        self.customerNameInput_2 = QLineEdit(self.serviceDetails)
        self.customerNameInput_2.setObjectName(u"customerNameInput_2")
        self.customerNameInput_2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_8.addWidget(self.customerNameInput_2, 0, Qt.AlignRight)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.device_2 = QLabel(self.serviceDetails)
        self.device_2.setObjectName(u"device_2")

        self.horizontalLayout_9.addWidget(self.device_2)

        self.deviceInput_2 = QLineEdit(self.serviceDetails)
        self.deviceInput_2.setObjectName(u"deviceInput_2")
        self.deviceInput_2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_9.addWidget(self.deviceInput_2, 0, Qt.AlignRight)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.technician_2 = QLabel(self.serviceDetails)
        self.technician_2.setObjectName(u"technician_2")

        self.horizontalLayout_10.addWidget(self.technician_2)

        self.technicianDropdown_2 = QComboBox(self.serviceDetails)
        self.technicianDropdown_2.addItem("")
        self.technicianDropdown_2.addItem("")
        self.technicianDropdown_2.setObjectName(u"technicianDropdown_2")
        self.technicianDropdown_2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_10.addWidget(self.technicianDropdown_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.serviceType_2 = QLabel(self.serviceDetails)
        self.serviceType_2.setObjectName(u"serviceType_2")

        self.horizontalLayout_11.addWidget(self.serviceType_2)

        self.serviceTypeDropdown_2 = QComboBox(self.serviceDetails)
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.setObjectName(u"serviceTypeDropdown_2")
        self.serviceTypeDropdown_2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_11.addWidget(self.serviceTypeDropdown_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)


        self.verticalLayout_8.addWidget(self.serviceDetails)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.cashInput = QFrame(serviceReportDialog)
        self.cashInput.setObjectName(u"cashInput")
        self.cashInput.setFrameShape(QFrame.StyledPanel)
        self.cashInput.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.cashInput)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.amountPaid_3 = QLabel(self.cashInput)
        self.amountPaid_3.setObjectName(u"amountPaid_3")

        self.horizontalLayout_15.addWidget(self.amountPaid_3)

        self.amountPaidInput_3 = QLineEdit(self.cashInput)
        self.amountPaidInput_3.setObjectName(u"amountPaidInput_3")
        self.amountPaidInput_3.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_15.addWidget(self.amountPaidInput_3, 0, Qt.AlignRight)


        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.charge_3 = QLabel(self.cashInput)
        self.charge_3.setObjectName(u"charge_3")

        self.horizontalLayout_16.addWidget(self.charge_3)

        self.chargeOutput_3 = QLineEdit(self.cashInput)
        self.chargeOutput_3.setObjectName(u"chargeOutput_3")
        self.chargeOutput_3.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_16.addWidget(self.chargeOutput_3, 0, Qt.AlignRight)


        self.verticalLayout_6.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.change_3 = QLabel(self.cashInput)
        self.change_3.setObjectName(u"change_3")

        self.horizontalLayout_17.addWidget(self.change_3)

        self.changeOutput_3 = QLineEdit(self.cashInput)
        self.changeOutput_3.setObjectName(u"changeOutput_3")
        self.changeOutput_3.setMinimumSize(QSize(250, 0))
        self.changeOutput_3.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.changeOutput_3, 0, Qt.AlignRight)


        self.verticalLayout_6.addLayout(self.horizontalLayout_17)


        self.verticalLayout_8.addWidget(self.cashInput)

        self.verticalSpacer_2 = QSpacerItem(20, 72, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.confirmButton_3 = QPushButton(serviceReportDialog)
        self.confirmButton_3.setObjectName(u"confirmButton_3")

        self.verticalLayout_7.addWidget(self.confirmButton_3)

        self.cancelButton_3 = QPushButton(serviceReportDialog)
        self.cancelButton_3.setObjectName(u"cancelButton_3")

        self.verticalLayout_7.addWidget(self.cancelButton_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.retranslateUi(serviceReportDialog)

        QMetaObject.connectSlotsByName(serviceReportDialog)
    # setupUi

    def retranslateUi(self, serviceReportDialog):
        serviceReportDialog.setWindowTitle(QCoreApplication.translate("serviceReportDialog", u"Dialog", None))
        self.customerName_2.setText(QCoreApplication.translate("serviceReportDialog", u"Customer Name", None))
        self.device_2.setText(QCoreApplication.translate("serviceReportDialog", u"Device", None))
        self.technician_2.setText(QCoreApplication.translate("serviceReportDialog", u"Technician", None))
        self.technicianDropdown_2.setItemText(0, QCoreApplication.translate("serviceReportDialog", u"person1", None))
        self.technicianDropdown_2.setItemText(1, QCoreApplication.translate("serviceReportDialog", u"person2", None))

        self.serviceType_2.setText(QCoreApplication.translate("serviceReportDialog", u"Service Type", None))
        self.serviceTypeDropdown_2.setItemText(0, QCoreApplication.translate("serviceReportDialog", u"Cleaning", None))
        self.serviceTypeDropdown_2.setItemText(1, QCoreApplication.translate("serviceReportDialog", u"Repair", None))
        self.serviceTypeDropdown_2.setItemText(2, QCoreApplication.translate("serviceReportDialog", u"Upgrade", None))

        self.amountPaid_3.setText(QCoreApplication.translate("serviceReportDialog", u"Amount Paid", None))
        self.charge_3.setText(QCoreApplication.translate("serviceReportDialog", u"Charge", None))
        self.change_3.setText(QCoreApplication.translate("serviceReportDialog", u"Change", None))
        self.confirmButton_3.setText(QCoreApplication.translate("serviceReportDialog", u"Confirm", None))
        self.cancelButton_3.setText(QCoreApplication.translate("serviceReportDialog", u"Cancel", None))
    # retranslateUi

