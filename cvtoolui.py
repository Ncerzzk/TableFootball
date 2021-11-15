# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cvtoolui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 582)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(640, 480))

        self.horizontalLayout.addWidget(self.graphicsView)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.pushButton_com_refresh = QPushButton(self.groupBox)
        self.pushButton_com_refresh.setObjectName(u"pushButton_com_refresh")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.pushButton_com_refresh)

        self.pushButton_connect = QPushButton(self.groupBox)
        self.pushButton_connect.setObjectName(u"pushButton_connect")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_connect)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.lineEdit_pos = QLineEdit(self.groupBox)
        self.lineEdit_pos.setObjectName(u"lineEdit_pos")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_pos)

        self.pushButton_vesc_home = QPushButton(self.groupBox)
        self.pushButton_vesc_home.setObjectName(u"pushButton_vesc_home")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.pushButton_vesc_home)

        self.pushButton_vesc_move = QPushButton(self.groupBox)
        self.pushButton_vesc_move.setObjectName(u"pushButton_vesc_move")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton_vesc_move)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_camID = QLineEdit(self.groupBox_2)
        self.lineEdit_camID.setObjectName(u"lineEdit_camID")
        self.lineEdit_camID.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_camID)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_width = QLineEdit(self.groupBox_2)
        self.lineEdit_width.setObjectName(u"lineEdit_width")
        self.lineEdit_width.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_width)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_height = QLineEdit(self.groupBox_2)
        self.lineEdit_height.setObjectName(u"lineEdit_height")
        self.lineEdit_height.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_height)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_fps = QLineEdit(self.groupBox_2)
        self.lineEdit_fps.setObjectName(u"lineEdit_fps")
        self.lineEdit_fps.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_fps)

        self.pushButton_initcamera = QPushButton(self.groupBox_2)
        self.pushButton_initcamera.setObjectName(u"pushButton_initcamera")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.pushButton_initcamera)

        self.pushButton_capture = QPushButton(self.groupBox_2)
        self.pushButton_capture.setObjectName(u"pushButton_capture")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.pushButton_capture)

        self.splitter.addWidget(self.groupBox_2)
        self.tabWidget_3 = QTabWidget(self.splitter)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3Page1 = QWidget()
        self.tabWidget_3Page1.setObjectName(u"tabWidget_3Page1")
        self.formLayout_3 = QFormLayout(self.tabWidget_3Page1)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.pushButton_TF_init = QPushButton(self.tabWidget_3Page1)
        self.pushButton_TF_init.setObjectName(u"pushButton_TF_init")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pushButton_TF_init)

        self.pushButton_tf_apply = QPushButton(self.tabWidget_3Page1)
        self.pushButton_tf_apply.setObjectName(u"pushButton_tf_apply")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.pushButton_tf_apply)

        self.pushButton_tf_reset = QPushButton(self.tabWidget_3Page1)
        self.pushButton_tf_reset.setObjectName(u"pushButton_tf_reset")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.pushButton_tf_reset)

        self.pushButton_save_matrix = QPushButton(self.tabWidget_3Page1)
        self.pushButton_save_matrix.setObjectName(u"pushButton_save_matrix")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.pushButton_save_matrix)

        self.tabWidget_3.addTab(self.tabWidget_3Page1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.formLayout_4 = QFormLayout(self.tab)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.pushButton_ball_bycolor = QPushButton(self.tab)
        self.pushButton_ball_bycolor.setObjectName(u"pushButton_ball_bycolor")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.pushButton_ball_bycolor)

        self.pushButton_start = QPushButton(self.tab)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.pushButton_start)

        self.pushButton_tf_color = QPushButton(self.tab)
        self.pushButton_tf_color.setObjectName(u"pushButton_tf_color")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.pushButton_tf_color)

        self.tabWidget_3.addTab(self.tab, "")
        self.splitter.addWidget(self.tabWidget_3)

        self.horizontalLayout.addWidget(self.splitter)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 876, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CVTool", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"VESC Controller", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Coms:", None))
        self.pushButton_com_refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pos:", None))
        self.lineEdit_pos.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_vesc_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_vesc_move.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cam ID:", None))
        self.lineEdit_camID.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Width:", None))
        self.lineEdit_width.setText(QCoreApplication.translate("MainWindow", u"640", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.lineEdit_height.setText(QCoreApplication.translate("MainWindow", u"480", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.lineEdit_fps.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.pushButton_initcamera.setText(QCoreApplication.translate("MainWindow", u"Init Camera", None))
        self.pushButton_capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushButton_TF_init.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.pushButton_tf_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.pushButton_tf_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.pushButton_save_matrix.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabWidget_3Page1), QCoreApplication.translate("MainWindow", u"Transform", None))
        self.pushButton_ball_bycolor.setText(QCoreApplication.translate("MainWindow", u"ByColor", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_tf_color.setText(QCoreApplication.translate("MainWindow", u"Transform+Color", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Ball", None))
    # retranslateUi

