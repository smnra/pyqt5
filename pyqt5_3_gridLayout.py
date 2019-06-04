# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, \
    QPushButton, QMessageBox,QDesktopWidget, QLabel, QHBoxLayout, \
    QVBoxLayout, QListView, QLineEdit, QTextEdit, QGridLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        auth = QLabel('Auth')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authEdit = QLineEdit()
        reviewEdit = QTextEdit()

        tableGrid = QGridLayout()
        tableGrid.setSpacing(15)

        tableGrid.addWidget(title, 1,1)
        tableGrid.addWidget(titleEdit,1,2)
        tableGrid.addWidget(auth, 2,1)
        tableGrid.addWidget(authEdit,2,2)
        tableGrid.addWidget(review, 3,1)
        tableGrid.addWidget(reviewEdit,3,2,6,2)



        self.setLayout(tableGrid)
        self.setGeometry(200,200,350,250)
        self.setWindowTitle('Pos')
        self.setWindowIcon(QIcon(r'./image/sql.ico'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())