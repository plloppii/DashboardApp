# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/activeprintwidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from builtins import object
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ActivePrintWidget(object):
    def setupUi(self, ActivePrintWidget):
        ActivePrintWidget.setObjectName("ActivePrintWidget")
        ActivePrintWidget.resize(800, 219)
        ActivePrintWidget.setMaximumSize(QtCore.QSize(800, 600))
        self.gridLayout = QtWidgets.QGridLayout(ActivePrintWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FileLabel = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FileLabel.sizePolicy().hasHeightForWidth())
        self.FileLabel.setSizePolicy(sizePolicy)
        self.FileLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.FileLabel.setObjectName("FileLabel")
        self.horizontalLayout.addWidget(self.FileLabel)
        self.FileName = QtWidgets.QLabel(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FileName.sizePolicy().hasHeightForWidth())
        self.FileName.setSizePolicy(sizePolicy)
        self.FileName.setMinimumSize(QtCore.QSize(0, 30))
        self.FileName.setObjectName("FileName")
        self.horizontalLayout.addWidget(self.FileName)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FeedrateSlider = QtWidgets.QSlider(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FeedrateSlider.sizePolicy().hasHeightForWidth())
        self.FeedrateSlider.setSizePolicy(sizePolicy)
        self.FeedrateSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.FeedrateSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FeedrateSlider.setMaximum(200)
        self.FeedrateSlider.setPageStep(1)
        self.FeedrateSlider.setSliderPosition(100)
        self.FeedrateSlider.setOrientation(QtCore.Qt.Horizontal)
        self.FeedrateSlider.setInvertedAppearance(False)
        self.FeedrateSlider.setInvertedControls(False)
        self.FeedrateSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.FeedrateSlider.setObjectName("FeedrateSlider")
        self.verticalLayout.addWidget(self.FeedrateSlider)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.FlowrateLabel = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FlowrateLabel.sizePolicy().hasHeightForWidth())
        self.FlowrateLabel.setSizePolicy(sizePolicy)
        self.FlowrateLabel.setMaximumSize(QtCore.QSize(200, 45))
        self.FlowrateLabel.setObjectName("FlowrateLabel")
        self.horizontalLayout_4.addWidget(self.FlowrateLabel)
        self.BabysteppingLabel = QtWidgets.QPushButton(ActivePrintWidget)
        self.BabysteppingLabel.setMaximumSize(QtCore.QSize(200, 25))
        self.BabysteppingLabel.setObjectName("BabysteppingLabel")
        self.horizontalLayout_4.addWidget(self.BabysteppingLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FlowrateNeg = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FlowrateNeg.sizePolicy().hasHeightForWidth())
        self.FlowrateNeg.setSizePolicy(sizePolicy)
        self.FlowrateNeg.setMaximumSize(QtCore.QSize(65, 65))
        self.FlowrateNeg.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/downarrow.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FlowrateNeg.setIcon(icon)
        self.FlowrateNeg.setIconSize(QtCore.QSize(50, 50))
        self.FlowrateNeg.setObjectName("FlowrateNeg")
        self.horizontalLayout_3.addWidget(self.FlowrateNeg)
        self.FlowrateVal = QtWidgets.QLabel(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FlowrateVal.sizePolicy().hasHeightForWidth())
        self.FlowrateVal.setSizePolicy(sizePolicy)
        self.FlowrateVal.setObjectName("FlowrateVal")
        self.horizontalLayout_3.addWidget(self.FlowrateVal)
        self.FlowratePos = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FlowratePos.sizePolicy().hasHeightForWidth())
        self.FlowratePos.setSizePolicy(sizePolicy)
        self.FlowratePos.setMaximumSize(QtCore.QSize(65, 65))
        self.FlowratePos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/uparrow.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FlowratePos.setIcon(icon1)
        self.FlowratePos.setIconSize(QtCore.QSize(50, 50))
        self.FlowratePos.setObjectName("FlowratePos")
        self.horizontalLayout_3.addWidget(self.FlowratePos)
        self.BabysteppingNeg = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BabysteppingNeg.sizePolicy().hasHeightForWidth())
        self.BabysteppingNeg.setSizePolicy(sizePolicy)
        self.BabysteppingNeg.setMaximumSize(QtCore.QSize(65, 65))
        self.BabysteppingNeg.setText("")
        self.BabysteppingNeg.setIcon(icon)
        self.BabysteppingNeg.setIconSize(QtCore.QSize(50, 50))
        self.BabysteppingNeg.setObjectName("BabysteppingNeg")
        self.horizontalLayout_3.addWidget(self.BabysteppingNeg)
        self.BabysteppingVal = QtWidgets.QLabel(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BabysteppingVal.sizePolicy().hasHeightForWidth())
        self.BabysteppingVal.setSizePolicy(sizePolicy)
        self.BabysteppingVal.setObjectName("BabysteppingVal")
        self.horizontalLayout_3.addWidget(self.BabysteppingVal)
        self.BabysteppingPos = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BabysteppingPos.sizePolicy().hasHeightForWidth())
        self.BabysteppingPos.setSizePolicy(sizePolicy)
        self.BabysteppingPos.setMaximumSize(QtCore.QSize(65, 65))
        self.BabysteppingPos.setText("")
        self.BabysteppingPos.setIcon(icon1)
        self.BabysteppingPos.setIconSize(QtCore.QSize(50, 50))
        self.BabysteppingPos.setObjectName("BabysteppingPos")
        self.horizontalLayout_3.addWidget(self.BabysteppingPos)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.FeedrateLabel = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FeedrateLabel.sizePolicy().hasHeightForWidth())
        self.FeedrateLabel.setSizePolicy(sizePolicy)
        self.FeedrateLabel.setMinimumSize(QtCore.QSize(120, 0))
        self.FeedrateLabel.setObjectName("FeedrateLabel")
        self.horizontalLayout_5.addWidget(self.FeedrateLabel)
        self.FeedrateVal = QtWidgets.QLabel(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FeedrateVal.sizePolicy().hasHeightForWidth())
        self.FeedrateVal.setSizePolicy(sizePolicy)
        self.FeedrateVal.setMinimumSize(QtCore.QSize(0, 30))
        self.FeedrateVal.setMaximumSize(QtCore.QSize(200, 16777215))
        self.FeedrateVal.setObjectName("FeedrateVal")
        self.horizontalLayout_5.addWidget(self.FeedrateVal)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Back = QtWidgets.QPushButton(ActivePrintWidget)
        self.Back.setMaximumSize(QtCore.QSize(100, 100))
        self.Back.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/back.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon2)
        self.Back.setIconSize(QtCore.QSize(100, 100))
        self.Back.setObjectName("Back")
        self.horizontalLayout_2.addWidget(self.Back)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.PausePrint = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.PausePrint.sizePolicy().hasHeightForWidth())
        self.PausePrint.setSizePolicy(sizePolicy)
        self.PausePrint.setMaximumSize(QtCore.QSize(65, 65))
        self.PausePrint.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/pause.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PausePrint.setIcon(icon3)
        self.PausePrint.setIconSize(QtCore.QSize(55, 55))
        self.PausePrint.setObjectName("PausePrint")
        self.horizontalLayout_2.addWidget(self.PausePrint)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ResumePrint = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ResumePrint.sizePolicy().hasHeightForWidth())
        self.ResumePrint.setSizePolicy(sizePolicy)
        self.ResumePrint.setMaximumSize(QtCore.QSize(65, 65))
        self.ResumePrint.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/resume.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ResumePrint.setIcon(icon4)
        self.ResumePrint.setIconSize(QtCore.QSize(55, 55))
        self.ResumePrint.setObjectName("ResumePrint")
        self.horizontalLayout_2.addWidget(self.ResumePrint)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.Fan = QtWidgets.QPushButton(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fan.sizePolicy().hasHeightForWidth())
        self.Fan.setSizePolicy(sizePolicy)
        self.Fan.setMaximumSize(QtCore.QSize(65, 65))
        self.Fan.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/fanoff.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Fan.setIcon(icon5)
        self.Fan.setIconSize(QtCore.QSize(55, 55))
        self.Fan.setObjectName("Fan")
        self.horizontalLayout_2.addWidget(self.Fan)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.FileProgress = QtWidgets.QProgressBar(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FileProgress.sizePolicy().hasHeightForWidth())
        self.FileProgress.setSizePolicy(sizePolicy)
        self.FileProgress.setMinimumSize(QtCore.QSize(280, 0))
        self.FileProgress.setProperty("value", 0)
        self.FileProgress.setObjectName("FileProgress")
        self.verticalLayout_2.addWidget(self.FileProgress)
        self.PositionLabel = QtWidgets.QLabel(ActivePrintWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.PositionLabel.sizePolicy().hasHeightForWidth())
        self.PositionLabel.setSizePolicy(sizePolicy)
        self.PositionLabel.setObjectName("PositionLabel")
        self.verticalLayout_2.addWidget(self.PositionLabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(ActivePrintWidget)
        QtCore.QMetaObject.connectSlotsByName(ActivePrintWidget)

    def retranslateUi(self, ActivePrintWidget):
        _translate = QtCore.QCoreApplication.translate
        ActivePrintWidget.setWindowTitle(_translate(
            "ActivePrintWidget", "TemperatureWindow"))
        self.FileLabel.setText(_translate(
            "ActivePrintWidget", "Current File:"))
        self.FileName.setText(_translate(
            "ActivePrintWidget", "<html><head/><body><p><span style=\" font-size:14pt;\">-----</span></p></body></html>"))
        self.FlowrateLabel.setText(_translate(
            "ActivePrintWidget", "Flowrate: All"))
        self.BabysteppingLabel.setText(
            _translate("ActivePrintWidget", "Babystepping"))
        self.FlowrateVal.setText(_translate(
            "ActivePrintWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">-----</span></p></body></html>"))
        self.BabysteppingVal.setText(_translate(
            "ActivePrintWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">-----</span></p></body></html>"))
        self.FeedrateLabel.setText(_translate(
            "ActivePrintWidget", "Feedrate:"))
        self.FeedrateVal.setText(_translate(
            "ActivePrintWidget", "<html><head/><body><p><span style=\" font-size:14pt;\">-----</span></p></body></html>"))
        self.PositionLabel.setText(_translate(
            "ActivePrintWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">-----</span></p></body></html>"))
