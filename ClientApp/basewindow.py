import logging
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets


#BaseWindow that is inherited from all windows. 
#Overrides basic functions like close and show
#Implements Fullscreen flags, cleaning up code in the individual windows

class BaseWindow(QtWidgets.QWidget):
	def __init__(self, parent = None):
		super(BaseWindow,self).__init__()

		# Set up logging
		self._logger = logging.getLogger(__name__)

		self.properties = {}
		config_path = Path(__file__).parent.absolute().__str__() + "/config.properties"
		for line in open(config_path):
			self.properties[line.split("=")[0]] = line.split("=")[1].strip()

		self.fullscreen = False
		self.parent = parent
		self.notification = None
		self.setWindowFlags(self.windowFlags())
		if (parent != None) and (self.parent.fullscreen):
			self.fullscreen = True
			self.setWindowState(self.windowState() | QtCore.Qt.WindowFullScreen)

	def _log(self, message):
		self._logger.debug(message)

	def back(self):
		self._log("User touched Back")
		self.parent.show()
		self.close()

	def show(self):
		self.move(QtWidgets.qApp.desktop().availableGeometry().center() - self.rect().center())
		super(BaseWindow,self).show()

		#Display notification if there is a notification object present AND
		#If the window is the main window or if the notificaiton is not visible. 
		if(self.notification != None):
			self.notification.parent = self
			self.notification.show()
			# self.notification.activateWindow()
			# print(self.notification.visibleRegion().isEmpty())

			
