import cv2
import time
import numpy as np

import multiprocessing
from cvtoolui import Ui_MainWindow
from cv import  *
from PySide6 import QtWidgets,QtCore,QtGui
from PySide6.QtGui import Qt,QPen,QPixmap
from PySide6.QtWidgets import QMainWindow,QGraphicsSceneMouseEvent,QGraphicsScene
import sys
from ui_camera import CamController
from ui_vesc import VescController
from ui_algorithms import Altorithm


class Scene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.setSceneRect(640,480)
        self.point_list=[]
        self.pen=QPen()
        self.pen.setWidth(5)
        self.pen.setColor(Qt.white)

        self.pixmap=QPixmap()
        self.addPixmap(self.pixmap)

        self.rects=[]

    def setSceneRect(self, width,height):
        super().setSceneRect(0,0,width,height)


    def clear_points(self):
        for i in self.rects:
            self.removeItem(i)
        self.point_list.clear()

    def mousePressEvent(self, event:QGraphicsSceneMouseEvent):
        if event.button() & Qt.LeftButton:
            pos = event.scenePos().toTuple()
            x,y=pos
            self.point_list.append(pos)
            rect=self.addRect(x,y,5,5,self.pen)
            self.rects.append(rect)
        elif event.button() & Qt.RightButton:
            self.clear_points()

    def show_qimg(self,qimg):
        self.clear()
        self.pixmap=QPixmap.fromImage(qimg)
        self.addPixmap(self.pixmap)

    def show_img(self,img):
        # img is opencv image
        qimage=cvimg2QImage(img)
        self.show_qimg(qimage)



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.scene = Scene()

        self.ui.graphicsView.setScene(self.scene)

        self.cam_controller=CamController(self.ui)
        self.cam_controller.bind_scene(self.scene)

        self.vesc_controller=VescController(self.ui)
        self.algorithm= Altorithm(self.ui)
        self.algorithm.bind_scene(self.scene)
        self.algorithm.bind_camcontroller(self.cam_controller)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())
"""
toushi_transform("ts.jpg")


#载入并显示图片
img=cv2.imread('test.jpg')
cv2.imshow('img',img)
#灰度化
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#输出图像大小，方便根据图像大小调节minRadius和maxRadius
print(img.shape)
#霍夫变换圆检测
circles= cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,200,param1=300,param2=30,minRadius=10,maxRadius=100)
#输出返回值，方便查看类型
print(circles)
#输出检测到圆的个数
print(len(circles[0]))

print('-------------我是条分割线-----------------')
#根据检测到圆的信息，画出每一个圆
for circle in circles[0]:
    #圆的基本信息
    print(circle[2])
    #坐标行列
    x=int(circle[0])
    y=int(circle[1])
    #半径
    r=int(circle[2]/2)
    #在原图用指定颜色标记出圆的位置
    img=cv2.circle(gray,(x,y),r,(0,0,255),-1)
#显示新图像q
cv2.imshow('res',img)

#按任意键退出
cv2.waitKey(0)
cv2.destroyAllWindows()
"""