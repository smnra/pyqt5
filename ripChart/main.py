# -*- coding: utf-8 -*-
# @Time       : 2020/1/2 15:27
# @Author     : SMnRa
# @Email      : smnra@163.com
# @File       : main.py
# @Software   : PyCharm
# @description: 本脚本的作用为 图表  prbrip_avg


from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
import sys, time,os
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
import matplotlib
import matplotlib.cbook as cbook


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=3.9, height=2.7, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=100)
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)

    def test(self):
        x = [1, 2, 3, 4, 5, 6, 7]
        y = [2, 1, 3, 5, 6, 4, 3]
        self.ax.plot(x, y)


class ImgDisp(QMainWindow):
    def __init__(self, parent=None):
        super(ImgDisp, self).__init__(parent)

        # 当前文件夹路径
        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            bundle_dir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            bundle_dir = os.path.dirname(os.path.abspath(__file__))

        #  载入UI 文件
        loadUi(bundle_dir + r'.\ui.ui', self)

        # 修改窗口大小
        # self.setFixedSize(self.sizeHint())
        self.setFixedSize(850, 480)

        # 生成图表
        self.Init_Widgets()

    def Init_Widgets(self):
        # 渲染画布
        self.PrepareSamples()
        self.PrepareLineCanvas()
        self.PrepareBarCanvas()
        self.PrepareImgCanvas()
        self.PrepareSurfaceCanvas()

    def PrepareSamples(self):
        # 载入数据
        self.x = np.arange(-4, 4, 0.02)  # 三个参数[start, ]stop, [step, ]
        self.y = np.arange(-4, 4, 0.02)
        self.X, self.Y = np.meshgrid(self.x, self.y)  # 生成网格点坐标矩阵
        self.z = np.sin(self.x)
        self.R = np.sqrt(self.X ** 2 + self.Y ** 2)
        self.Z = np.sin(self.R)


    def PrepareLineCanvas(self):
        # 绘制折线图
        self.LineFigure = Figure_Canvas()
        self.LineFigureLayout = QGridLayout(self.LineDisplayGB)
        self.LineFigureLayout.addWidget(self.LineFigure)
        self.LineFigure.ax.set_xlim(-4, 4)  # 限制 x轴范围
        self.LineFigure.ax.set_ylim(-1, 1)  # 限制 y轴范围
        self.line = Line2D(self.x, self.z)
        self.LineFigure.ax.add_line(self.line)

    def PrepareBarCanvas(self):
        # 绘制柱状图
        self.BarFigure = Figure_Canvas()
        self.BarFigureLayout = QGridLayout(self.BarDisplayGB)
        self.BarFigureLayout.addWidget(self.BarFigure)
        self.BarFigure.ax.set_xlim(-4, 4)
        self.BarFigure.ax.set_ylim(-1, 1)
        self.bar = self.BarFigure.ax.bar(np.arange(-4, 4, 0.5), np.sin(np.arange(-4, 4, 0.5)), width=0.4)
        self.patches = self.bar.patches

    def PrepareImgCanvas(self):
        # 绘制圈圈图
        self.ImgFigure = Figure_Canvas()
        self.ImgFigureLayout = QGridLayout(self.ImageDisplayGB)
        self.ImgFigureLayout.addWidget(self.ImgFigure)
        self.ImgFig = self.ImgFigure.ax.imshow(self.Z, cmap='bone')
        self.ImgFig.set_clim(-0.8, 0.8)

    def PrepareSurfaceCanvas(self):
        # 绘制三维图
        self.SurfFigure = Figure_Canvas()
        self.SurfFigureLayout = QGridLayout(self.SurfaceDisplayGB)
        self.SurfFigureLayout.addWidget(self.SurfFigure)
        self.SurfFigure.ax.remove()
        self.ax3d = self.SurfFigure.fig.gca(projection='3d')
        self.Surf = self.ax3d.plot_surface(self.X, self.Y, self.Z, cmap='rainbow')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ImgDisp()
    ui.show()
    sys.exit(app.exec_())