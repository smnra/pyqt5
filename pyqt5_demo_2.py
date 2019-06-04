# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox,QDesktopWidget, QLabel, QHBoxLayout, QVBoxLayout, QListView
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('name',self)
        label1.move(50,10)
        label2 = QLabel('text',self)
        label2.move(50,25)
        label3 = QLabel('sex',self)
        label3.move(100,10)
        label4 = QLabel('age',self)
        label4.move(100,25)

        okButton = QPushButton('OK')
        exitButton = QPushButton('Exit')
        stopButton = QPushButton('Stop')
        listbox = QListView()

        hbox = QHBoxLayout()
        hbox.addStretch(0)
        hbox.addWidget(okButton)
        hbox.addWidget(exitButton)
        hbox.addWidget(stopButton)

        vbox = QVBoxLayout()
        vbox.addStretch(0)
        vbox.addWidget(listbox)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setGeometry(200,200,600,400)
        self.setWindowTitle('Pos')
        self.setWindowIcon(QIcon(r'./image/sql.ico'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())