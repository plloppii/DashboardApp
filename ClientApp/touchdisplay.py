from qt.touchdisplaywindow import *
from PyQt5.QtCore import Qt
from control import *
import sys

class TouchDisplay(QtWidgets.QWidget, Ui_TouchDisplay):
    def __init__(self, parent = None):
        super(TouchDisplay, self).__init__()
        self.setupUi(self)
        self.showFullScreen()
        self.Control.setCheckable(False)
        #self.Control.setStyleSheet("QPushButton{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:checked{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:pressed {background: rgba(255,255,255,0); outline: none; border: none;}")
        self.setbuttonstyle(self.Print)
        self.setbuttonstyle(self.Settings)
        self.setbuttonstyle(self.Control)
        #self.Print.setStyleSheet("QPushButton{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:checked{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:pressed {background: rgba(255,255,255,0); outline: none; border: none;}")
        #self.Settings.setStyleSheet("QPushButton{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:checked{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:pressed {background: rgba(255,255,255,0); outline: none; border: none;}")
        self.Control.clicked.connect(self.controlpop)
    def controlpop(self):
        self.con_pop = ControlWindow(self)
        self.con_pop.show()
    def setbuttonstyle(self,obj):
        obj.setStyleSheet("QPushButton{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:checked{background: rgba(255,255,255,0); outline: none; border: none;} QPushButton:pressed {background: rgba(255,255,255,0); outline: none; border: none;}")

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	display = TouchDisplay()
	display.show()
	app.exec_()
