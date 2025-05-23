# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GradeGen.ui'
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
        self.EnterScore = QtWidgets.QLabel(self.centralwidget)
        self.EnterScore.setGeometry(QtCore.QRect(20, 30, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.EnterScore.setFont(font)
        self.EnterScore.setObjectName("EnterScore")
        self.EnterScoreLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EnterScoreLineEdit.setGeometry(QtCore.QRect(200, 30, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.EnterScoreLineEdit.setFont(font)
        self.EnterScoreLineEdit.setObjectName("EnterScoreLineEdit")
        self.GenGrade = QtWidgets.QPushButton(self.centralwidget)
        self.GenGrade.setGeometry(QtCore.QRect(10, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.GenGrade.setFont(font)
        self.GenGrade.setObjectName("GenGrade")

        #When generate grade and gpa button clicked it connects to the gen_grade function
        self.GenGrade.clicked.connect(self.gen_grade)

        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(180, 112, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")

        self.Clear.clicked.connect(self.clear)

        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(280, 110, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.Exit.setFont(font)
        self.Exit.setObjectName("Exit")

        self.Exit.clicked.connect(self.exit)

        self.LG = QtWidgets.QLabel(self.centralwidget)
        self.LG.setGeometry(QtCore.QRect(20, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.LG.setFont(font)
        self.LG.setObjectName("LG")
        self.GPA = QtWidgets.QLabel(self.centralwidget)
        self.GPA.setGeometry(QtCore.QRect(20, 310, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.GPA.setFont(font)
        self.GPA.setObjectName("GPA")
        self.LGB = QtWidgets.QLabel(self.centralwidget)
        self.LGB.setGeometry(QtCore.QRect(120, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.LGB.setFont(font)
        self.LGB.setText("")
        self.LGB.setObjectName("LGB")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 300, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
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
        self.EnterScore.setText(_translate("MainWindow", "Enter your score:"))
        self.GenGrade.setText(_translate("MainWindow", "Generate Grade and GPA"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.LG.setText(_translate("MainWindow", "Letter Grade"))
        self.GPA.setText(_translate("MainWindow", "GPA"))

    def clear(self):
        self.EnterScoreLineEdit.clear()
        self.LGB.clear()
        self.GPA.clear()


    #exit the application
    def exit(self):
        application.exit()

    def gen_grade(self):
        score = float(self.EnterScoreLineEdit.text())
        print("User's input is", score)
        if score >= 90:
            self.LGB.setText("A")
            self.GPA.setText("4")
        elif score >= 80:
            self.LGB.setText("B")
            self.GPA.setText("3")
        elif score >= 70:
            self.LGB.setText("C")
            self.GPA.setText("2")
        elif score >= 60:
            self.LGB.setText("D")
            self.GPA.setText("1")
        elif score >= 50:
            self.LGB.setText("F")
            self.GPA.setText("0")



if __name__ == '__main__':
    import sys
    application = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    user_interface = Ui_MainWindow()
    user_interface.setupUi(form)
    form.show()
    sys.exit(application.exec_())