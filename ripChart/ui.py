# -*- coding: utf-8 -*-
# @Time       : 2020/1/3 11:49
# @Author     : SMnRa
# @Email      : smnra@163.com
# @File       : ui.py.py
# @Software   : PyCharm
# @description: 本脚本的作用为




from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.LineDisplayGB = QtWidgets.QGroupBox(self.centralwidget)
        self.LineDisplayGB.setObjectName("LineDisplayGB")
        self.gridLayout.addWidget(self.LineDisplayGB, 0, 0, 1, 1)

        self.BarDisplayGB = QtWidgets.QGroupBox(self.centralwidget)
        self.BarDisplayGB.setObjectName("BarDisplayGB")
        self.gridLayout.addWidget(self.BarDisplayGB, 0, 1, 1, 1)

        self.ImageDisplayGB = QtWidgets.QGroupBox(self.centralwidget)
        self.ImageDisplayGB.setObjectName("ImageDisplayGB")
        self.gridLayout.addWidget(self.ImageDisplayGB, 1, 0, 1, 1)

        self.SurfaceDisplayGB = QtWidgets.QGroupBox(self.centralwidget)
        self.SurfaceDisplayGB.setObjectName("SurfaceDisplayGB")
        self.gridLayout.addWidget(self.SurfaceDisplayGB, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
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

        self.LineDisplayGB.setTitle(_translate("MainWindow", "Line Display"))
        self.BarDisplayGB.setTitle(_translate("MainWindow", "PRB_2 Display"))
        self.ImageDisplayGB.setTitle(_translate("MainWindow", "PRB_3 Display"))
        self.SurfaceDisplayGB.setTitle(_translate("MainWindow", "PRB_4 Display"))