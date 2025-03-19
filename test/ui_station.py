# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stationxnClaY.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(915, 716)
        
        

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))

        self.horizontalLayout_4.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Noto Serif Thai"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.left_menu = QWidget(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMinimumSize(QSize(200, 0))
        self.left_menu.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.left_menu)
        self.widget_2.setObjectName(u"widget_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.widget_2.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.frame_3.setFont(font2)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 0, 0)
        self.home_btn = QPushButton(self.frame_3)
        self.home_btn.setObjectName(u"home_btn")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.home_btn.setFont(font3)
        self.home_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.home_btn)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.pushButton_8)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.pushButton_11)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_content = QWidget(self.main_body)
        self.main_content.setObjectName(u"main_content")
        self.verticalLayout_2 = QVBoxLayout(self.main_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_content)

        self.right_menu = QWidget(self.main_body)
        self.right_menu.setObjectName(u"right_menu")

        self.horizontalLayout.addWidget(self.right_menu)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"sdfafdsafsdfasdfsdfasd", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"acc", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"My account", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

