# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'duexsetupwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_duexSetupWindow(object):
    def setupUi(self, duexSetupWindow):
        duexSetupWindow.setObjectName("duexSetupWindow")
        duexSetupWindow.resize(800, 480)
        duexSetupWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.Back = QtWidgets.QPushButton(duexSetupWindow)
        self.Back.setGeometry(QtCore.QRect(10, 380, 91, 91))
        self.Back.setMaximumSize(QtCore.QSize(100, 100))
        self.Back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back.setIcon(icon)
        self.Back.setIconSize(QtCore.QSize(100, 100))
        self.Back.setObjectName("Back")
        self.verticalLayoutWidget = QtWidgets.QWidget(duexSetupWindow)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 60, 301, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.w_lineedit_x1 = JTLineEdit(self.verticalLayoutWidget)
        self.w_lineedit_x1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.w_lineedit_x1.setFont(font)
        self.w_lineedit_x1.setObjectName("w_lineedit_x1")
        self.horizontalLayout.addWidget(self.w_lineedit_x1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.w_lineedit_y1 = JTLineEdit(self.verticalLayoutWidget)
        self.w_lineedit_y1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.w_lineedit_y1.setFont(font)
        self.w_lineedit_y1.setObjectName("w_lineedit_y1")
        self.horizontalLayout_2.addWidget(self.w_lineedit_y1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.w_pushbutton_temporary = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.w_pushbutton_temporary.setEnabled(False)
        self.w_pushbutton_temporary.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.w_pushbutton_temporary.setFont(font)
        self.w_pushbutton_temporary.setObjectName("w_pushbutton_temporary")
        self.verticalLayout.addWidget(self.w_pushbutton_temporary)
        self.w_pushbutton_permanent = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.w_pushbutton_permanent.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.w_pushbutton_permanent.setFont(font)
        self.w_pushbutton_permanent.setObjectName("w_pushbutton_permanent")
        self.verticalLayout.addWidget(self.w_pushbutton_permanent)
        self.w_pushbutton_revert = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.w_pushbutton_revert.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.w_pushbutton_revert.setFont(font)
        self.w_pushbutton_revert.setObjectName("w_pushbutton_revert")
        self.verticalLayout.addWidget(self.w_pushbutton_revert)
        self.horizontalLayoutWidget = QtWidgets.QWidget(duexSetupWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(450, 60, 272, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.w_pushbutton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_7.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_7.setFont(font)
        self.w_pushbutton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_7.setObjectName("w_pushbutton_7")
        self.verticalLayout_3.addWidget(self.w_pushbutton_7)
        self.w_pushbutton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_4.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_4.setFont(font)
        self.w_pushbutton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_4.setObjectName("w_pushbutton_4")
        self.verticalLayout_3.addWidget(self.w_pushbutton_4)
        self.w_pushbutton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_1.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_1.setFont(font)
        self.w_pushbutton_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_1.setObjectName("w_pushbutton_1")
        self.verticalLayout_3.addWidget(self.w_pushbutton_1)
        self.w_pushbutton_negative = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_negative.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.w_pushbutton_negative.setFont(font)
        self.w_pushbutton_negative.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_negative.setObjectName("w_pushbutton_negative")
        self.verticalLayout_3.addWidget(self.w_pushbutton_negative)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.w_pushbutton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_8.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_8.setFont(font)
        self.w_pushbutton_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_8.setObjectName("w_pushbutton_8")
        self.verticalLayout_5.addWidget(self.w_pushbutton_8)
        self.w_pushbutton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_5.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_5.setFont(font)
        self.w_pushbutton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_5.setObjectName("w_pushbutton_5")
        self.verticalLayout_5.addWidget(self.w_pushbutton_5)
        self.w_pushbutton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_2.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_2.setFont(font)
        self.w_pushbutton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_2.setObjectName("w_pushbutton_2")
        self.verticalLayout_5.addWidget(self.w_pushbutton_2)
        self.w_pushbutton_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_0.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_0.setFont(font)
        self.w_pushbutton_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_0.setObjectName("w_pushbutton_0")
        self.verticalLayout_5.addWidget(self.w_pushbutton_0)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.w_pushbutton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_9.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_9.setFont(font)
        self.w_pushbutton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_9.setObjectName("w_pushbutton_9")
        self.verticalLayout_4.addWidget(self.w_pushbutton_9)
        self.w_pushbutton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_6.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_6.setFont(font)
        self.w_pushbutton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_6.setObjectName("w_pushbutton_6")
        self.verticalLayout_4.addWidget(self.w_pushbutton_6)
        self.w_pushbutton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_3.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_3.setFont(font)
        self.w_pushbutton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_3.setObjectName("w_pushbutton_3")
        self.verticalLayout_4.addWidget(self.w_pushbutton_3)
        self.w_pushbutton_decimal = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_decimal.setMinimumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.w_pushbutton_decimal.setFont(font)
        self.w_pushbutton_decimal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_decimal.setObjectName("w_pushbutton_decimal")
        self.verticalLayout_4.addWidget(self.w_pushbutton_decimal)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.w_pushbutton_delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_delete.setMinimumSize(QtCore.QSize(60, 120))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.w_pushbutton_delete.setFont(font)
        self.w_pushbutton_delete.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_delete.setObjectName("w_pushbutton_delete")
        self.verticalLayout_2.addWidget(self.w_pushbutton_delete)
        self.w_pushbutton_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.w_pushbutton_clear.setMinimumSize(QtCore.QSize(60, 120))
        self.w_pushbutton_clear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w_pushbutton_clear.setObjectName("w_pushbutton_clear")
        self.verticalLayout_2.addWidget(self.w_pushbutton_clear)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(duexSetupWindow)
        QtCore.QMetaObject.connectSlotsByName(duexSetupWindow)

    def retranslateUi(self, duexSetupWindow):
        _translate = QtCore.QCoreApplication.translate
        duexSetupWindow.setWindowTitle(_translate("duexSetupWindow", "ControlWindow"))
        self.label_3.setText(_translate("duexSetupWindow", "Dual Extruder Offsets"))
        self.label.setText(_translate("duexSetupWindow", "T1 X Offset"))
        self.label_2.setText(_translate("duexSetupWindow", "T1 Y Offset"))
        self.w_pushbutton_temporary.setText(_translate("duexSetupWindow", "Use these settings temporarily"))
        self.w_pushbutton_permanent.setText(_translate("duexSetupWindow", "Save these settings permanently"))
        self.w_pushbutton_revert.setText(_translate("duexSetupWindow", "Revert to last saved settings"))
        self.w_pushbutton_7.setText(_translate("duexSetupWindow", "7"))
        self.w_pushbutton_4.setText(_translate("duexSetupWindow", "4"))
        self.w_pushbutton_1.setText(_translate("duexSetupWindow", "1"))
        self.w_pushbutton_negative.setText(_translate("duexSetupWindow", "+/-"))
        self.w_pushbutton_8.setText(_translate("duexSetupWindow", "8"))
        self.w_pushbutton_5.setText(_translate("duexSetupWindow", "5"))
        self.w_pushbutton_2.setText(_translate("duexSetupWindow", "2"))
        self.w_pushbutton_0.setText(_translate("duexSetupWindow", "0"))
        self.w_pushbutton_9.setText(_translate("duexSetupWindow", "9"))
        self.w_pushbutton_6.setText(_translate("duexSetupWindow", "6"))
        self.w_pushbutton_3.setText(_translate("duexSetupWindow", "3"))
        self.w_pushbutton_decimal.setText(_translate("duexSetupWindow", "."))
        self.w_pushbutton_delete.setText(_translate("duexSetupWindow", "⌫"))
        self.w_pushbutton_clear.setText(_translate("duexSetupWindow", "Clear"))
from jtlineedit import JTLineEdit
