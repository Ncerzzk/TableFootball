from PySide6 import QtCore
import cv2
from cv import *
from cvtoolui import *

class CamController:
    def __init__(self,ui:Ui_MainWindow):
        self.ui=ui
        self.cap:cv2.VideoCapture=None

        self.ui.pushButton_initcamera.clicked.connect(self.init_camera)
        self.ui.pushButton_capture.clicked.connect(self.capture)
        self.scene:QGraphicsScene=None

    @QtCore.Slot()
    def init_camera(self):
        cap = cv2.VideoCapture(int(self.ui.lineEdit_camID.text()))
        cap.set(cv2.CAP_PROP_FPS, int(self.ui.lineEdit_fps.text()))
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.ui.lineEdit_width.text()))
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.ui.lineEdit_height.text()))
        self.cap = cap
        if self.scene is not None:
            width=int(self.ui.lineEdit_width.text())
            height=int(self.ui.lineEdit_height.text())
            self.scene.setSceneRect(width,height)

    @QtCore.Slot()
    def capture(self):
        ret,frame=(None,None)
        for i in range(10):
            ret,frame = self.cap.read()
            self.scene.show_img(frame)

    def bind_scene(self,scene):
        self.scene=scene











