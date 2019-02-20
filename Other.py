# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Other.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 30, 321, 231))
        self.label_2.setText("")
        #IMAGE TWO
        self.label_2.setPixmap(QtGui.QPixmap("city.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 341, 231))
        self.label_3.setText("")
        #IMAGE ONE
        self.label_3.setPixmap(QtGui.QPixmap("balloon.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 290, 161, 41))
        self.label_4.setStyleSheet("font: 16pt \"Lucida Handwriting\";")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 280, 341, 231))
        self.label_7.setStyleSheet("")
        self.label_7.setText("")
        # IMAGE THREE
        self.label_7.setPixmap(QtGui.QPixmap("best.jpg"))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 360, 161, 41))
        self.label_5.setStyleSheet("font: 16pt \"Lucida Handwriting\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(480, 430, 161, 41))
        self.label_6.setStyleSheet("font: 16pt \"Lucida Handwriting\";")
        self.label_6.setObjectName("label_6")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "OtherWindow"))
        self.label_4.setText(_translate("OtherWindow", "Text One"))
        self.label_5.setText(_translate("OtherWindow", "Text Two"))
        self.label_6.setText(_translate("OtherWindow", "Text Three"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
