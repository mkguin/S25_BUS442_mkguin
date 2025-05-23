# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'databaseretreive.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(951, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 260, 661, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 140, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        #When pushButton is clicked connect it to the function retrieve_data
        self.pushButton.clicked.connect(self.retrieve_data)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 951, 22))
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
        self.pushButton.setText(_translate("MainWindow", "Import Data"))

    def establish_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                database="student",
                user="root",
                password="0107"
            )
            msg = QtWidgets.QMessageBox()
            msg.setText("Connection was successfully established!")
            msg.exec_()
        except Exception as e:
            self.connection = None  # <- Important to set this
            msg = QtWidgets.QMessageBox()
            msg.setText("Could not establish connection to the server because: " + str(e))
            msg.exec_()

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText("Could not close connection to the database. " + str(e))
            msg.exec_()

    def retrieve_data(self):
        # establish connection to the DB
        self.establish_connection()

        try:
            # establish cursor
            cursor = self.connection.cursor()

            # execute SQL query (make sure to replace 'your_table_name' with your actual table name)
            cursor.execute("SELECT * FROM student")

            # retrieve resultset based on our SQL command using the cursor
            resultset = cursor.fetchall()

            # print metadata about the columns
            print(cursor.description)

            # Create an empty list of columns; we will add column names to this list
            columns = []

            # Loop through cursor description to extract column names
            for col in cursor.description:
                print(col, col[0])  # This prints the entire column metadata and just the column name
                columns.append(col[0])  # Append column name to list

            columns.append('Eligibility')

            print(columns,len(columns))

            # add the number of columns in the table widget
            self.tableWidget.setColumnCount(len(columns))

            # Add the column names
            self.tableWidget.setHorizontalHeaderLabels(columns)

            self.tableWidget.setRowCount(0)

            for record in resultset:
                print(record)

                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)


                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(record[0])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(record[1])))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(record[2])))

                if (record[2]) > 21:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str('Yes')))
                else:
                    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str('No')))

        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setText("Error retrieving data: " + str(e))
            msg.exec_()

        finally:
            #close connection to the DB
            self.close_connection()


#Run the application
if __name__ == '__main__':
    import sys
    application = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    user_interface = Ui_MainWindow()
    user_interface.setupUi(form)
    form.show()
    sys.exit(application.exec_())