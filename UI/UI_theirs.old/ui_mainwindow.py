# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Jun 15 10:47:06 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
    
  
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 672)
        MainWindow.setMinimumSize(QtCore.QSize(851, 672))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.labelblanksideicon = QtGui.QLabel(self.centralWidget)
        self.labelblanksideicon.setMaximumSize(QtCore.QSize(10, 30))
        self.labelblanksideicon.setText("")
        self.labelblanksideicon.setObjectName("labelblanksideicon")
        self.horizontalLayout_16.addWidget(self.labelblanksideicon)
        self.labelicon = QtGui.QLabel(self.centralWidget)
        self.labelicon.setMinimumSize(QtCore.QSize(33, 30))
        self.labelicon.setMaximumSize(QtCore.QSize(33, 30))
        self.labelicon.setText("")
        self.labelicon.setPixmap(QtGui.QPixmap(":/images/icon.png"))
        self.labelicon.setScaledContents(True)
        self.labelicon.setObjectName("labelicon")
        self.horizontalLayout_16.addWidget(self.labelicon)
        self.labelcartoonupload = QtGui.QLabel(self.centralWidget)
        self.labelcartoonupload.setMinimumSize(QtCore.QSize(104, 30))
        self.labelcartoonupload.setMaximumSize(QtCore.QSize(104, 30))
        self.labelcartoonupload.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"SimSun\";")
        self.labelcartoonupload.setObjectName("labelcartoonupload")
        self.horizontalLayout_16.addWidget(self.labelcartoonupload)
        self.labelblanksidefeedback = QtGui.QLabel(self.centralWidget)
        self.labelblanksidefeedback.setMinimumSize(QtCore.QSize(0, 30))
        self.labelblanksidefeedback.setText("")
        self.labelblanksidefeedback.setObjectName("labelblanksidefeedback")
        self.horizontalLayout_16.addWidget(self.labelblanksidefeedback)
#        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
#        self.pushButton_2.setMinimumSize(QtCore.QSize(35, 30))
#        self.pushButton_2.setMaximumSize(QtCore.QSize(35, 30))
#        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
#"border:outset;")
#        self.pushButton_2.setObjectName("pushButton_2")
#        self.horizontalLayout_16.addWidget(self.pushButton_2)
#        self.buttonset = QtGui.QPushButton(self.centralWidget)
#        self.buttonset.setMinimumSize(QtCore.QSize(35, 30))
#        self.buttonset.setMaximumSize(QtCore.QSize(35, 30))
#        self.buttonset.setStyleSheet("color: rgb(255, 255, 255);\n"
#"border:outset;")
#        self.buttonset.setObjectName("buttonset")
#        self.horizontalLayout_16.addWidget(self.buttonset)

#        self.buttonmenu = QtGui.QPushButton(self.centralWidget)
#        self.buttonmenu.setMinimumSize(QtCore.QSize(38, 30))
#        self.buttonmenu.setMaximumSize(QtCore.QSize(38, 30))
#        self.buttonmenu.setStyleSheet("border:outset;")
#        self.buttonmenu.setText("")
#        icon = QtGui.QIcon()
#        icon.addPixmap(QtGui.QPixmap(":/images/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#        self.buttonmenu.setIcon(icon)
#        self.buttonmenu.setIconSize(QtCore.QSize(38, 30))
#        self.buttonmenu.setObjectName("buttonmenu")
#        self.horizontalLayout_16.addWidget(self.buttonmenu)

        self.buttonminimize = QtGui.QPushButton(self.centralWidget)
        self.buttonminimize.setMinimumSize(QtCore.QSize(27, 23))
#        self.buttonminimize.setMaximumSize(QtCore.QSize(27, 23))
        self.buttonminimize.setStyleSheet("border:outset;")
        self.buttonminimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonminimize.setIcon(icon1)
        self.buttonminimize.setIconSize(QtCore.QSize(30, 30))
        self.buttonminimize.setObjectName("buttonminimize")
        self.horizontalLayout_16.addWidget(self.buttonminimize)
        self.buttonmaximize = QtGui.QPushButton(self.centralWidget)
        self.buttonmaximize.setMinimumSize(QtCore.QSize(27, 23))
#        self.buttonmaximize.setMaximumSize(QtCore.QSize(27, 23))
        self.buttonmaximize.setStyleSheet("border:outset;")
        self.buttonmaximize.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonmaximize.setIcon(icon2)
        self.buttonmaximize.setIconSize(QtCore.QSize(30, 30))
        self.buttonmaximize.setObjectName("buttonmaximize")
        self.horizontalLayout_16.addWidget(self.buttonmaximize)
        self.buttonclose = QtGui.QPushButton(self.centralWidget)
        self.buttonclose.setMinimumSize(QtCore.QSize(30, 23))
        self.buttonclose.setMaximumSize(QtCore.QSize(30, 23))
        self.buttonclose.setStyleSheet("border:outset;")
        self.buttonclose.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonclose.setIcon(icon3)
        self.buttonclose.setIconSize(QtCore.QSize(30, 30))
        self.buttonclose.setObjectName("buttonclose")
        self.horizontalLayout_16.addWidget(self.buttonclose)
        self.labelblanksidecancel = QtGui.QLabel(self.centralWidget)
        self.labelblanksidecancel.setMaximumSize(QtCore.QSize(17, 30))
        self.labelblanksidecancel.setText("")
        self.labelblanksidecancel.setObjectName("labelblanksidecancel")
        self.horizontalLayout_16.addWidget(self.labelblanksidecancel)
        self.horizontalLayout_16.setStretch(0, 10)
        self.horizontalLayout_16.setStretch(1, 33)
        self.horizontalLayout_16.setStretch(2, 104)
        self.horizontalLayout_16.setStretch(3, 16404)
        self.horizontalLayout_16.setStretch(4, 35)
        self.horizontalLayout_16.setStretch(5, 35)
        self.horizontalLayout_16.setStretch(6, 23)
        self.horizontalLayout_16.setStretch(7, 23)
        self.horizontalLayout_16.setStretch(8, 23)
        self.horizontalLayout_16.setStretch(9, 23)
        self.horizontalLayout_16.setStretch(10, 18)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 105))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(83,83,83,255),stop:0.5 rgba(125,125,125,255),stop:1 rgba(83,83,83,255));"
"border-top-width: 1px;"
#"border-color: rgba (0, 0, 0, 255);"
"border-style: outset;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox) 
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 2, 0, 2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelblank = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelblank.sizePolicy().hasHeightForWidth())
        self.labelblank.setSizePolicy(sizePolicy)
        self.labelblank.setMinimumSize(QtCore.QSize(20, 96))
        self.labelblank.setMaximumSize(QtCore.QSize(27, 130))
        self.labelblank.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:outset")
        self.labelblank.setText("")
        self.labelblank.setObjectName("labelblank")
        self.horizontalLayout_4.addWidget(self.labelblank)
        self.MovieEdit = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MovieEdit.sizePolicy().hasHeightForWidth())
        self.MovieEdit.setSizePolicy(sizePolicy)
        self.MovieEdit.setMinimumSize(QtCore.QSize(68, 96))
        self.MovieEdit.setMaximumSize(QtCore.QSize(90, 105))
        self.MovieEdit.setStyleSheet("\n"
"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(116,116,116, 255),  stop:1 rgba(124,124,124, 255));};\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 12px;\n"
"border:outset\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/Animation Edition2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MovieEdit.setIcon(icon4)
        self.MovieEdit.setIconSize(QtCore.QSize(80, 90))        
        self.MovieEdit.setText("")
        self.MovieEdit.setObjectName("MovieEdit")
        self.horizontalLayout_4.addWidget(self.MovieEdit)
        self.labelarrow = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelarrow.sizePolicy().hasHeightForWidth())
        self.labelarrow.setSizePolicy(sizePolicy)
        self.labelarrow.setMinimumSize(QtCore.QSize(20, 98))
        self.labelarrow.setMaximumSize(QtCore.QSize(29, 130))
        self.labelarrow.setStyleSheet("font: bold 14pt \"SimHei\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color:  rgba(255, 255, 255, 0);"
"border:outset;")
        self.labelarrow.setObjectName("labelarrow")
        self.horizontalLayout_4.addWidget(self.labelarrow)
        self.FormatConvert = QtGui.QPushButton(self.groupBox)
        self.FormatConvert.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FormatConvert.sizePolicy().hasHeightForWidth())
        self.FormatConvert.setSizePolicy(sizePolicy)
        self.FormatConvert.setMinimumSize(QtCore.QSize(68, 96))
        self.FormatConvert.setMaximumSize(QtCore.QSize(90, 105))
        self.FormatConvert.setStyleSheet("\n"
"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(128,128,128, 255),  stop:1 rgba(134,134,134, 255));};\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 12px;\n"
"border:outset;")
        self.FormatConvert.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/format conversion2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FormatConvert.setIcon(icon5)
        self.FormatConvert.setIconSize(QtCore.QSize(80, 98))	
        self.FormatConvert.setObjectName("FormatConvert")
        self.horizontalLayout_4.addWidget(self.FormatConvert)
        self.labelblankbesidecup = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelblankbesidecup.sizePolicy().hasHeightForWidth())
        self.labelblankbesidecup.setSizePolicy(sizePolicy)
        self.labelblankbesidecup.setMaximumSize(QtCore.QSize(1000, 130))
        self.labelblankbesidecup.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:outset;")
        self.labelblankbesidecup.setText("")
        self.labelblankbesidecup.setObjectName("labelblankbesidecup")
        self.horizontalLayout_4.addWidget(self.labelblankbesidecup)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(267, 130))
        self.groupBox_2.setStyleSheet("border:outset;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.labelhello = QtGui.QLabel(self.groupBox_2)
        self.labelhello.setGeometry(QtCore.QRect(12, 12, 199, 16))
        self.labelhello.setStyleSheet("font: bold 10pt \"SimHei\";\n"
"color: rgb(214, 214, 214);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.labelhello.setObjectName("labelhello")
        self.labelworldcup = QtGui.QLabel(self.groupBox_2)
        self.labelworldcup.setGeometry(QtCore.QRect(4, 28, 77, 67))
        self.labelworldcup.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.labelworldcup.setText("")
        self.labelworldcup.setPixmap(QtGui.QPixmap(":/images/world cup.png"))
        self.labelworldcup.setScaledContents(True)
        self.labelworldcup.setObjectName("labelworldcup")
        self.labelvideoedit = QtGui.QLabel(self.groupBox_2)
        self.labelvideoedit.setGeometry(QtCore.QRect(84, 42, 167, 19))
        self.labelvideoedit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"
"\n"
"font: bold 10pt \"SimSun\";")
        self.labelvideoedit.setObjectName("labelvideoedit")
        self.labelvideoconvert = QtGui.QLabel(self.groupBox_2)
        self.labelvideoconvert.setGeometry(QtCore.QRect(84, 68, 167, 16))
        self.labelvideoconvert.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"
"font: bold 10pt \"SimSun\";")
        self.labelvideoconvert.setObjectName("labelvideoconvert")
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_4.setStretch(0, 27)
        self.horizontalLayout_4.setStretch(1, 90)
        self.horizontalLayout_4.setStretch(2, 29)
        self.horizontalLayout_4.setStretch(3, 90)
        self.horizontalLayout_4.setStretch(4, 365)
        self.horizontalLayout_4.setStretch(5, 250)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget = QtGui.QStackedWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_4 = QtGui.QGridLayout(self.page)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        ##主体功能区中的背景
        self.groupBox_3 = QtGui.QGroupBox(self.page)
        self.groupBox_3.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, \n"
                                      "stop:0 rgba(231, 231, 231, 255),  stop:0.954802 rgba(126, 126, 126, 255));")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setContentsMargins(11, 15, 16, 16)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.stackedWidget_2 = QtGui.QStackedWidget(self.groupBox_3)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_4 = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(280, 16777215))
        self.groupBox_4.setStyleSheet("border-width: 2px;\n"
"border-left-style:outset;\n"
"border-left-color: rgb(102,102,102);")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_12 = QtGui.QGridLayout()
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_7.setMinimumSize(QtCore.QSize(242, 68))
        self.groupBox_7.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(149,149, 149, 255), stop:0.954802 rgba(140,140, 140, 255));\n"
"border:outset;")
        self.groupBox_7.setObjectName("groupBox_7")
        self.buttonsave = QtGui.QPushButton(self.groupBox_7)
        self.buttonsave.setGeometry(QtCore.QRect(20, 0, 121, 47))
        self.buttonsave.setStyleSheet(
"QPushButton{background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(77,77,77, 255),  stop:1  rgba(152,152, 152, 255));\n"
"color: rgb(255,255,255); \n"
"border-radius: 6px;\n"
"font: 16px \"微软雅黑\";}\n"

"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(152,152, 152, 255),  stop:1 rgba(77,77,77, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";\n"
"}\n"
""
)
        self.buttonsave.setObjectName("buttonsave")
        
        self.labelSave = QtGui.QLabel(self.groupBox_7);
        self.labelSave.setGeometry(QtCore.QRect(20, 49, 121, 16))
        self.labelSave.setStyleSheet("background-color: rgba(255, 255, 255, 0);border:outset;")  
        iconSave = QtGui.QPixmap(":images/gray_invert.png")
        self.labelSave.setPixmap(iconSave)
        self.labelSave.setObjectName("labelSave")
        
        self.buttonpreview = QtGui.QPushButton(self.groupBox_7)
        self.buttonpreview.setGeometry(QtCore.QRect(149, 0, 121, 47))
        self.buttonpreview.setStyleSheet("QPushButton{background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,82,181, 255),  stop:1 rgba(16,135,251, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";}\n"
"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16,135,251, 255),  stop:1 rgba(0,82,181, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";\n"
"}\n"
"")
        self.buttonpreview.setObjectName("buttonpreview")
        
        self.labelPreview = QtGui.QLabel(self.groupBox_7);
        self.labelPreview.setGeometry(QtCore.QRect(149, 49, 121, 18))
        self.labelPreview.setStyleSheet("background-color: rgba(255, 255, 255, 0);border:outset;")  
        iconPreview = QtGui.QPixmap(":images/bright_invert.png")
        self.labelPreview.setPixmap(iconPreview)
        self.labelPreview.setObjectName("iconPreview")
        
        self.buttoncancelbrowse = QtGui.QPushButton(self.groupBox_7)
        self.buttoncancelbrowse.setGeometry(QtCore.QRect(149, 0, 121, 47))
        self.buttoncancelbrowse.setStyleSheet("QPushButton{background-color:  rgb(255,102,0);\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 14px;}\n"
"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150,150,150, 255),  stop:1 rgba(70,70, 70, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 14px;\n"
"}")
        self.buttoncancelbrowse.setObjectName("buttoncancelbrowse")
        self.verticalLayout_6.addWidget(self.groupBox_7)
        self.gridLayout_12.addLayout(self.verticalLayout_6, 3, 0, 1, 1)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelblankaudioload = QtGui.QLabel(self.groupBox_4)
        self.labelblankaudioload.setMinimumSize(QtCore.QSize(274, 0))
        self.labelblankaudioload.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(157,157, 157, 255), stop:1 rgba(149,149, 149, 255));")
        self.labelblankaudioload.setText("")
        self.labelblankaudioload.setObjectName("labelblankaudioload")
        self.verticalLayout_7.addWidget(self.labelblankaudioload)
        self.gridLayout_12.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy)
        self.groupBox_8.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_8.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(226, 226, 226, 255), stop:0.954802 rgba(157,157, 157, 255));"
"border-style:none")
        self.groupBox_8.setObjectName("groupBox_8")
        self.buttonloadfile = QtGui.QPushButton(self.groupBox_8)
        self.buttonloadfile.setGeometry(QtCore.QRect(26, 23, 230, 41))
        self.buttonloadfile.setStyleSheet("border:outset\n")
        self.buttonloadfile.setText(unicode("导入视频文件", 'UTF8'))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/loadaudiofile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#        self.buttonloadfile.setIcon(icon6)
#        self.buttonloadfile.setIconSize(QtCore.QSize(230, 41))
        self.buttonloadfile.setStyleSheet(
"QPushButton{background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(169,169,169, 255),  stop:0.5 rgba(6,6,6, 255),  stop:0.954802 rgba(169,169,169, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";}\n"
"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1,  stop:0 rgba(6,6,6, 255), stop:0.5 rgba(169,169,169, 255),  stop:0.954802 rgba(6,6,6, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";\n"
"}\n"
                                          );
        self.buttonloadfile.setObjectName("buttonloadfile")
        
        self.lblLoadFile = QtGui.QLabel(self.groupBox_8)
        self.lblLoadFile.setGeometry(QtCore.QRect(26, 65, 230, 24))
        self.lblLoadFile.setText("")
        iconLoadFileInvert = QtGui.QPixmap(QtGui.QPixmap(":/images/loadfile_invert.png"))
#        iconLoadFileInvert.scaled(QtCore.QSize(264, 24))
        self.lblLoadFile.setPixmap(iconLoadFileInvert);                                    
        self.lblLoadFile.setObjectName("lblLoadFile")
        
        self.labellastrecord = QtGui.QLabel(self.groupBox_8)
        self.labellastrecord.setGeometry(QtCore.QRect(36, 102, 81, 20))
        self.labellastrecord.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:outset;")
        self.labellastrecord.setObjectName("labellastrecord")
        self.labelstarttime = QtGui.QLabel(self.groupBox_8)
        self.labelstarttime.setGeometry(QtCore.QRect(19, 172, 95, 16))        
        self.labelstarttime.setStyleSheet("background-color: rgba(255, 255, 255, 0);border:outset;")
        iconStartTime = QtGui.QPixmap(":/images/starttime.png")
        self.labelstarttime.setPixmap(iconStartTime)
        self.labelstarttime.setObjectName("labelstarttime")
        
        self.linetimetitle = QtGui.QFrame(self.groupBox_8)
        self.linetimetitle.setGeometry(QtCore.QRect(8, 232, 261, 1))
        self.linetimetitle.setStyleSheet("")
        self.linetimetitle.setFrameShape(QtGui.QFrame.HLine)
        self.linetimetitle.setFrameShadow(QtGui.QFrame.Sunken)
        self.linetimetitle.setObjectName("linetimetitle")
        
        self.labelendtime = QtGui.QLabel(self.groupBox_8)
        self.labelendtime.setGeometry(QtCore.QRect(19, 204, 91, 16))
        self.labelendtime.setPixmap(QtGui.QPixmap(":/images/endtime.png"))
        self.labelendtime.setStyleSheet("background-color: rgba(255, 255, 255, 0);border:outset;")
        self.labelendtime.setObjectName("labelendtime")
        self.labellastsave = QtGui.QLabel(self.groupBox_8)
        self.labellastsave.setGeometry(QtCore.QRect(36, 123, 81, 20))
        self.labellastsave.setStyleSheet("border:outset;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.labellastsave.setObjectName("labellastsave")
        self.labellastrecordtime = QtGui.QLabel(self.groupBox_8)
        self.labellastrecordtime.setGeometry(QtCore.QRect(120, 102, 151, 20))
        self.labellastrecordtime.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:outset;")
        self.labellastrecordtime.setObjectName("labellastrecordtime")
        self.labellastsavefile = QtGui.QLabel(self.groupBox_8)
        self.labellastsavefile.setGeometry(QtCore.QRect(120, 126, 151, 41))
        self.labellastsavefile.setWordWrap(True)
        self.labellastsavefile.setAlignment (QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.labellastsavefile.setStyleSheet("background-color: rgba(255, 255, 255, 0);border:outset;")
        self.labellastsavefile.setObjectName("labellastsavefile")
        self.lineeditstarttime = QtGui.QLineEdit(self.groupBox_8)
        self.lineeditstarttime.setGeometry(QtCore.QRect(113, 167, 156, 20))
        self.lineeditstarttime.setReadOnly(True)
        self.lineeditstarttime.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
#"border-style:groove;\n"
#"border-width:2px;\n"
"border-top-color: rgb(105, 105, 105);")
        self.lineeditstarttime.setObjectName("lineeditstarttime")
        self.lineeditendtime = QtGui.QLineEdit(self.groupBox_8)
        self.lineeditendtime.setGeometry(QtCore.QRect(113, 200, 156, 20))
        self.lineeditendtime.setReadOnly(True)
        self.lineeditendtime.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
#"border-style:groove;\n"
#"border-width:2px;\n"
"border-top-color: rgb(105, 105, 105);")
        self.lineeditendtime.setObjectName("lineeditendtime")
        self.lineeditleadertitle = QtGui.QLineEdit(self.groupBox_8)
        self.lineeditleadertitle.setGeometry(QtCore.QRect(113, 242, 156, 20))
        self.lineeditleadertitle.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
#"border-style:groove;\n"
#"border-width:1px;\n"
"border-top-color: rgb(105, 105, 105);")
        self.lineeditleadertitle.setObjectName("lineeditleadertitle")
        self.checkboxleadertitle = QtGui.QCheckBox(self.groupBox_8)
        self.checkboxleadertitle.setGeometry(QtCore.QRect(19, 244, 85, 18))
        iconLeaderTitle = QtGui.QIcon()
        iconLeaderTitle.addPixmap(QtGui.QPixmap(":images/leadertitle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)        
        self.checkboxleadertitle.setIcon(QtGui.QIcon(iconLeaderTitle))
        self.checkboxleadertitle.setIconSize(QtCore.QSize(65, 15))
        self.checkboxleadertitle.setStyleSheet("background-color: rgba(255, 255, 255, 0);color:#FFFFFF; font-size:16px;")
        self.checkboxleadertitle.setObjectName("checkboxleadertitle")	
        self.verticalLayout_8.addWidget(self.groupBox_8)
        self.gridLayout_12.addLayout(self.verticalLayout_8, 1, 0, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_9.setMaximumSize(QtCore.QSize(276, 38))
        self.groupBox_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:outset;"
"font: 75 11pt \"SimSun\";\n"
"color: rgb(255, 255, 255);")
        self.groupBox_9.setObjectName("groupBox_9")
        self.buttonvideointercept = QtGui.QPushButton(self.groupBox_9)
        self.buttonvideointercept.setGeometry(QtCore.QRect(1, 1, 142, 38))
        self.buttonvideointercept.setMinimumSize(QtCore.QSize(0, 38))
        self.buttonvideointercept.setMaximumSize(QtCore.QSize(16777215, 38))
        self.buttonvideointercept.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(114, 114,114, 255),  stop:1 rgba(201, 201,201, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"SimSun\";"
"border:outset")
        self.buttonvideointercept.setObjectName("buttonvideointercept")
        self.buttonvideomerge = QtGui.QPushButton(self.groupBox_9)
        self.buttonvideomerge.setGeometry(QtCore.QRect(142, 1, 139, 38))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonvideomerge.sizePolicy().hasHeightForWidth())
        self.buttonvideomerge.setSizePolicy(sizePolicy)
        self.buttonvideomerge.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(117,117,117, 255),  stop:0.954802 rgba(26,26, 26, 255));\n"
"border:outset;"
"font: 12pt \"SimSum\";"
"color: rgb(204, 204, 204);")
        self.buttonvideomerge.setObjectName("buttonvideomerge")
        self.gridLayout_12.addWidget(self.groupBox_9, 0, 0, 1, 1)	
        self.gridLayout_12.setRowStretch(0, 10)
        self.gridLayout_12.setRowStretch(1, 90)
        self.gridLayout_12.setRowStretch(2, 5)
        self.gridLayout_12.setRowStretch(3, 15)
        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_8)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_5 = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupbox7 = QtGui.QGroupBox(self.groupBox_5);
        self.groupbox7.setStyleSheet("border-image: url(:/images/bj_control.png);")
        self.groupbox7.setMinimumSize(QtCore.QSize(600, 44))
        self.groupbox7.setMaximumSize(QtCore.QSize(5740, 44))
        sizepolicy7 = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)     
        self.groupbox7.setSizePolicy(sizepolicy7);
#        self.horizontalLayout_7.addWidget(self.groupbox7);
        
        self.groupBox_6 = QtGui.QGroupBox(self.groupbox7)
        self.groupBox_6.setGeometry(QtCore.QRect(1, 0, 140, 44))
        self.groupBox_6.setMinimumSize(QtCore.QSize(140, 16777215))
        self.groupBox_6.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_6.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")	
        self.labelduration = QtGui.QLabel(self.groupBox_6)
        self.labelduration.setGeometry(QtCore.QRect(1, 11, 139, 19))
        self.labelduration.setStyleSheet("border-style:none;background-color: rgba(255, 255, 255, 0);border-image:none;color:rgb(255,255,255);font:12px\n")
        self.labelduration.setText("")
        self.labelduration.setObjectName("labelduration")
        
#        self.horizontalLayout_7.addWidget(self.groupBox_6)
        self.labelblankbesideduration = QtGui.QLabel(self.groupbox7)
        self.labelblankbesideduration.setGeometry(QtCore.QRect(142, 0, 58, 44))
        self.labelblankbesideduration.setMaximumSize(QtCore.QSize(258, 16777215))
        self.labelblankbesideduration.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.labelblankbesideduration.setText("")
        self.labelblankbesideduration.setObjectName("labelblankbesideduration")
#        self.horizontalLayout_7.addWidget(self.labelblankbesideduration)                
        self.buttonplayerstop = QtGui.QPushButton(self.groupbox7)
        self.buttonplayerstop.setGeometry(QtCore.QRect(150, 0, 51, 44))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonplayerstop.sizePolicy().hasHeightForWidth())
        self.buttonplayerstop.setSizePolicy(sizePolicy)
        self.buttonplayerstop.setMaximumSize(QtCore.QSize(51, 2000))
        self.buttonplayerstop.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.buttonplayerstop.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonplayerstop.setIcon(icon7)
        self.buttonplayerstop.setObjectName("buttonplayerstop")
#        self.horizontalLayout_7.addWidget(self.buttonplayerstop)
        self.buttonplayerbackward = QtGui.QPushButton(self.groupbox7)
        self.buttonplayerbackward.setGeometry(QtCore.QRect(200, 0, 41, 44))
        self.buttonplayerbackward.setMaximumSize(QtCore.QSize(51, 2000))
        self.buttonplayerbackward.setStyleSheet("border-style:none;border-image:none;background-color:transparent")                
        self.buttonplayerbackward.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonplayerbackward.setIcon(icon8)
        self.buttonplayerbackward.setObjectName("buttonplayerbackward")
#        self.horizontalLayout_7.addWidget(self.buttonplayerbackward)
        self.buttonplayerplay = QtGui.QPushButton(self.groupbox7)
        self.buttonplayerplay.setGeometry(QtCore.QRect(240, 0, 73, 44))
        self.buttonplayerplay.setMaximumSize(QtCore.QSize(103, 2000))
        self.buttonplayerplay.setStyleSheet("border-style:none;border-image:none;background-color:transparent")                      
        self.buttonplayerplay.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonplayerplay.setIcon(icon9)
        self.buttonplayerplay.setIconSize(QtCore.QSize(36, 36))
        self.buttonplayerplay.setObjectName("buttonplayerplay")
#        self.horizontalLayout_7.addWidget(self.buttonplayerplay)
        self.buttonplayerforward = QtGui.QPushButton(self.groupbox7)
        self.buttonplayerforward.setGeometry(QtCore.QRect(312, 0, 41, 44))
        self.buttonplayerforward.setMaximumSize(QtCore.QSize(51, 2000))
        self.buttonplayerforward.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.buttonplayerforward.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonplayerforward.setIcon(icon10)
        self.buttonplayerforward.setObjectName("buttonplayerforward")
#        self.horizontalLayout_7.addWidget(self.buttonplayerforward)
        self.labelblankbesideforward = QtGui.QLabel(self.groupbox7)
        self.labelblankbesideforward.setGeometry(QtCore.QRect(353, 0, 20, 44))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelblankbesideforward.sizePolicy().hasHeightForWidth())
        self.labelblankbesideforward.setSizePolicy(sizePolicy)
        self.labelblankbesideforward.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.labelblankbesideforward.setText("")
        self.labelblankbesideforward.setObjectName("labelblankbesideforward")
#        self.horizontalLayout_7.addWidget(self.labelblankbesideforward)                	
        self.buttonvolume = QtGui.QPushButton(self.groupbox7)
        self.buttonvolume.setGeometry(QtCore.QRect(373, 0, 41, 44))
        self.buttonvolume.setMaximumSize(QtCore.QSize(49, 2000))

        self.buttonvolume.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.buttonvolume.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonvolume.setIcon(icon11)
        self.buttonvolume.setObjectName("buttonvolume")
#        self.horizontalLayout_7.addWidget(self.buttonvolume)
        self.labelblankbesidevolume = QtGui.QLabel(self.groupbox7)
        self.labelblankbesidevolume.setGeometry(QtCore.QRect(414, 0, 8, 44))
        self.labelblankbesidevolume.setMaximumSize(QtCore.QSize(8, 16777215))
        self.labelblankbesidevolume.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.labelblankbesidevolume.setText("")
        self.labelblankbesidevolume.setObjectName("labelblankbesidevolume")
#        self.horizontalLayout_7.addWidget(self.labelblankbesidevolume)
        self.groupboxvolume = QtGui.QGroupBox(self.groupbox7)
        self.groupboxvolume.setGeometry(QtCore.QRect(422, 0, 80, 46))
        self.groupboxvolume.setTitle("")
        self.groupboxvolume.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.slidervolume = QtGui.QSlider(self.groupboxvolume)
        self.slidervolume.setGeometry(QtCore.QRect(0, 0, 80, 44))
        self.slidervolume.setStyleSheet(
 "QSlider::groove:horizontal {"                                      
     "border: 1px solid #999999;"
     "height:1px; }" 
"QSlider::handle:horizontal {"
"background-image:url(:/images/volume_round.png);"
    "width: 9px;margin:-3px, -3px,-3px,-3px;"
    "border:1px"
    "}"
"QSlider::sub-page:horizontal{"
 "background:rgb(102,102,102);"
"border-radius:5px;}"
"QSlider::add-page:horizontal{"
 "background:rgb(27,47,65);"
"border-radius:20px;};"                                  
)
        self.slidervolume.setOrientation(QtCore.Qt.Horizontal)
        self.slidervolume.setObjectName("slidervolume")
#        self.horizontalLayout_7.addWidget(self.slidervolume)
        self.labelblankbesideslider = QtGui.QLabel(self.groupbox7)
        self.labelblankbesideslider.setGeometry(QtCore.QRect(523, 0, 16, 44))
        self.labelblankbesideslider.setMaximumSize(QtCore.QSize(16, 16777215))
        self.labelblankbesideslider.setStyleSheet("border-style:none;border-image:none;background-color:transparent")
        self.labelblankbesideslider.setText("")
        self.labelblankbesideslider.setObjectName("labelblankbesideslider")
#        self.horizontalLayout_7.addWidget(self.labelblankbesideslider)
#        self.horizontalLayout_7.setStretch(0, 14)
#        self.horizontalLayout_7.setStretch(1, 2)
#        self.horizontalLayout_7.setStretch(2, 6)
#        self.horizontalLayout_7.setStretch(3, 6)
#        self.horizontalLayout_7.setStretch(4, 12)
#        self.horizontalLayout_7.setStretch(5, 6)
#        self.horizontalLayout_7.setStretch(6, 1)
#        self.horizontalLayout_7.setStretch(7, 6)
#        self.horizontalLayout_7.setStretch(8, 1)
#        self.horizontalLayout_7.setStretch(9, 8)
#        self.horizontalLayout_7.setStretch(10, 2)
#        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.groupbox7)
        self.gridLayout_10.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/filmleft.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)        
        self.frame_2 = QtGui.QFrame(self.groupBox_5)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_11.addWidget(self.frame_2)
        self.label = QtGui.QLabel(self.groupBox_5)
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/filmright.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_11.addWidget(self.label)
        self.horizontalLayout_11.setStretch(0, 5)
        self.horizontalLayout_11.setStretch(1, 80)
        self.horizontalLayout_11.setStretch(2, 5)
        self.gridLayout_10.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)        
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(6, 16777215))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)       
        self.sliderseek = QtGui.QSlider(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliderseek.sizePolicy().hasHeightForWidth())
        self.sliderseek.setSizePolicy(sizePolicy)
        self.sliderseek.setMinimumSize(QtCore.QSize(520, 24))
        self.sliderseek.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sliderseek.setStyleSheet("\n"
"QSlider::groove:horizontal {"
"     border: 1px solid #999999;"
"     height:3px;"
"     left: 10px; right:10px;}"
"QSlider::handle:horizontal {"
"  border-image:url(:/images/round.png);"
"    width: 13px;"
"    margin:-3px, -3px,-3px,-3px;} "
"QSlider::sub-page:horizontal{"
" background:rgb(102,102,102);"
"border-radius:5px;}"
"QSlider::add-page:horizontal{"
" background:rgb(255,255,255);"
"border-radius:20px; };"
"background-color: rgb(0, 0, 0);")
        self.sliderseek.setOrientation(QtCore.Qt.Horizontal)
        self.sliderseek.setObjectName("sliderseek")
        self.horizontalLayout_12.addWidget(self.sliderseek)
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(6, 16777215))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border:outset\n")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)        
        self.gridLayout_10.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.gridLayout_10.setRowStretch(0, 372)
        self.gridLayout_10.setRowStretch(1, 24)
        self.gridLayout_10.setRowStretch(2, 44)
        self.gridLayout_11.addLayout(self.gridLayout_10, 1, 0, 1, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_10.setMinimumSize(QtCore.QSize(0, 38))
        self.groupBox_10.setStyleSheet("background-color: rgb(0, 0, 0);""border:outset")
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem = QtGui.QSpacerItem(146, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)	
        self.labelfilmtitle = QtGui.QLabel(self.groupBox_10)
        self.labelfilmtitle.setMinimumSize(QtCore.QSize(200, 0))
        self.labelfilmtitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelfilmtitle.setText("")
        self.labelfilmtitle.setObjectName("labelfilmtitle")
        self.horizontalLayout_14.addWidget(self.labelfilmtitle)
        spacerItem1 = QtGui.QSpacerItem(146, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.gridLayout_11.addWidget(self.groupBox_10, 0, 0, 1, 1)        
        self.gridLayout_7.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_7)
        self.horizontalLayout_6.setStretch(0, 280)
        self.horizontalLayout_6.setStretch(1, 542)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.stackedWidget_2.addWidget(self.tab)
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_15 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox_11 = QtGui.QGroupBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.groupBox_11.setMinimumSize(QtCore.QSize(0, 130))
        self.groupBox_11.setMaximumSize(QtCore.QSize(2000, 150))
        self.groupBox_11.setStyleSheet("background-color: rgb(242, 242, 242);"
"/*border:outset;*/")
        self.groupBox_11.setObjectName("groupBox_11")
        self.labelfilename = QtGui.QLabel(self.groupBox_11)
        self.labelfilename.setGeometry(QtCore.QRect(8, 38, 61, 21))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(9)
        self.labelfilename.setFont(font)
        self.labelfilename.setObjectName("labelfilename")
        self.labeloutputset = QtGui.QLabel(self.groupBox_11)
        self.labeloutputset.setGeometry(QtCore.QRect(6, 6, 91, 21))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        font.setPointSize(13)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.labeloutputset.setFont(font)
        self.labeloutputset.setStyleSheet("font: bold 13pt \"SimHei\";")
        self.labeloutputset.setObjectName("labeloutputset")
        self.labelsaveto = QtGui.QLabel(self.groupBox_11)
        self.labelsaveto.setGeometry(QtCore.QRect(6, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(9)
        self.labelsaveto.setFont(font)
        self.labelsaveto.setObjectName("labelsaveto")
        self.buttonbrowse = QtGui.QPushButton(self.groupBox_11)
        self.buttonbrowse.setGeometry(QtCore.QRect(460, 80, 75, 23))
        self.buttonbrowse.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"border-right-color: rgb(105, 105, 105);\n"
"border-bottom-color: rgb(105, 105, 105);\n"
"border-width:2px;\n"
"background-color: rgb(242, 242, 242);\n"
"border-style:inset;\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);}\n"
"QPushButton::pressed {border-bottom-color: rgb(255, 255, 255);\n"
"border-width:2px;\n"
"background-color: rgb(242, 242, 242);\n"
"border-style:ridge;\n"
"border-top-color: rgb(105, 105, 105);\n"
"border-left-color: rgb(105, 105, 105);\n"
"border-right-color: rgb(255, 255, 255);\n"
"}\n")
        self.buttonbrowse.setObjectName("buttonbrowse")
        self.lineeditfilenameblank = QtGui.QLineEdit(self.groupBox_11)
        self.lineeditfilenameblank.setGeometry(QtCore.QRect(64, 38, 385, 25))
        self.lineeditfilenameblank.setStyleSheet("background-color: white;\n"
"border-bottom-color: rgb(152, 152, 152);\n"
"border-right-color: rgb(152, 152, 152);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-top-color: rgb(101,101,101);\n"
"border-left-color: rgb(101, 101, 101);\n"
"")
        self.lineeditfilenameblank.setText("")
        self.lineeditfilenameblank.setObjectName("lineeditfilenameblank")
        self.lineeditsaveblank = QtGui.QLineEdit(self.groupBox_11)
        self.lineeditsaveblank.setGeometry(QtCore.QRect(64, 79, 385, 25))
        self.lineeditsaveblank.setStyleSheet("background-color: white;\n"
"border-bottom-color: rgb(152, 152, 152);\n"
"border-right-color: rgb(152, 152, 152);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 5px;\n"
"border-top-color: rgb(101,101,101);\n"
"border-left-color: rgb(101, 101, 101);\n"
"")
        self.lineeditsaveblank.setObjectName("lineeditsaveblank")
        self.verticalLayout_10.addWidget(self.groupBox_11)
        self.gridLayout_14.addLayout(self.verticalLayout_10, 1, 0, 1, 1)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_12 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_12.setMinimumSize(QtCore.QSize(0, 38))
        self.groupBox_12.setMaximumSize(QtCore.QSize(16777215, 38))
        self.groupBox_12.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(117,117,117, 255),  stop:0.954802 rgba(26,26, 26, 255));"
"border:outset;")
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.buttonvideointerceptpage = QtGui.QPushButton(self.groupBox_12)
        self.buttonvideointerceptpage.setMinimumSize(QtCore.QSize(0, 38))
        self.buttonvideointerceptpage.setMaximumSize(QtCore.QSize(137, 38))
        self.buttonvideointerceptpage.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(117,117,117, 255),  stop:0.954802 rgba(26,26, 26, 255));\n"
"border:outset;\n"
"color: rgb(204, 204, 204);\n"
"font: 12pt \"SimSun\";")
        self.buttonvideointerceptpage.setObjectName("buttonvideointerceptpage")
        self.horizontalLayout_13.addWidget(self.buttonvideointerceptpage)
        self.buttonvideomergepage = QtGui.QPushButton(self.groupBox_12)
        self.buttonvideomergepage.setMinimumSize(QtCore.QSize(0, 38))
        self.buttonvideomergepage.setMaximumSize(QtCore.QSize(137, 38))
        self.buttonvideomergepage.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(114, 114,114, 255),  stop:1 rgba(201, 201,201, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"SimSun\";"
"border:outset")
        self.buttonvideomergepage.setObjectName("buttonvideomergepage")
        self.horizontalLayout_13.addWidget(self.buttonvideomergepage)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)	
        self.buttonplus = QtGui.QPushButton(self.groupBox_12)
        self.buttonplus.setMinimumSize(QtCore.QSize(0, 38))
        self.buttonplus.setMaximumSize(QtCore.QSize(35, 16777215))
        self.buttonplus.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border:outset")        
        self.buttonplus.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonplus.setIcon(icon12)
        self.buttonplus.setIconSize(QtCore.QSize(23, 24))        
        self.buttonplus.setObjectName("buttonplus")
        self.horizontalLayout_13.addWidget(self.buttonplus)
        self.buttonup = QtGui.QPushButton(self.groupBox_12)
        self.buttonup.setMinimumSize(QtCore.QSize(0, 38))
        self.buttonup.setMaximumSize(QtCore.QSize(35, 16777215))
        self.buttonup.setStyleSheet("background-color: rgba(255, 255, 255, 0);"
"border:outset")        
        self.buttonup.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonup.setIcon(icon13)
        self.buttonup.setIconSize(QtCore.QSize(21, 24))
        self.buttonup.setObjectName("buttonup")
        self.horizontalLayout_13.addWidget(self.buttonup)
        self.buttondown = QtGui.QPushButton(self.groupBox_12)
        self.buttondown.setMinimumSize(QtCore.QSize(0, 38))
        self.buttondown.setMaximumSize(QtCore.QSize(35, 16777215))
        self.buttondown.setStyleSheet("background-color: rgba(255, 255, 255, 0);"
"border:outset")
        self.buttondown.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttondown.setIcon(icon14)
        self.buttondown.setIconSize(QtCore.QSize(22, 24))	
        self.buttondown.setObjectName("buttondown")
        self.horizontalLayout_13.addWidget(self.buttondown)
        self.buttondelete = QtGui.QPushButton(self.groupBox_12)
        self.buttondelete.setMinimumSize(QtCore.QSize(0, 38))
        self.buttondelete.setMaximumSize(QtCore.QSize(35, 16777215))
        self.buttondelete.setStyleSheet("background-color: rgba(255, 255, 255, 0);"
"border:outset")
        self.buttondelete.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttondelete.setIcon(icon15)
        self.buttondelete.setIconSize(QtCore.QSize(21, 24))
        self.buttondelete.setObjectName("buttondelete")
        self.horizontalLayout_13.addWidget(self.buttondelete)
        self.label_5 = QtGui.QLabel(self.groupBox_12)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_13.addWidget(self.label_5)
        self.horizontalLayout_13.setStretch(0, 137)
        self.horizontalLayout_13.setStretch(1, 137)
        self.horizontalLayout_13.setStretch(2, 387)
        self.horizontalLayout_13.setStretch(3, 35)
        self.horizontalLayout_13.setStretch(4, 35)
        self.horizontalLayout_13.setStretch(5, 35)
        self.horizontalLayout_13.setStretch(6, 35)
        self.horizontalLayout_13.setStretch(7, 12)	
        self.verticalLayout_12.addWidget(self.groupBox_12)
        self.mergeview = QtGui.QTreeView(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mergeview.sizePolicy().hasHeightForWidth())
        self.mergeview.setSizePolicy(sizePolicy)
        self.mergeview.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mergeview.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mergeview.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mergeview.setStyleSheet("\n"
"background-color:white;\n"
"border:outset;\n")
        self.mergeview.setAutoScroll(False)
        self.mergeview.setAutoScrollMargin(16)
        self.mergeview.setObjectName("mergeview")
        self.mergeviewheader = QtGui.QHeaderView (QtCore.Qt.Horizontal, self.mergeview)
        self.mergeviewheader.setStyleSheet("\n"
"QHeaderView::section {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(202,202,202, 255));\n"
"height: 30px;\n"
"border-bottom-width:1px;\n"
"border-right-width:1px;\n"
"border-color:rgb(102,102,102);"
"border-style:outset;}\n")
        self.mergeviewheader.setDefaultAlignment (QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.mergeviewheader.setDefaultSectionSize (200)
        self.mergeviewheader.setStretchLastSection (True)
        self.mergeview.setHeader (self.mergeviewheader)
        self.verticalLayout_12.addWidget(self.mergeview)
        self.labelmerge = QtGui.QLabel(self.tab_2)
        self.labelmerge.setStyleSheet("background-color:white;\n"
"border-bottom-color: rgb(121, 121, 121);\n"
"border-style: outset;\n"
"border-bottom-width: 1px;")
        self.labelmerge.setObjectName("labelmerge")
        self.verticalLayout_12.addWidget(self.labelmerge)
        self.verticalLayout_12.setStretch(0, 20)
        self.verticalLayout_12.setStretch(1, 90)
        self.verticalLayout_12.setStretch(2, 10)
        self.gridLayout_14.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox_13 = QtGui.QGroupBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy)
        self.groupBox_13.setMinimumSize(QtCore.QSize(0, 88))
        self.groupBox_13.setMaximumSize(QtCore.QSize(2000, 1000))
        self.groupBox_13.setStyleSheet("background-color: rgb(242, 242, 242);\n"
"border:outset")
        self.groupBox_13.setObjectName("groupBox_13")
        self.buttonstart = QtGui.QPushButton(self.groupBox_13)
        self.buttonstart.setGeometry(QtCore.QRect(184, 10, 121, 46))
        self.buttonstart.setStyleSheet("QPushButton{background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,82,181, 255),  stop:1 rgba(16,135,251, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";}\n"
"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(16,135,251, 255),  stop:1 rgba(0,82,181, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";\n"
"}\n"
"")
        self.buttonstart.setObjectName("buttonstart")
        self.buttoncancel = QtGui.QPushButton(self.groupBox_13)
        self.buttoncancel.setGeometry(QtCore.QRect(332, 10, 121, 46))
        self.buttoncancel.setStyleSheet("QPushButton{background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(77,77,77, 255),  stop:1  rgba(152,152, 152, 255));\n"
"color: rgb(255,255,255); \n"
"border-radius: 6px;\n"
"font: 16px \"微软雅黑\";}\n"

"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(152,152, 152, 255),  stop:1 rgba(77,77,77, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";\n"
"}\n"
"")
        self.buttoncancel.setObjectName("buttoncancel")
        self.buttonexamine = QtGui.QPushButton(self.groupBox_13)
        self.buttonexamine.setGeometry(QtCore.QRect(484, 10, 121, 46))
        self.buttonexamine.setStyleSheet("QPushButton{background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(77,77,77, 255),  stop:1  rgba(152,152, 152, 255));\n"
"color: rgb(255,255,255); \n"
"border-radius: 6px;\n"
"font: 16px \"微软雅黑\";}\n"

"QPushButton::hover{\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(152,152, 152, 255),  stop:1 rgba(77,77,77, 255));\n"
"color: rgb(255,255,255);\n"
"border:outset;\n"
"border-radius: 6px;\n"
"font: 16px\"微软雅黑\";\n"
"}\n"
"")
        self.buttonexamine.setObjectName("buttonexamine")
        self.horizontalLayout_8.addWidget(self.groupBox_13)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.gridLayout_14.addLayout(self.verticalLayout_9, 2, 0, 1, 1)
        self.gridLayout_14.setRowStretch(0, 225)
        self.gridLayout_14.setRowStretch(1, 130)
        self.gridLayout_14.setRowStretch(2, 88)
        self.gridLayout_15.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.tab_2)
        self.gridLayout_5.addWidget(self.stackedWidget_2, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_17 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtGui.QGridLayout()
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.groupBox_14 = QtGui.QGroupBox(self.page_2)
        self.groupBox_14.setMaximumSize(QtCore.QSize(16777215, 43))
        self.groupBox_14.setStyleSheet("background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(120, 120, 120, 255),  stop:0.954802 rgba(30, 30,30, 255));"
"border:outset;")
        self.groupBox_14.setObjectName("groupBox_14")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox_14)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.buttontransnew = QtGui.QPushButton(self.groupBox_14)
        self.buttontransnew.setMinimumSize(QtCore.QSize(67, 27))
        self.buttontransnew.setMaximumSize(QtCore.QSize(67, 27))
        self.buttontransnew.setStyleSheet("background-color: rgb(222, 222, 222);""border-radius:2px;")
        self.buttontransnew.setObjectName("buttontransnew")
        self.horizontalLayout_9.addWidget(self.buttontransnew)
        self.buttontransbegin = QtGui.QPushButton(self.groupBox_14)
        self.buttontransbegin.setMinimumSize(QtCore.QSize(67, 27))
        self.buttontransbegin.setMaximumSize(QtCore.QSize(67, 27))
        self.buttontransbegin.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 2px;")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/begin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttontransbegin.setIcon(icon16)
        self.buttontransbegin.setObjectName("buttontransbegin")
        self.horizontalLayout_9.addWidget(self.buttontransbegin)
        self.buttontranspause = QtGui.QPushButton(self.groupBox_14)
        self.buttontranspause.setMinimumSize(QtCore.QSize(67, 27))
        self.buttontranspause.setMaximumSize(QtCore.QSize(67, 27))
        self.buttontranspause.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 2px;")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/images/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttontranspause.setIcon(icon17)
        self.buttontranspause.setObjectName("buttontranspause")
        self.horizontalLayout_9.addWidget(self.buttontranspause)
        self.buttontransdelete = QtGui.QPushButton(self.groupBox_14)
        self.buttontransdelete.setMinimumSize(QtCore.QSize(67, 27))
        self.buttontransdelete.setMaximumSize(QtCore.QSize(67, 27))
        self.buttontransdelete.setStyleSheet("background-color: rgb(222, 222, 222);\n"
"border-radius: 2px;")
        self.buttontransdelete.setIcon(icon15)
        self.buttontransdelete.setObjectName("buttontransdelete")
        self.horizontalLayout_9.addWidget(self.buttontransdelete)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.gridLayout_16.addWidget(self.groupBox_14, 0, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 1, 1, 1)
        self.gridLayout_20 = QtGui.QGridLayout()
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.labelallmission = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelallmission.sizePolicy().hasHeightForWidth())
        self.labelallmission.setSizePolicy(sizePolicy)
        self.labelallmission.setMaximumSize(QtCore.QSize(159, 43))
        self.labelallmission.setStyleSheet("background-color: rgb(167, 167, 167); \n"
"font: 15pt \"SimHei\";\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255),  stop:0.954802 rgba(204, 204, 204, 255));")
        self.labelallmission.setObjectName("labelallmission")
        self.gridLayout_20.addWidget(self.labelallmission, 0, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.gridLayout_21 = QtGui.QGridLayout()
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.listWidget = QtGui.QListWidget(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(159, 16777215))
        self.listWidget.setStyleSheet("border:outset;\n"
"font: 12pt;\n"
"background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(228, 228, 228, 255),  stop:0.954802 rgba(136, 136, 136, 255));")
        self.listWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.listWidget.setObjectName("listWidget")
        QtGui.QListWidgetItem(self.listWidget)
        QtGui.QListWidgetItem(self.listWidget)
        self.gridLayout_21.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_21, 1, 0, 1, 1)
        self.gridLayout_18 = QtGui.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.transview = QtGui.QTreeView(self.page_2)
        self.transview.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.transview.setObjectName("transview")
        self.transviewheader = QtGui.QHeaderView (QtCore.Qt.Horizontal, self.transview)
        self.transviewheader.setStyleSheet("\n"
"QHeaderView::section {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(202,202,202, 255));\n"
"height: 30px;\n"
"border-bottom-width:1px;\n"
"border-right-width:1px;\n"
"border-color:rgb(102,102,102);"
"border-style:outset;}\n")
        self.transviewheader.setDefaultAlignment (QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.transviewheader.setDefaultSectionSize (170)
        self.transviewheader.setStretchLastSection (True)
        self.transview.setHeader (self.transviewheader)
        self.gridLayout_18.addWidget(self.transview, 0, 1, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_18, 1, 1, 1, 1)
        self.gridLayout_17.setColumnStretch(0, 159)
        self.gridLayout_17.setColumnStretch(1, 691)
        self.gridLayout_17.setRowStretch(0, 43)
        self.gridLayout_17.setRowStretch(1, 470)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelsideversions = QtGui.QLabel(self.centralWidget)
        self.labelsideversions.setText("")
        self.labelsideversions.setObjectName("labelsideversions")
        self.horizontalLayout.addWidget(self.labelsideversions)

        self.labelversions = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelversions.sizePolicy().hasHeightForWidth())
        self.labelversions.setSizePolicy(sizePolicy)
        self.labelversions.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(81, 81, 81);")
        self.labelversions.setObjectName("labelversions")
        self.horizontalLayout.addWidget(self.labelversions)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.labelcnmobile = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelcnmobile.sizePolicy().hasHeightForWidth())
        self.labelcnmobile.setSizePolicy(sizePolicy)
        self.labelcnmobile.setMinimumSize(QtCore.QSize(176, 20))
#        self.labelcnmobile.setMaximumSize(QtCore.QSize(23, 20))
        self.labelcnmobile.setText("")
        self.labelcnmobile.setPixmap(QtGui.QPixmap(":/images/cnmobile.png"))
        self.labelcnmobile.setScaledContents(False)
        self.labelcnmobile.setObjectName("labelcnmobile")
        self.horizontalLayout.addWidget(self.labelcnmobile)
        self.labelsidechinamobile = QtGui.QLabel(self.centralWidget)
        self.labelsidechinamobile.setText("")
        self.labelsidechinamobile.setObjectName("labelsidechinamobile")
        self.horizontalLayout.addWidget(self.labelsidechinamobile)
        self.horizontalLayout.setStretch(0, 13)
        self.horizontalLayout.setStretch(1, 114)
        self.horizontalLayout.setStretch(2, 541)
        self.horizontalLayout.setStretch(3, 25)
        self.horizontalLayout.setStretch(4, 130)
        self.horizontalLayout.setStretch(5, 28)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 30)
        self.verticalLayout.setStretch(1, 98)
        self.verticalLayout.setStretch(2, 513)
        self.verticalLayout.setStretch(3, 29)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.labelcartoonupload.setText(QtGui.QApplication.translate("MainWindow", "动画编码上传平台", None, QtGui.QApplication.UnicodeUTF8))
#        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", " 反馈 ", None, QtGui.QApplication.UnicodeUTF8))
#        self.buttonset.setText(QtGui.QApplication.translate("MainWindow", " 设置 ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelarrow.setText(QtGui.QApplication.translate("MainWindow", " >", None, QtGui.QApplication.UnicodeUTF8))
        self.labelhello.setText(QtGui.QApplication.translate("MainWindow", "您好，融创天下股份有限公司", None, QtGui.QApplication.UnicodeUTF8))
        self.labelvideoedit.setText(QtGui.QApplication.translate("MainWindow", "视频编辑：共计 203 集", None, QtGui.QApplication.UnicodeUTF8))
        self.labelvideoconvert.setText(QtGui.QApplication.translate("MainWindow", "视频转码：共计 203 集", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonsave.setText(QtGui.QApplication.translate("MainWindow", "保存", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonpreview.setText(QtGui.QApplication.translate("MainWindow", "预览", None, QtGui.QApplication.UnicodeUTF8))
        self.buttoncancelbrowse.setText(QtGui.QApplication.translate("MainWindow", "取消预览", None, QtGui.QApplication.UnicodeUTF8))
        self.labellastrecord.setText(QtGui.QApplication.translate("MainWindow", "上次截取记录：", None, QtGui.QApplication.UnicodeUTF8))
        self.labellastsave.setText(QtGui.QApplication.translate("MainWindow", "上次保存文件：", None, QtGui.QApplication.UnicodeUTF8))
        self.labellastrecordtime.setText(QtGui.QApplication.translate("MainWindow", "00:00:00 -- 00:05:31", None, QtGui.QApplication.UnicodeUTF8))
        self.labellastsavefile.setText(QtGui.QApplication.translate("MainWindow", "秦时明月", None, QtGui.QApplication.UnicodeUTF8))
#        self.checkboxleadertitle.setText(QtGui.QApplication.translate("MainWindow", "片头标题", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonvideointercept.setText(QtGui.QApplication.translate("MainWindow", "视频截取", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonvideomerge.setText(QtGui.QApplication.translate("MainWindow", "视频合并", None, QtGui.QApplication.UnicodeUTF8))
	
        self.labelfilename.setText(QtGui.QApplication.translate("MainWindow", "文件名：", None, QtGui.QApplication.UnicodeUTF8))
        self.labeloutputset.setText(QtGui.QApplication.translate("MainWindow", "输出设置", None, QtGui.QApplication.UnicodeUTF8))
        self.labelsaveto.setText(QtGui.QApplication.translate("MainWindow", "保存到：", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonbrowse.setText(QtGui.QApplication.translate("MainWindow", "浏览", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonvideointerceptpage.setText(QtGui.QApplication.translate("MainWindow", "视频截取", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonvideomergepage.setText(QtGui.QApplication.translate("MainWindow", "视频合并", None, QtGui.QApplication.UnicodeUTF8))
	
        self.labelmerge.setText(QtGui.QApplication.translate("MainWindow", "共有 0 个视频准备合并", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonstart.setText(QtGui.QApplication.translate("MainWindow", "开始", None, QtGui.QApplication.UnicodeUTF8))
        self.buttoncancel.setText(QtGui.QApplication.translate("MainWindow", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonexamine.setText(QtGui.QApplication.translate("MainWindow", "查看", None, QtGui.QApplication.UnicodeUTF8))
        self.buttontransnew.setText(QtGui.QApplication.translate("MainWindow", "新建任务", None, QtGui.QApplication.UnicodeUTF8))
        self.buttontransbegin.setText(QtGui.QApplication.translate("MainWindow", "开始", None, QtGui.QApplication.UnicodeUTF8))
        self.buttontranspause.setText(QtGui.QApplication.translate("MainWindow", "暂停", None, QtGui.QApplication.UnicodeUTF8))
        self.buttontransdelete.setText(QtGui.QApplication.translate("MainWindow", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.labelallmission.setText(QtGui.QApplication.translate("MainWindow", "   全部任务", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", "      进行中", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.item(1).setText(QtGui.QApplication.translate("MainWindow", "      已完成", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.labelversions.setText(QtGui.QApplication.translate("MainWindow", " 当前版本 V1.0 Beta", None, QtGui.QApplication.UnicodeUTF8))
        #self.labelsidechinamobile.setText(QtGui.QApplication.translate("MainWindow", "中国移动手机动漫基地", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
