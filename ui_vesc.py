from PySide6 import QtCore
import cv2
import serial
import serial.tools.list_ports
from cvtoolui import *
import pyvesc

class VESC_Home(metaclass=pyvesc.VESCMessage):
    id = 111
    fields=[]

class VESC_Alive(metaclass=pyvesc.VESCMessage):
    id = 30
    fields=[]

class VescController:
    def __init__(self,ui:Ui_MainWindow):
        self.ui=ui
        self.refresh()
        self.serial:serial.Serial=None

        self.ui.pushButton_connect.clicked.connect(self.connect)
        self.ui.pushButton_com_refresh.clicked.connect(self.refresh)
        self.ui.pushButton_vesc_move.clicked.connect(self.set_pos)
        self.ui.pushButton_vesc_home.clicked.connect(self.home)

    @QtCore.Slot()
    def refresh(self):
        port_list =serial.tools.list_ports.comports()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(map(lambda x:x.name,port_list))

    @QtCore.Slot()
    def connect(self):
        if self.serial is None or not self.serial.is_open:
            com=self.ui.comboBox.currentText()
            try:
                self.serial=serial.Serial(com,"115200")
                self.ui.pushButton_connect.setText("disconnect")
                self.ui.comboBox.setEnabled(False)
            except:
                pass
        else:
            self.ui.pushButton_connect.setText("connect")
            self.serial.close()
            self.ui.comboBox.setEnabled(True)

    def write(self,data):
        if self.serial is not None and self.serial.is_open:
            self.serial.write(data)
        else:
            print("please connect to VESC!")

    def home(self):
        msg=VESC_Home()
        self.write(pyvesc.encode_request(msg))

    def set_pos(self,pos=None):
        if not pos:
            pos = float(self.ui.lineEdit_pos.text())
        print(pos)
        msg=pyvesc.SetPosition(pos)
        self.write(pyvesc.encode(msg))


