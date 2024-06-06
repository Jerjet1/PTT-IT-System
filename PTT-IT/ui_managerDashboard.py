# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'managerDashboard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_managerDashboard(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1100, 657)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.navigationPanel = QFrame(Form)
        self.navigationPanel.setObjectName(u"navigationPanel")
        self.navigationPanel.setFrameShape(QFrame.StyledPanel)
        self.navigationPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.navigationPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inventoryButton_2 = QPushButton(self.navigationPanel)
        self.inventoryButton_2.setObjectName(u"inventoryButton_2")

        self.verticalLayout_3.addWidget(self.inventoryButton_2)

        self.employeeButton_2 = QPushButton(self.navigationPanel)
        self.employeeButton_2.setObjectName(u"employeeButton_2")

        self.verticalLayout_3.addWidget(self.employeeButton_2)

        self.historyButton_2 = QPushButton(self.navigationPanel)
        self.historyButton_2.setObjectName(u"historyButton_2")

        self.verticalLayout_3.addWidget(self.historyButton_2)

        self.serviceReportButton_2 = QPushButton(self.navigationPanel)
        self.serviceReportButton_2.setObjectName(u"serviceReportButton_2")

        self.verticalLayout_3.addWidget(self.serviceReportButton_2)

        self.purchaseButton_2 = QPushButton(self.navigationPanel)
        self.purchaseButton_2.setObjectName(u"purchaseButton_2")

        self.verticalLayout_3.addWidget(self.purchaseButton_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.logOutButton_2 = QPushButton(self.navigationPanel)
        self.logOutButton_2.setObjectName(u"logOutButton_2")

        self.verticalLayout_3.addWidget(self.logOutButton_2)


        self.horizontalLayout.addWidget(self.navigationPanel)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.inventoryPage = QWidget()
        self.inventoryPage.setObjectName(u"inventoryPage")
        self.verticalLayout_4 = QVBoxLayout(self.inventoryPage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.inventoryNavigation = QFrame(self.inventoryPage)
        self.inventoryNavigation.setObjectName(u"inventoryNavigation")
        self.inventoryNavigation.setFrameShape(QFrame.StyledPanel)
        self.inventoryNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.inventoryNavigation)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.addItemButton_2 = QPushButton(self.inventoryNavigation)
        self.addItemButton_2.setObjectName(u"addItemButton_2")

        self.gridLayout_2.addWidget(self.addItemButton_2, 1, 0, 1, 1)

        self.searchBar_2 = QLineEdit(self.inventoryNavigation)
        self.searchBar_2.setObjectName(u"searchBar_2")

        self.gridLayout_2.addWidget(self.searchBar_2, 1, 2, 1, 1)

        self.searchButton_2 = QPushButton(self.inventoryNavigation)
        self.searchButton_2.setObjectName(u"searchButton_2")

        self.gridLayout_2.addWidget(self.searchButton_2, 1, 3, 1, 1)

        self.title_2 = QLabel(self.inventoryNavigation)
        self.title_2.setObjectName(u"title_2")

        self.gridLayout_2.addWidget(self.title_2, 0, 0, 1, 4)


        self.verticalLayout_4.addWidget(self.inventoryNavigation)

        self.inventoryList = QFrame(self.inventoryPage)
        self.inventoryList.setObjectName(u"inventoryList")
        self.inventoryList.setFrameShape(QFrame.StyledPanel)
        self.inventoryList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.inventoryList)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.products_2 = QTableWidget(self.inventoryList)
        if (self.products_2.columnCount() < 6):
            self.products_2.setColumnCount(6)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.products_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.products_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.products_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.products_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.products_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.products_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.products_2.setObjectName(u"products_2")
        self.products_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.products_2.horizontalHeader().setCascadingSectionResizes(False)
        self.products_2.horizontalHeader().setDefaultSectionSize(156)
        self.products_2.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.products_2)


        self.verticalLayout_4.addWidget(self.inventoryList)

        self.stackedWidget.addWidget(self.inventoryPage)
        self.employeePage = QWidget()
        self.employeePage.setObjectName(u"employeePage")
        self.verticalLayout_6 = QVBoxLayout(self.employeePage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.employeeNavigation = QFrame(self.employeePage)
        self.employeeNavigation.setObjectName(u"employeeNavigation")
        self.employeeNavigation.setFrameShape(QFrame.StyledPanel)
        self.employeeNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.employeeNavigation)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.addEmployeeButton = QPushButton(self.employeeNavigation)
        self.addEmployeeButton.setObjectName(u"addEmployeeButton")

        self.gridLayout_3.addWidget(self.addEmployeeButton, 1, 0, 1, 1)

        self.searchBar_3 = QLineEdit(self.employeeNavigation)
        self.searchBar_3.setObjectName(u"searchBar_3")

        self.gridLayout_3.addWidget(self.searchBar_3, 1, 2, 1, 1)

        self.searchButton_3 = QPushButton(self.employeeNavigation)
        self.searchButton_3.setObjectName(u"searchButton_3")

        self.gridLayout_3.addWidget(self.searchButton_3, 1, 3, 1, 1)

        self.title_3 = QLabel(self.employeeNavigation)
        self.title_3.setObjectName(u"title_3")

        self.gridLayout_3.addWidget(self.title_3, 0, 0, 1, 4)


        self.verticalLayout_6.addWidget(self.employeeNavigation)

        self.employeeList = QFrame(self.employeePage)
        self.employeeList.setObjectName(u"employeeList")
        self.employeeList.setFrameShape(QFrame.StyledPanel)
        self.employeeList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.employeeList)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.employees = QTableWidget(self.employeeList)
        if (self.employees.columnCount() < 6):
            self.employees.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.employees.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.employees.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.employees.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.employees.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.employees.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.employees.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.employees.setObjectName(u"employees")
        self.employees.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.employees.horizontalHeader().setDefaultSectionSize(186)
        self.employees.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.employees)


        self.verticalLayout_6.addWidget(self.employeeList)

        self.stackedWidget.addWidget(self.employeePage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.verticalLayout_8 = QVBoxLayout(self.historyPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.historyNavigation = QFrame(self.historyPage)
        self.historyNavigation.setObjectName(u"historyNavigation")
        self.historyNavigation.setFrameShape(QFrame.StyledPanel)
        self.historyNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.historyNavigation)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.title_4 = QLabel(self.historyNavigation)
        self.title_4.setObjectName(u"title_4")

        self.gridLayout_4.addWidget(self.title_4, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.historyNavigation)

        self.historyList = QTabWidget(self.historyPage)
        self.historyList.setObjectName(u"historyList")
        self.historyList.setTabPosition(QTabWidget.North)
        self.historyList.setTabShape(QTabWidget.Rounded)
        self.historyList.setElideMode(Qt.ElideNone)
        self.PurchaseHistory = QWidget()
        self.PurchaseHistory.setObjectName(u"PurchaseHistory")
        self.verticalLayout_9 = QVBoxLayout(self.PurchaseHistory)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.history = QTableWidget(self.PurchaseHistory)
        if (self.history.columnCount() < 7):
            self.history.setColumnCount(7)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.history.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.history.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.history.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.history.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.history.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.history.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.history.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        self.history.setObjectName(u"history")

        self.verticalLayout_9.addWidget(self.history)

        self.historyList.addTab(self.PurchaseHistory, "")
        self.ServiceHistory = QWidget()
        self.ServiceHistory.setObjectName(u"ServiceHistory")
        self.verticalLayout = QVBoxLayout(self.ServiceHistory)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.history_2 = QTableWidget(self.ServiceHistory)
        if (self.history_2.columnCount() < 7):
            self.history_2.setColumnCount(7)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.history_2.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.history_2.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.history_2.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.history_2.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.history_2.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.history_2.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.history_2.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        self.history_2.setObjectName(u"history_2")

        self.verticalLayout.addWidget(self.history_2)

        self.historyList.addTab(self.ServiceHistory, "")

        self.verticalLayout_8.addWidget(self.historyList)

        self.stackedWidget.addWidget(self.historyPage)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)
        self.historyList.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.inventoryButton_2.setText(QCoreApplication.translate("Form", u"Inventory", None))
        self.employeeButton_2.setText(QCoreApplication.translate("Form", u"Employee", None))
        self.historyButton_2.setText(QCoreApplication.translate("Form", u"History", None))
        self.serviceReportButton_2.setText(QCoreApplication.translate("Form", u"Service Report", None))
        self.purchaseButton_2.setText(QCoreApplication.translate("Form", u"Purchase", None))
        self.logOutButton_2.setText(QCoreApplication.translate("Form", u"Log Out", None))
        self.addItemButton_2.setText(QCoreApplication.translate("Form", u"Add Item", None))
        self.searchBar_2.setPlaceholderText(QCoreApplication.translate("Form", u"Product Name...", None))
        self.searchButton_2.setText(QCoreApplication.translate("Form", u"Search", None))
        self.title_2.setText(QCoreApplication.translate("Form", u"INVENTORY", None))
        ___qtablewidgetitem = self.products_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Product ID", None));
        ___qtablewidgetitem1 = self.products_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem2 = self.products_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem3 = self.products_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Price", None));
        ___qtablewidgetitem4 = self.products_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Category", None));
        ___qtablewidgetitem5 = self.products_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Actions", None));
        self.addEmployeeButton.setText(QCoreApplication.translate("Form", u"Add Employee", None))
        self.searchBar_3.setPlaceholderText(QCoreApplication.translate("Form", u"Name...", None))
        self.searchButton_3.setText(QCoreApplication.translate("Form", u"Search", None))
        self.title_3.setText(QCoreApplication.translate("Form", u"EMPLOYEE", None))
        ___qtablewidgetitem6 = self.employees.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Employee ID", None));
        ___qtablewidgetitem7 = self.employees.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Last Name", None));
        ___qtablewidgetitem8 = self.employees.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"First Name", None));
        ___qtablewidgetitem9 = self.employees.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Address", None));
        ___qtablewidgetitem10 = self.employees.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Contact No.", None));
        ___qtablewidgetitem11 = self.employees.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Date Hired", None));
        self.title_4.setText(QCoreApplication.translate("Form", u"TRANSACTION HISTORY", None))
        ___qtablewidgetitem12 = self.history.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Receipt ID", None));
        ___qtablewidgetitem13 = self.history.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Customer Name", None));
        ___qtablewidgetitem14 = self.history.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"product", None));
        ___qtablewidgetitem15 = self.history.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem16 = self.history.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"Price", None));
        ___qtablewidgetitem17 = self.history.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"Total Charge", None));
        ___qtablewidgetitem18 = self.history.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Date Purchase", None));
        self.historyList.setTabText(self.historyList.indexOf(self.PurchaseHistory), "")
        ___qtablewidgetitem19 = self.history_2.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"Service ID", None));
        ___qtablewidgetitem20 = self.history_2.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"Customer Name", None));
        ___qtablewidgetitem21 = self.history_2.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Device", None));
        ___qtablewidgetitem22 = self.history_2.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"Service Type", None));
        ___qtablewidgetitem23 = self.history_2.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"Technician", None));
        ___qtablewidgetitem24 = self.history_2.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"Charge", None));
        ___qtablewidgetitem25 = self.history_2.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"Date", None));
        self.historyList.setTabText(self.historyList.indexOf(self.ServiceHistory), QCoreApplication.translate("Form", u"Page", None))
    # retranslateUi

