# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 469)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lcd_heart = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcd_heart.setGeometry(QtCore.QRect(340, 100, 211, 161))
        self.lcd_heart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcd_heart.setObjectName("lcd_heart")
        self.play_list = QtWidgets.QListWidget(self.centralWidget)
        self.play_list.setGeometry(QtCore.QRect(40, 100, 241, 161))
        self.play_list.setObjectName("play_list")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(130, 70, 54, 17))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(400, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.add = QtWidgets.QPushButton(self.centralWidget)
        self.add.setGeometry(QtCore.QRect(40, 260, 121, 31))
        self.add.setObjectName("add")
        self.delete_2 = QtWidgets.QPushButton(self.centralWidget)
        self.delete_2.setGeometry(QtCore.QRect(160, 260, 121, 31))
        self.delete_2.setObjectName("delete_2")
        self.mi_band = QtWidgets.QPushButton(self.centralWidget)
        self.mi_band.setGeometry(QtCore.QRect(340, 260, 211, 31))
        self.mi_band.setObjectName("mi_band")
        self.prev = QtWidgets.QPushButton(self.centralWidget)
        self.prev.setGeometry(QtCore.QRect(40, 330, 171, 41))
        self.prev.setObjectName("prev")
        self.play = QtWidgets.QPushButton(self.centralWidget)
        self.play.setGeometry(QtCore.QRect(230, 330, 151, 41))
        self.play.setObjectName("play")
        self.next = QtWidgets.QPushButton(self.centralWidget)
        self.next.setGeometry(QtCore.QRect(400, 330, 151, 41))
        self.next.setObjectName("next")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(210, 10, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Adlam")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(40, 238, 241, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.label_play = QtWidgets.QLabel(self.centralWidget)
        self.label_play.setGeometry(QtCore.QRect(40, 310, 511, 20))
        self.label_play.setText("")
        self.label_play.setAlignment(QtCore.Qt.AlignCenter)
        self.label_play.setObjectName("label_play")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 597, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Music"))
        self.label_2.setText(_translate("MainWindow", "Heart Rate"))
        self.add.setText(_translate("MainWindow", "ADD"))
        self.delete_2.setText(_translate("MainWindow", "DELETE"))
        self.mi_band.setText(_translate("MainWindow", "MI BAND"))
        self.prev.setText(_translate("MainWindow", "PREVIOUS"))
        self.play.setText(_translate("MainWindow", "PLAY"))
        self.next.setText(_translate("MainWindow", "NEXT"))
        self.label_3.setText(_translate("MainWindow", "USER INTERFACE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
