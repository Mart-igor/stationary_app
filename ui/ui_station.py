# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stationxNdeSx.ui'
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
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.data_label = QLabel(self.frame_6)
        self.data_label.setObjectName(u"data_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.data_label.sizePolicy().hasHeightForWidth())
        self.data_label.setSizePolicy(sizePolicy2)
        self.data_label.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_11.addWidget(self.data_label)


        self.verticalLayout_12.addWidget(self.frame_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.load_btn = QPushButton(self.frame_7)
        self.load_btn.setObjectName(u"load_btn")
        self.load_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.load_btn)

        self.name_file_label = QLabel(self.frame_7)
        self.name_file_label.setObjectName(u"name_file_label")

        self.horizontalLayout_6.addWidget(self.name_file_label)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.widget_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.box_y = QComboBox(self.frame_8)
        self.box_y.setObjectName(u"box_y")

        self.horizontalLayout_7.addWidget(self.box_y)

        self.box_x = QComboBox(self.frame_8)
        self.box_x.setObjectName(u"box_x")

        self.horizontalLayout_7.addWidget(self.box_x)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.data_graph_btn = QPushButton(self.widget_3)
        self.data_graph_btn.setObjectName(u"data_graph_btn")
        self.data_graph_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_12.addWidget(self.data_graph_btn)

        self.frame_9 = QFrame(self.widget_3)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.table_data = QTableWidget(self.frame_9)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setMinimumSize(QSize(0, 0))
        self.table_data.setSortingEnabled(False)

        self.horizontalLayout_8.addWidget(self.table_data)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.widget_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_4 = MplWidget(self.frame_10)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.widget_4)


        self.verticalLayout_12.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.home_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.label_3 = QLabel(self.report_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 210, 66, 18))
        self.label_3.setFont(font)
        self.stackedWidget.addWidget(self.report_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        font5 = QFont()
        font5.setFamilies([u"Ubuntu Mono"])
        font5.setStyleStrategy(QFont.PreferDefault)
        self.about_page.setFont(font5)
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

        self.verticalLayout_2.addWidget(self.stackedWidget)


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
        font6 = QFont()
        font6.setBold(False)
        font6.setItalic(False)
        self.add_user_btn.setFont(font6)
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
        font7 = QFont()
        font7.setPointSize(9)
        self.label_9.setFont(font7)

        self.horizontalLayout_5.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.data_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.load_btn.setText(QCoreApplication.translate("MainWindow", u"Load file", None))
        self.name_file_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.data_graph_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
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

