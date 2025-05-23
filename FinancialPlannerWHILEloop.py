# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FinancialPlannerWHILEloop.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 121, 71))
        self.label_2.setObjectName("label_2")
        self.lineEdit_annualcontribution = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_annualcontribution.setGeometry(QtCore.QRect(210, 10, 191, 81))
        self.lineEdit_annualcontribution.setObjectName("lineEdit_annualcontribution")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 110, 201, 81))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 191, 71))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(210, 220, 201, 81))
        self.comboBox.setObjectName("comboBox")

        # Add combobox items for the user to select
        self.comboBox.addItems(["Retirement Plan 2050", "Retirement Plan 2060"])

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 330, 161, 71))
        self.pushButton.setObjectName("pushButton")

        # Activates the calculate_time_taken definition
        self.pushButton.clicked.connect(self.calculate_time_taken)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 420, 181, 71))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(210, 430, 201, 91))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5") #label_result equivalent
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Annual Contribution"))
        self.label_2.setText(_translate("MainWindow", "Target Value"))
        self.label_3.setText(_translate("MainWindow", "Retirement Plan"))
        self.pushButton.setText(_translate("MainWindow", "How long?"))
        self.label_4.setText(_translate("MainWindow", "Time Taken (Years)"))

    def calculate_time_taken(self):

        annual_contribution = float(self.lineEdit_annualcontribution.text())
        target_value = float(self.lineEdit_2.text())
        print("Enter annual contribution ", annual_contribution)
        print("Entered Target Balance", target_value)

        # capture user’s selection from the comboBox
        retirement_plan = self.comboBox.currentText()
        print("Retirement plan selected by user:", retirement_plan)

        # decide return rate
        return_rate = 0.0
        if retirement_plan == "Retirement Plan 2050":
            return_rate = 5.0
        elif retirement_plan == "Retirement Plan 2060":
            return_rate = 6.0
        print("Return rate based on retirement plan:", return_rate)

        portfolio_balance = 0.0
        years_taken = 0
        # portfolio will increase over time; we need to stop when portfolio balance is equal to target_balance
        while portfolio_balance < target_value:
            portfolio_balance = (portfolio_balance + annual_contribution) * (1 + return_rate / 100)
            years_taken = years_taken + 1
            print("portfolio balance:", portfolio_balance, "after years:", years_taken)
        self.label_5.setText(str(years_taken))


if __name__ == '__main__':
    import sys

    application = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    user_interface = Ui_MainWindow()
    user_interface.setupUi(form)
    form.show()
    sys.exit(application.exec_())