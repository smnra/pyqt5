# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox,QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitBtn = QPushButton('Quit', self)
        exitBtn.clicked.connect(QCoreApplication.instance().quit)
        exitBtn.resize(exitBtn.sizeHint())
        exitBtn.move(100,200)


        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('微软雅黑', 10))

        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a widget')

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('OK 就哈哈', self)
        btn.setToolTip('This is a <h2>QPushButton</h2> widget')

        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())


        self.setGeometry(300,200,600,400)
        self.center()
        self.setWindowTitle('SMnRa')
        self.setWindowIcon(QIcon(r'./image/sql.ico'))
        #self.resize(250, 150)
        self.show()

    def closeEvent(self,event):
        rep = QMessageBox.question(self,'Message', 'Are you sure?', QMessageBox.Yes |QMessageBox.No |QMessageBox.YesAll,QMessageBox.No)

        if rep == QMessageBox.Yes :
            event.accept()
        elif rep == QMessageBox.No :
            event.ignore()
        else :
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())