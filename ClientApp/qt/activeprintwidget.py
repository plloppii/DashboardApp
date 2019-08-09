# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/activeprintwidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ActivePrintWidget(object):
    def setupUi(self, ActivePrintWidget):
        ActivePrintWidget.setObjectName("ActivePrintWidget")
        ActivePrintWidget.resize(800, 188)
        ActivePrintWidget.setMaximumSize(QtCore.QSize(800, 480))
        self.layoutWidget = QtWidgets.QWidget(ActivePrintWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 791, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.ActivePrint = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.ActivePrint.setObjectName("ActivePrint")
        self.Back = QtWidgets.QPushButton(self.layoutWidget)
        self.Back.setMaximumSize(QtCore.QSize(100, 100))
        self.Back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon)
        self.Back.setIconSize(QtCore.QSize(100, 100))
        self.Back.setObjectName("Back")
        self.ActivePrint.addWidget(self.Back)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FileLabel = QtWidgets.QLabel(self.layoutWidget)
        self.FileLabel.setObjectName("FileLabel")
        self.horizontalLayout.addWidget(self.FileLabel)
        self.FileName = QtWidgets.QLabel(self.layoutWidget)
        self.FileName.setObjectName("FileName")
        self.horizontalLayout.addWidget(self.FileName)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.progress = QtWidgets.QProgressBar(self.layoutWidget)
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.verticalLayout_5.addWidget(self.progress)
        self.ActivePrint.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.FeedLabel = QtWidgets.QPushButton(self.layoutWidget)
        self.FeedLabel.setObjectName("FeedLabel")
        self.verticalLayout.addWidget(self.FeedLabel)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.Feedneg = QtWidgets.QPushButton(self.layoutWidget)
        self.Feedneg.setMaximumSize(QtCore.QSize(75, 75))
        self.Feedneg.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/downarrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Feedneg.setIcon(icon1)
        self.Feedneg.setIconSize(QtCore.QSize(50, 50))
        self.Feedneg.setObjectName("Feedneg")
        self.horizontalLayout_11.addWidget(self.Feedneg)
        self.Feed = QtWidgets.QLabel(self.layoutWidget)
        self.Feed.setObjectName("Feed")
        self.horizontalLayout_11.addWidget(self.Feed)
        self.Feedpos = QtWidgets.QPushButton(self.layoutWidget)
        self.Feedpos.setMaximumSize(QtCore.QSize(75, 75))
        self.Feedpos.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/uparrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Feedpos.setIcon(icon2)
        self.Feedpos.setIconSize(QtCore.QSize(50, 50))
        self.Feedpos.setObjectName("Feedpos")
        self.horizontalLayout_11.addWidget(self.Feedpos)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Fan = QtWidgets.QPushButton(self.layoutWidget)
        self.Fan.setMaximumSize(QtCore.QSize(75, 75))
        self.Fan.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/fanoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Fan.setIcon(icon3)
        self.Fan.setIconSize(QtCore.QSize(65, 65))
        self.Fan.setObjectName("Fan")
        self.horizontalLayout_2.addWidget(self.Fan)
        self.StopPrint = QtWidgets.QPushButton(self.layoutWidget)
        self.StopPrint.setMaximumSize(QtCore.QSize(75, 75))
        self.StopPrint.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/cooldown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopPrint.setIcon(icon4)
        self.StopPrint.setIconSize(QtCore.QSize(65, 65))
        self.StopPrint.setObjectName("StopPrint")
        self.horizontalLayout_2.addWidget(self.StopPrint)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.ActivePrint.addLayout(self.verticalLayout)

        self.retranslateUi(ActivePrintWidget)
        QtCore.QMetaObject.connectSlotsByName(ActivePrintWidget)

    def retranslateUi(self, ActivePrintWidget):
        _translate = QtCore.QCoreApplication.translate
        ActivePrintWidget.setWindowTitle(_translate("ActivePrintWidget", "TemperatureWindow"))
        self.FileLabel.setText(_translate("ActivePrintWidget", "Curent File:"))
        self.FileName.setText(_translate("ActivePrintWidget", "-----"))
        self.FeedLabel.setText(_translate("ActivePrintWidget", "Feedrate"))
        self.Feed.setText(_translate("ActivePrintWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">-----</span></p></body></html>"))

