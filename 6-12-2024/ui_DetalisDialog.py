# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DetalisDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_DetailsDialog(object):
    def setupUi(self, DetailsDialog):
        if not DetailsDialog.objectName():
            DetailsDialog.setObjectName(u"DetailsDialog")
        DetailsDialog.resize(300, 300)
        self.verticalLayout = QVBoxLayout(DetailsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DetailsDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontal = QHBoxLayout()
        self.horizontal.setObjectName(u"horizontal")
        self.item = QLabel(self.frame)
        self.item.setObjectName(u"item")

        self.horizontal.addWidget(self.item, 0, Qt.AlignLeft)

        self.itemName = QLineEdit(self.frame)
        self.itemName.setObjectName(u"lineEdit")
        self.itemName.setFixedWidth(150)

        self.horizontal.addWidget(self.itemName, 0, Qt.AlignLeft)


        self.verticalLayout_3.addLayout(self.horizontal)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.category = QLabel(self.frame)
        self.category.setObjectName(u"category")

        self.horizontalLayout_2.addWidget(self.category, 0, Qt.AlignLeft)

        self.categoryName = QLineEdit(self.frame)
        self.categoryName.setObjectName(u"categoryName")
        self.categoryName.setFixedWidth(150)

        self.horizontalLayout_2.addWidget(self.categoryName, 0, Qt.AlignLeft)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignTop)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit, 0, Qt.AlignBottom)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DetailsDialog)

        QMetaObject.connectSlotsByName(DetailsDialog)
    # setupUi

    def retranslateUi(self, DetailsDialog):
        DetailsDialog.setWindowTitle(QCoreApplication.translate("DetailsDialog", u"Dialog", None))
        self.item.setText(QCoreApplication.translate("DetailsDialog", u"Item Name ", None))
        self.category.setText(QCoreApplication.translate("DetailsDialog", u"Category", None))
        self.label_3.setText(QCoreApplication.translate("DetailsDialog", u"Specs", None))
    # retranslateUi

