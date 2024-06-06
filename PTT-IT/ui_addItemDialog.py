# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addItemDialog.ui'
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

class Ui_addItemDialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.itemName = QLabel(self.frame)
        self.itemName.setObjectName(u"itemName")

        self.horizontalLayout.addWidget(self.itemName)

        self.itemNameInput = QLineEdit(self.frame)
        self.itemNameInput.setObjectName(u"itemNameInput")
        self.itemNameInput.setMinimumSize(QSize(250, 0))
        self.itemNameInput.setMaxLength(30)
        self.itemNameInput.setFrame(True)

        self.horizontalLayout.addWidget(self.itemNameInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.quantity = QLabel(self.frame)
        self.quantity.setObjectName(u"quantity")

        self.horizontalLayout_3.addWidget(self.quantity)

        self.quantityInput = QLineEdit(self.frame)
        self.quantityInput.setObjectName(u"quantityInput")
        self.quantityInput.setMinimumSize(QSize(250, 0))
        self.quantityInput.setMaxLength(30)

        self.horizontalLayout_3.addWidget(self.quantityInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.price = QLabel(self.frame)
        self.price.setObjectName(u"price")

        self.horizontalLayout_4.addWidget(self.price)

        self.priceInput = QLineEdit(self.frame)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setMinimumSize(QSize(250, 0))
        self.priceInput.setMaxLength(30)

        self.horizontalLayout_4.addWidget(self.priceInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.category = QLabel(self.frame)
        self.category.setObjectName(u"category")

        self.horizontalLayout_5.addWidget(self.category)

        self.categoryDropdown = QComboBox(self.frame)
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.setObjectName(u"categoryDropdown")
        self.categoryDropdown.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_5.addWidget(self.categoryDropdown, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 69, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.confirmButton = QPushButton(Dialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_3.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.itemName.setText(QCoreApplication.translate("Dialog", u"Item Name", None))
        self.itemNameInput.setText("")
        self.itemNameInput.setPlaceholderText("")
        self.quantity.setText(QCoreApplication.translate("Dialog", u"Quantity", None))
        self.quantityInput.setText("")
        self.price.setText(QCoreApplication.translate("Dialog", u"Price", None))
        self.category.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.categoryDropdown.setItemText(0, QCoreApplication.translate("Dialog", u"CPU", None))
        self.categoryDropdown.setItemText(1, QCoreApplication.translate("Dialog", u"GPU", None))
        self.categoryDropdown.setItemText(2, QCoreApplication.translate("Dialog", u"Motherboard", None))
        self.categoryDropdown.setItemText(3, QCoreApplication.translate("Dialog", u"RAM", None))
        self.categoryDropdown.setItemText(4, QCoreApplication.translate("Dialog", u"Storage", None))
        self.categoryDropdown.setItemText(5, "")

        self.confirmButton.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

