#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@Author: SMnRa 
@Email: smnra@163.com
@Project: pyqt5
@File: docToDoc.py
@Time: 2019/05/17 10:53

功能描述: 
直接使用ui文件 加载 软件界面



"""



import os, sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from readDocx import  doc2doc


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            bundle_dir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            bundle_dir = os.path.dirname(os.path.abspath(__file__))
        loadUi(bundle_dir + r'.\ui.ui', self)
        # self.setFixedSize(self.sizeHint())
        self.setFixedSize(490,380)

        # print(self.toolButton.text())
        # self.toolButton.setText("浏览...")
        # self.toolButton_2.setText("浏览...")
        # self.textBrowser.setText(self.textBrowser.toPlainText() + '\n' + self.toolButton.text())
        # print(self.textBrowser.toPlainText())
        self.lineEdit.setText(u'./doc/二年级下册书法教案.docx')
        self.lineEdit_2.setText(u'./doc/tagDir')

        self.toolButton.clicked.connect(self.showFileSelectDialog)
        self.toolButton_2.clicked.connect(self.showDirSelectDialog)
        self.pushButton.clicked.connect(self.okButtonEvent)
        self.textBrowser.setText("...")

    def changeTextEdit(self):
        print(self.toolButton.text())
        self.toolButton.setText("浏览...")
        self.toolButton_2.setText("浏览...")
        self.textBrowser.setText(self.textBrowser.toPlainText() + '\n' + self.toolButton.text())
        print(w.textBrowser.toPlainText())

    def showFileSelectDialog(self):
        # 源文件选择 按钮的槽函数  选择一个doc文件
        fname = QFileDialog.getOpenFileName(self,'open file', self.lineEdit.text(),"All Files (*);;Doc Files (*.Doc);;Docx Files (*.Docx)")
        if fname[0]:
            self.lineEdit.setText(fname[0])

    def showDirSelectDialog(self):
        fname = QFileDialog.getExistingDirectory(self,'Select Dir', self.lineEdit_2.text())
        if fname[0]:
            self.lineEdit_2.setText(fname)

    def okButtonEvent(self):
        self.textBrowser.setText(u"开始...")
        QApplication.processEvents()
        doc2doc(self.lineEdit.text(),self.lineEdit_2.text())
        QApplication.processEvents()
        self.textBrowser.setText(u"转换完成 !")




app = QApplication(sys.argv)
w = MainWindow()


# w.toolButton.text()
# w.toolButton.setText("浏览...")
# w.toolButton_2.setText("浏览...")
# w.textBrowser.setText(w.textBrowser.toPlainText() + '\n' + w.toolButton.text())
# w.textBrowser.toPlainText()



w.show()
sys.exit(app.exec())