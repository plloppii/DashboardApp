# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infowindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        InfoWindow.setObjectName("InfoWindow")
        InfoWindow.resize(800, 480)
        InfoWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.Back = QtWidgets.QPushButton(InfoWindow)
        self.Back.setGeometry(QtCore.QRect(10, 380, 91, 91))
        self.Back.setMaximumSize(QtCore.QSize(100, 100))
        self.Back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon)
        self.Back.setIconSize(QtCore.QSize(100, 100))
        self.Back.setObjectName("Back")
        self.layoutWidget = QtWidgets.QWidget(InfoWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 112, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.w_pushbutton_info = QtWidgets.QPushButton(self.layoutWidget)
        self.w_pushbutton_info.setMaximumSize(QtCore.QSize(100, 100))
        self.w_pushbutton_info.setObjectName("w_pushbutton_info")
        self.verticalLayout.addWidget(self.w_pushbutton_info)
        self.w_pushbutton_capabilities = QtWidgets.QPushButton(self.layoutWidget)
        self.w_pushbutton_capabilities.setMaximumSize(QtCore.QSize(100, 100))
        self.w_pushbutton_capabilities.setObjectName("w_pushbutton_capabilities")
        self.verticalLayout.addWidget(self.w_pushbutton_capabilities)
        self.w_pushbutton_stats = QtWidgets.QPushButton(self.layoutWidget)
        self.w_pushbutton_stats.setMaximumSize(QtCore.QSize(100, 100))
        self.w_pushbutton_stats.setObjectName("w_pushbutton_stats")
        self.verticalLayout.addWidget(self.w_pushbutton_stats)
        self.w_pushbutton_settings = QtWidgets.QPushButton(self.layoutWidget)
        self.w_pushbutton_settings.setMaximumSize(QtCore.QSize(100, 100))
        self.w_pushbutton_settings.setObjectName("w_pushbutton_settings")
        self.verticalLayout.addWidget(self.w_pushbutton_settings)
        self.w_message_text = QtWidgets.QTextEdit(InfoWindow)
        self.w_message_text.setGeometry(QtCore.QRect(139, 30, 601, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_message_text.sizePolicy().hasHeightForWidth())
        self.w_message_text.setSizePolicy(sizePolicy)
        self.w_message_text.setMaximumSize(QtCore.QSize(115200, 1000))
        self.w_message_text.setObjectName("w_message_text")

        self.retranslateUi(InfoWindow)
        QtCore.QMetaObject.connectSlotsByName(InfoWindow)

    def retranslateUi(self, InfoWindow):
        _translate = QtCore.QCoreApplication.translate
        InfoWindow.setWindowTitle(_translate("InfoWindow", "ControlWindow"))
        self.w_pushbutton_info.setText(_translate("InfoWindow", "Printer Info"))
        self.w_pushbutton_capabilities.setText(_translate("InfoWindow", "Printer\n"
"Capabilities"))
        self.w_pushbutton_stats.setText(_translate("InfoWindow", "Printer Stats"))
        self.w_pushbutton_settings.setText(_translate("InfoWindow", "Printer\n"
"Settings"))
