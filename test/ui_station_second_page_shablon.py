# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stationQchHnO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from mplwidget import MplWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1011, 785)
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget, #home_btn, #main_content, QLineEdit {\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #main_body {\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#footer {\n"
"	background-color: #000;\n"
"}\n"
"\n"
"#add_user_btn {\n"
"	background-color: #1b1b27;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#pushButton {\n"
"	border: 1px solid #cc5bce;\n"
"	border-radius: 16px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton {\n"
"	text-align: left;\n"
"	padding: 3px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#home_btn, #reports_btn, #account_btn  {\n"
"	border-left: 3px solid #cc5bce;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: black; /* \u0426\u0432"
                        "\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white; /* \u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    color: black; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u043c \u0441\u043f\u0438\u0441\u043a\u0435 */\n"
"}")
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
        self.menu_btn = QPushButton(self.frame)
        self.menu_btn.setObjectName(u"menu_btn")
        font = QFont()
        font.setPointSize(14)
        self.menu_btn.setFont(font)
        self.menu_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatJustifyFill))
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.menu_btn, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Noto Serif Thai"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.notifications = QPushButton(self.frame_2)
        self.notifications.setObjectName(u"notifications")
        self.notifications.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        self.notifications.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.notifications, 0, Qt.AlignmentFlag.AlignRight)

        self.signin = QPushButton(self.frame_2)
        self.signin.setObjectName(u"signin")
        self.signin.setFont(font)
        self.signin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.signin, 0, Qt.AlignmentFlag.AlignRight)


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
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.left_menu = QWidget(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy1)
        self.left_menu.setMinimumSize(QSize(50, 0))
        self.left_menu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.left_menu)
        self.widget_2.setObjectName(u"widget_2")
        font2 = QFont()
        font2.setPointSize(12)
        self.widget_2.setFont(font2)
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.frame_3.setFont(font3)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 0, 0)
        self.home_btn = QPushButton(self.frame_3)
        self.home_btn.setObjectName(u"home_btn")
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.home_btn.setFont(font4)
        self.home_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.home_btn.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.home_btn)

        self.reports_btn = QPushButton(self.frame_3)
        self.reports_btn.setObjectName(u"reports_btn")
        self.reports_btn.setFont(font4)
        self.reports_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.reports_btn.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.reports_btn)

        self.account_btn = QPushButton(self.frame_3)
        self.account_btn.setObjectName(u"account_btn")
        self.account_btn.setFont(font4)
        self.account_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.account_btn.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.account_btn)


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
        self.verticalLayout_6.setContentsMargins(5, -1, 0, 0)
        self.help_btn = QPushButton(self.frame_4)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setFont(font2)
        self.help_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.help_btn.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.help_btn)

        self.settings_btn = QPushButton(self.frame_4)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setFont(font2)
        self.settings_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settings_btn.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.settings_btn)

        self.about_btn = QPushButton(self.frame_4)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setFont(font2)
        self.about_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.about_btn.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.about_btn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_content = QWidget(self.main_body)
        self.main_content.setObjectName(u"main_content")
        sizePolicy1.setHeightForWidth(self.main_content.sizePolicy().hasHeightForWidth())
        self.main_content.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.main_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy1.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy1)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        sizePolicy1.setHeightForWidth(self.home_page.sizePolicy().hasHeightForWidth())
        self.home_page.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.home_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_6 = QWidget(self.home_page)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(100, 17))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.next_page_1 = QPushButton(self.widget_6)
        self.next_page_1.setObjectName(u"next_page_1")
        self.next_page_1.setMinimumSize(QSize(0, 17))
        font5 = QFont()
        font5.setPointSize(6)
        self.next_page_1.setFont(font5)

        self.horizontalLayout_7.addWidget(self.next_page_1)


        self.verticalLayout_10.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignRight)

        self.widget_3 = QWidget(self.home_page)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))
        self.widget_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget_3.setAutoFillBackground(False)
        self.verticalLayout_12 = QVBoxLayout(self.widget_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.data_label = QLabel(self.frame_6)
        self.data_label.setObjectName(u"data_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.data_label.sizePolicy().hasHeightForWidth())
        self.data_label.setSizePolicy(sizePolicy2)
        self.data_label.setMaximumSize(QSize(16777215, 100))
        self.data_label.setFont(font)

        self.verticalLayout_11.addWidget(self.data_label)


        self.verticalLayout_12.addWidget(self.frame_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.load_btn = QPushButton(self.frame_10)
        self.load_btn.setObjectName(u"load_btn")
        font6 = QFont()
        font6.setPointSize(10)
        self.load_btn.setFont(font6)
        self.load_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_15.addWidget(self.load_btn)

        self.name_file_label = QLabel(self.frame_10)
        self.name_file_label.setObjectName(u"name_file_label")

        self.verticalLayout_15.addWidget(self.name_file_label)


        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(50, 0))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 0))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.box_x = QComboBox(self.frame_12)
        self.box_x.setObjectName(u"box_x")

        self.horizontalLayout_9.addWidget(self.box_x)

        self.frame_9 = QFrame(self.frame_12)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(25, 0))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_9.addWidget(self.frame_9)

        self.box_y = QComboBox(self.frame_12)
        self.box_y.setObjectName(u"box_y")

        self.horizontalLayout_9.addWidget(self.box_y)


        self.verticalLayout_16.addWidget(self.frame_12)

        self.data_graph_btn = QPushButton(self.frame_11)
        self.data_graph_btn.setObjectName(u"data_graph_btn")
        self.data_graph_btn.setMinimumSize(QSize(0, 0))
        self.data_graph_btn.setFont(font6)
        self.data_graph_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_16.addWidget(self.data_graph_btn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_11)


        self.verticalLayout_12.addWidget(self.frame_7)


        self.verticalLayout_10.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_5 = QWidget(self.home_page)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.table_data = QTableWidget(self.widget_5)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setMinimumSize(QSize(0, 0))
        self.table_data.setSortingEnabled(False)

        self.verticalLayout_14.addWidget(self.table_data)


        self.verticalLayout_10.addWidget(self.widget_5)

        self.widget_91 = QWidget(self.home_page)
        self.widget_91.setObjectName(u"widget_91")
        sizePolicy1.setHeightForWidth(self.widget_91.sizePolicy().hasHeightForWidth())
        self.widget_91.setSizePolicy(sizePolicy1)
        self.widget_91.setMinimumSize(QSize(0, 300))
        self.widget_91.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_13 = QVBoxLayout(self.widget_91)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_4 = MplWidget(self.widget_91)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(0, 0))

        self.verticalLayout_13.addWidget(self.widget_4)


        self.verticalLayout_10.addWidget(self.widget_91)

        self.stackedWidget.addWidget(self.home_page)
        self.second_page = QWidget()
        self.second_page.setObjectName(u"second_page")
        self.verticalLayout_18 = QVBoxLayout(self.second_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_7 = QWidget(self.second_page)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_17 = QVBoxLayout(self.widget_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_13 = QFrame(self.widget_9)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy3)
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        font7 = QFont()
        font7.setFamilies([u"Sans Serif Collection"])
        font7.setPointSize(12)
        self.label_11.setFont(font7)

        self.horizontalLayout_12.addWidget(self.label_11)


        self.verticalLayout_17.addWidget(self.frame_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_20 = QFrame(self.widget_9)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.gran_val = QLineEdit(self.frame_20)
        self.gran_val.setObjectName(u"gran_val")

        self.horizontalLayout_13.addWidget(self.gran_val)


        self.verticalLayout_17.addWidget(self.frame_20)

        self.frame_14 = QFrame(self.widget_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.x_min = QLineEdit(self.frame_15)
        self.x_min.setObjectName(u"x_min")

        self.horizontalLayout_16.addWidget(self.x_min)


        self.horizontalLayout_10.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.x_max = QLineEdit(self.frame_16)
        self.x_max.setObjectName(u"x_max")

        self.horizontalLayout_17.addWidget(self.x_max)


        self.horizontalLayout_10.addWidget(self.frame_16)


        self.verticalLayout_17.addWidget(self.frame_14)

        self.frame_18 = QFrame(self.widget_9)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.optimize = QPushButton(self.frame_18)
        self.optimize.setObjectName(u"optimize")

        self.horizontalLayout_14.addWidget(self.optimize)


        self.verticalLayout_17.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.widget_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.graph_opt = QPushButton(self.frame_19)
        self.graph_opt.setObjectName(u"graph_opt")

        self.horizontalLayout_15.addWidget(self.graph_opt, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_19)


        self.horizontalLayout_8.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.widget_10.setMinimumSize(QSize(300, 0))
        self.widget_10.setMaximumSize(QSize(16777215, 400))
        self.verticalLayout_19 = QVBoxLayout(self.widget_10)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_10)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_19.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tableWidget = QTableWidget(self.widget_10)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(300, 0))

        self.verticalLayout_19.addWidget(self.tableWidget)


        self.horizontalLayout_8.addWidget(self.widget_10, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_18.addWidget(self.widget_7, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_17 = QFrame(self.second_page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.search_k = QPushButton(self.frame_17)
        self.search_k.setObjectName(u"search_k")

        self.horizontalLayout_11.addWidget(self.search_k)

        self.k_1 = QLineEdit(self.frame_17)
        self.k_1.setObjectName(u"k_1")

        self.horizontalLayout_11.addWidget(self.k_1)

        self.k_2 = QLineEdit(self.frame_17)
        self.k_2.setObjectName(u"k_2")

        self.horizontalLayout_11.addWidget(self.k_2)

        self.k_3 = QLineEdit(self.frame_17)
        self.k_3.setObjectName(u"k_3")

        self.horizontalLayout_11.addWidget(self.k_3)

        self.F_score = QLabel(self.frame_17)
        self.F_score.setObjectName(u"F_score")

        self.horizontalLayout_11.addWidget(self.F_score)


        self.verticalLayout_18.addWidget(self.frame_17, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_11 = QWidget(self.second_page)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 10))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.graph_result = QPushButton(self.widget_11)
        self.graph_result.setObjectName(u"graph_result")

        self.horizontalLayout_18.addWidget(self.graph_result, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_18.addWidget(self.widget_11)

        self.widget_8 = QWidget(self.second_page)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_18.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.second_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.label_3 = QLabel(self.report_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 210, 66, 18))
        self.label_3.setFont(font)
        self.stackedWidget.addWidget(self.report_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        font8 = QFont()
        font8.setFamilies([u"Ubuntu Mono"])
        font8.setStyleStrategy(QFont.PreferDefault)
        self.about_page.setFont(font8)
        self.label_4 = QLabel(self.about_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(240, 260, 66, 18))
        self.label_4.setFont(font)
        self.stackedWidget.addWidget(self.about_page)
        self.account_page = QWidget()
        self.account_page.setObjectName(u"account_page")
        self.label_7 = QLabel(self.account_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(400, 440, 66, 18))
        self.label_7.setFont(font)
        self.stackedWidget.addWidget(self.account_page)
        self.help_page = QWidget()
        self.help_page.setObjectName(u"help_page")
        self.label_5 = QLabel(self.help_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 290, 66, 18))
        self.label_5.setFont(font)
        self.stackedWidget.addWidget(self.help_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_6 = QLabel(self.settings_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(380, 430, 66, 18))
        self.label_6.setFont(font)
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_2.addWidget(self.stackedWidget, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.main_content)

        self.right_menu = QWidget(self.main_body)
        self.right_menu.setObjectName(u"right_menu")
        sizePolicy1.setHeightForWidth(self.right_menu.sizePolicy().hasHeightForWidth())
        self.right_menu.setSizePolicy(sizePolicy1)
        self.right_menu.setMinimumSize(QSize(50, 0))
        self.right_menu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.right_menu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.widget = QWidget(self.right_menu)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u"../../../../.designer/icons/user.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.userName = QLineEdit(self.frame_5)
        self.userName.setObjectName(u"userName")

        self.verticalLayout_9.addWidget(self.userName)

        self.email = QLineEdit(self.frame_5)
        self.email.setObjectName(u"email")

        self.verticalLayout_9.addWidget(self.email)

        self.phoneNo = QLineEdit(self.frame_5)
        self.phoneNo.setObjectName(u"phoneNo")

        self.verticalLayout_9.addWidget(self.phoneNo)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.add_user_btn = QPushButton(self.widget)
        self.add_user_btn.setObjectName(u"add_user_btn")
        font9 = QFont()
        font9.setBold(False)
        font9.setItalic(False)
        self.add_user_btn.setFont(font9)
        self.add_user_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.add_user_btn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.right_menu)


        self.verticalLayout.addWidget(self.main_body)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.footer)
        self.label_9.setObjectName(u"label_9")
        font10 = QFont()
        font10.setPointSize(9)
        self.label_9.setFont(font10)

        self.horizontalLayout_5.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"         Stationary App", None))
        self.notifications.setText("")
        self.signin.setText(QCoreApplication.translate("MainWindow", u"Sign in ", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.account_btn.setText(QCoreApplication.translate("MainWindow", u"My account", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.next_page_1.setText(QCoreApplication.translate("MainWindow", u"NEXT PAGE", None))
        self.data_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.load_btn.setText(QCoreApplication.translate("MainWindow", u"Pick File", None))
        self.name_file_label.setText("")
        self.box_x.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c X", None))
        self.box_y.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u044c Y", None))
        self.data_graph_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0440\u043e\u043a\u0430 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u043d\u0438\u0447\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.optimize.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u043a\u043b\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0439", None))
        self.graph_opt.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 ", None))
        self.search_k.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.F_score.setText(QCoreApplication.translate("MainWindow", u"F1-score =?", None))
        self.graph_result.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0442\u0438\u043c\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_2.setText("")
        self.userName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.phoneNo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.add_user_btn.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Created gy idwac, don't copyright 2025", None))
    # retranslateUi

