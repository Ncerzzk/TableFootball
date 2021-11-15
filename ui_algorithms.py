from PySide6 import QtCore
import cv2
import serial
import serial.tools.list_ports
from cvtoolui import *
import numpy as np
from cv import *

class Altorithm:
    def __init__(self,ui:Ui_MainWindow):
        self.ui=ui
        self.scene:QGraphicsScene=None

        self.ui.pushButton_TF_init.clicked.connect(self.transform_init)
        self.ui.pushButton_tf_apply.clicked.connect(self.apply)
        self.ui.pushButton_tf_reset.clicked.connect(self.reset)

        self.ui.pushButton_ball_bycolor.clicked.connect(self.find_ball_by_color)
        self.ui.pushButton_tf_color.clicked.connect(self.transform_plus_color)

    def bind_scene(self,scene):
        self.scene=scene

    def transform_init(self):
        if self.scene is None:
            print("please bind to a scene!")
            return None
        else:
            self.width = int(self.ui.lineEdit_width.text())
            self.height = int(self.ui.lineEdit_height.text())
            dst_point = np.float32([[0, 0], [self.width, 0],
                                    [0, self.height], [self.width, self.height]])
            src_point = np.float32([self.scene.point_list])
            print(self.scene.point_list)
            self.scene.clear_points()
            self.perspective_matrix = cv2.getPerspectiveTransform(src_point, dst_point)
            return self.perspective_matrix

    def apply(self):
        if self.scene is None:
            print("please bind to a scene!")
            return None
        else:
            # there are problems when pximap converting to cv2 image
            qimage=self.scene.pixmap.toImage()
            self.temp_qimage=qimage
            #img=QImage2cvimg(qimage)
            ret,img = self.cam_ctrl.cap.read()
            cv2.warpPerspective(img, self.perspective_matrix, (self.width, self.height))

            self.scene.show_img(img)


    def reset(self):
        if self.temp_qimage is not None:
            self.scene.show_qimg(self.temp_qimage)


    def find_ball_by_color(self):
        #img=QImage2cvimg(self.scene.pixmap.toImage())
        ret,img = self.cam_ctrl.cap.read()
        find_circle_by_color(img)

    def transform_plus_color(self):
        ret,img=self.cam_ctrl.cap.read()
        cv2.warpPerspective(img, self.perspective_matrix, (self.width, self.height))
        find_circle_by_color(img)


    def bind_camcontroller(self,cam):
        self.cam_ctrl=cam
