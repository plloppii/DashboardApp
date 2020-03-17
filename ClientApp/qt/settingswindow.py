# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingswindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.setEnabled(True)
        SettingsWindow.resize(800, 480)
        SettingsWindow.setMinimumSize(QtCore.QSize(800, 480))
        SettingsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Server = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Server.sizePolicy().hasHeightForWidth())
        self.Server.setSizePolicy(sizePolicy)
        self.Server.setMinimumSize(QtCore.QSize(150, 150))
        self.Server.setMaximumSize(QtCore.QSize(150, 150))
        self.Server.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Server.setIcon(icon)
        self.Server.setIconSize(QtCore.QSize(150, 150))
        self.Server.setObjectName("Server")
        self.horizontalLayout_2.addWidget(self.Server)
        self.Serial = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Serial.sizePolicy().hasHeightForWidth())
        self.Serial.setSizePolicy(sizePolicy)
        self.Serial.setMinimumSize(QtCore.QSize(150, 150))
        self.Serial.setMaximumSize(QtCore.QSize(150, 150))
        self.Serial.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/serial.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Serial.setIcon(icon1)
        self.Serial.setIconSize(QtCore.QSize(150, 150))
        self.Serial.setObjectName("Serial")
        self.horizontalLayout_2.addWidget(self.Serial)
        self.UserUpdate = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.UserUpdate.sizePolicy().hasHeightForWidth())
        self.UserUpdate.setSizePolicy(sizePolicy)
        self.UserUpdate.setMinimumSize(QtCore.QSize(150, 150))
        self.UserUpdate.setMaximumSize(QtCore.QSize(150, 150))
        self.UserUpdate.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/userupdate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UserUpdate.setIcon(icon2)
        self.UserUpdate.setIconSize(QtCore.QSize(150, 150))
        self.UserUpdate.setObjectName("UserUpdate")
        self.horizontalLayout_2.addWidget(self.UserUpdate)
        self.Wifi = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Wifi.sizePolicy().hasHeightForWidth())
        self.Wifi.setSizePolicy(sizePolicy)
        self.Wifi.setMinimumSize(QtCore.QSize(150, 150))
        self.Wifi.setMaximumSize(QtCore.QSize(150, 150))
        self.Wifi.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/wifi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Wifi.setIcon(icon3)
        self.Wifi.setIconSize(QtCore.QSize(150, 150))
        self.Wifi.setObjectName("Wifi")
        self.horizontalLayout_2.addWidget(self.Wifi)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.w_pushbutton_debug = QtWidgets.QPushButton(SettingsWindow)
        self.w_pushbutton_debug.setMinimumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_debug.setMaximumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_debug.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/bug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.w_pushbutton_debug.setIcon(icon4)
        self.w_pushbutton_debug.setIconSize(QtCore.QSize(100, 100))
        self.w_pushbutton_debug.setObjectName("w_pushbutton_debug")
        self.horizontalLayout_3.addWidget(self.w_pushbutton_debug)
        self.w_pushbutton_info = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_pushbutton_info.sizePolicy().hasHeightForWidth())
        self.w_pushbutton_info.setSizePolicy(sizePolicy)
        self.w_pushbutton_info.setMinimumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_info.setMaximumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_info.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.w_pushbutton_info.setIcon(icon5)
        self.w_pushbutton_info.setIconSize(QtCore.QSize(100, 100))
        self.w_pushbutton_info.setObjectName("w_pushbutton_info")
        self.horizontalLayout_3.addWidget(self.w_pushbutton_info)
        self.w_pushbutton_duex = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_pushbutton_duex.sizePolicy().hasHeightForWidth())
        self.w_pushbutton_duex.setSizePolicy(sizePolicy)
        self.w_pushbutton_duex.setMinimumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_duex.setMaximumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_duex.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/duex.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.w_pushbutton_duex.setIcon(icon6)
        self.w_pushbutton_duex.setIconSize(QtCore.QSize(100, 100))
        self.w_pushbutton_duex.setObjectName("w_pushbutton_duex")
        self.horizontalLayout_3.addWidget(self.w_pushbutton_duex)
        self.w_pushbutton_term = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_pushbutton_term.sizePolicy().hasHeightForWidth())
        self.w_pushbutton_term.setSizePolicy(sizePolicy)
        self.w_pushbutton_term.setMinimumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_term.setMaximumSize(QtCore.QSize(150, 150))
        self.w_pushbutton_term.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/term.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.w_pushbutton_term.setIcon(icon7)
        self.w_pushbutton_term.setIconSize(QtCore.QSize(100, 100))
        self.w_pushbutton_term.setObjectName("w_pushbutton_term")
        self.horizontalLayout_3.addWidget(self.w_pushbutton_term)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back = QtWidgets.QPushButton(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Back.sizePolicy().hasHeightForWidth())
        self.Back.setSizePolicy(sizePolicy)
        self.Back.setMinimumSize(QtCore.QSize(100, 100))
        self.Back.setMaximumSize(QtCore.QSize(100, 100))
        self.Back.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon8)
        self.Back.setIconSize(QtCore.QSize(100, 100))
        self.Back.setObjectName("Back")
        self.horizontalLayout.addWidget(self.Back)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SoftwareVersion = QtWidgets.QLabel(SettingsWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SoftwareVersion.sizePolicy().hasHeightForWidth())
        self.SoftwareVersion.setSizePolicy(sizePolicy)
        self.SoftwareVersion.setMinimumSize(QtCore.QSize(0, 65))
        self.SoftwareVersion.setMaximumSize(QtCore.QSize(250, 70))
        self.SoftwareVersion.setObjectName("SoftwareVersion")
        self.horizontalLayout.addWidget(self.SoftwareVersion)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "TouchDisplay"))
        self.SoftwareVersion.setText(_translate("SettingsWindow", "V.1.0.0 re3Display"))
