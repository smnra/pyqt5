# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import  QMainWindow, QApplication, QAction, qApp

from PyQt5.QtGui import QIcon



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.statusBar().showMessage('Connected OK!')       #设置状态栏消息
        exitAction = QAction(QIcon(r'./image/sql.ico'), '&Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit Application')
        exitAction.triggered.connect(qApp.quit)

        connectAction = QAction(QIcon(r'./image/sql.png'), '&Connect', self)
        connectAction.setShortcut('Ctrl+C')
        connectAction.setStatusTip('Connect to Oracle')
        connectAction.triggered.connect(qApp.aboutQt)         #打开QT 的about 对话框

        menuBar = self.menuBar()                #创建一个菜单栏
        fileMenu = menuBar.addMenu('&File')     #添加一个菜单 File
        fileMenu.addAction(exitAction)          #给菜单添加事件

        fileMenu = menuBar.addMenu('&Connect')     #添加一个菜单 File
        fileMenu.addAction(connectAction)          #给菜单添加事件

        self.toolBar = self.addToolBar('Exit')      #添加一个工具栏按钮
        self.toolBar.addAction(exitAction)          #给工具栏按钮添加动作
        self.toolBar = self.addToolBar('Connect')
        self.toolBar.addAction(connectAction)

        self.setGeometry(300,300,300,200)                         #设置窗口位置和大小, 前两个参数是 窗口左上角的位置, 后两个参数是窗口的宽 和 高
        self.setWindowTitle('Status Bar')                       #设置窗口标题
        self.setWindowIcon(QIcon(r'./image/sql.ico'))          #设置窗口标题栏图标
        self.show()                                               #显示窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())