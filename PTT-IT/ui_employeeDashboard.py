# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeeDashboard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_employeeDashboard(object):
    def setupUi(self, employeeDashboard):
        if not employeeDashboard.objectName():
            employeeDashboard.setObjectName(u"employeeDashboard")
        employeeDashboard.setEnabled(True)
        employeeDashboard.resize(1149, 666)
        employeeDashboard.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(employeeDashboard)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.navigationPanel = QFrame(employeeDashboard)
        self.navigationPanel.setObjectName(u"navigationPanel")
        self.navigationPanel.setStyleSheet(u"QFrame{\n"
"background-color: rgb(107, 138, 122);\n"
"}")
        self.navigationPanel.setFrameShape(QFrame.StyledPanel)
        self.navigationPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.navigationPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.serviceReportButton = QPushButton(self.navigationPanel)
        self.serviceReportButton.setObjectName(u"serviceReportButton")
        self.serviceReportButton.setMaximumSize(QSize(150, 16777215))
        self.serviceReportButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 120px\n"
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

        self.verticalLayout.addWidget(self.serviceReportButton)

        self.purchaseButton = QPushButton(self.navigationPanel)
        self.purchaseButton.setObjectName(u"purchaseButton")
        self.purchaseButton.setMaximumSize(QSize(150, 16777215))
        self.purchaseButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 120px;\n"
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

        self.verticalLayout.addWidget(self.purchaseButton)

        self.verticalSpacer = QSpacerItem(20, 473, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logOutButton = QPushButton(self.navigationPanel)
        self.logOutButton.setObjectName(u"logOutButton")
        self.logOutButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"margin-left:5px;\n"
"margin-right:5px;\n"
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

        self.verticalLayout.addWidget(self.logOutButton)


        self.horizontalLayout_2.addWidget(self.navigationPanel, 0, Qt.AlignLeft)

        self.inventoryFrame = QFrame(employeeDashboard)
        self.inventoryFrame.setObjectName(u"inventoryFrame")
        self.inventoryFrame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(107, 138, 122);\n"
"}")
        self.inventoryFrame.setFrameShape(QFrame.StyledPanel)
        self.inventoryFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.inventoryFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inventoryNavigation = QFrame(self.inventoryFrame)
        self.inventoryNavigation.setObjectName(u"inventoryNavigation")
        self.inventoryNavigation.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(183, 181, 151);\n"
"}")
        self.inventoryNavigation.setFrameShape(QFrame.StyledPanel)
        self.inventoryNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.inventoryNavigation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.searchButton = QPushButton(self.inventoryNavigation)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 5px;\n"
"font-size:16px;\n"
"text-align: center;\n"
"width: 100px\n"
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

        self.gridLayout.addWidget(self.searchButton, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.searchBar = QLineEdit(self.inventoryNavigation)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setMaximumSize(QSize(500, 16777215))
        self.searchBar.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"width:250px;\n"
"font-size:16px;\n"
"}")

        self.gridLayout.addWidget(self.searchBar, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.inventoryNavigation)

        self.inventoryList = QFrame(self.inventoryFrame)
        self.inventoryList.setObjectName(u"inventoryList")
        self.inventoryList.setStyleSheet(u"QFrame{\n"
"background-color: rgb(183, 181, 151);\n"
"}")
        self.inventoryList.setFrameShape(QFrame.StyledPanel)
        self.inventoryList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.inventoryList)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.products = QTableWidget(self.inventoryList)
        if (self.products.columnCount() < 5):
            self.products.setColumnCount(5)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.products.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.products.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.products.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.products.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.products.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.products.setObjectName(u"products")
        self.products.setStyleSheet(u" QTableWidget {\n"
"background-color: rgba(255, 255, 255, 200); /* Semi-transparent white */\n"
"gridline-color: rgba(0, 0, 0, 50); /* Semi-transparent grid lines */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgba(255, 255, 255, 180); /* Semi-transparent header */\n"
"}")
        self.products.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.products.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.products.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.products.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.products.horizontalHeader().setVisible(True)
        self.products.horizontalHeader().setDefaultSectionSize(190)
        self.products.horizontalHeader().setProperty("showSortIndicator", False)
        self.products.horizontalHeader().setStretchLastSection(True)
        self.products.verticalHeader().setCascadingSectionResizes(False)
        self.products.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.products)


        self.verticalLayout_3.addWidget(self.inventoryList)


        self.horizontalLayout_2.addWidget(self.inventoryFrame)


        self.retranslateUi(employeeDashboard)

        QMetaObject.connectSlotsByName(employeeDashboard)
    # setupUi

    def retranslateUi(self, employeeDashboard):
        employeeDashboard.setWindowTitle(QCoreApplication.translate("employeeDashboard", u"Form", None))
        self.serviceReportButton.setText(QCoreApplication.translate("employeeDashboard", u"Service Report", None))
        self.purchaseButton.setText(QCoreApplication.translate("employeeDashboard", u"Purchase", None))
        self.logOutButton.setText(QCoreApplication.translate("employeeDashboard", u"Log Out", None))
        self.searchButton.setText(QCoreApplication.translate("employeeDashboard", u"Search", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("employeeDashboard", u"Product Name...", None))
        ___qtablewidgetitem = self.products.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("employeeDashboard", u"Product ID", None));
        ___qtablewidgetitem1 = self.products.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("employeeDashboard", u"Name", None));
        ___qtablewidgetitem2 = self.products.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("employeeDashboard", u"Quantity", None));
        ___qtablewidgetitem3 = self.products.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("employeeDashboard", u"Price", None));
        ___qtablewidgetitem4 = self.products.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("employeeDashboard", u"Category", None));
    # retranslateUi

