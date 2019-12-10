from builtins import str
from qt.serialwindow import *
from PyQt5.QtCore import Qt


class SerialWindow(QtWidgets.QWidget, Ui_SerialWindow):
    def __init__(self, serial, event_handler, parent=None):
        super(SerialWindow, self).__init__()
        self.setupUi(self)
        # self.serial = serial
        self.event_handler = event_handler
        self.event_handler.reconnect_serial.connect(self.reconnect_serial)
        # self.serial.data.checkserial_msg.connect(self.checkserial_msg)

        # Make the selection Behavior as selecting the entire row
        self.COMlist.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.COMlist.setSelectionMode(QtWidgets.QTableView.SingleSelection)
        # Hide the vertical header which contains the Index of the row.
        self.COMlist.verticalHeader().hide()
        # Stretch out the horizontal header to take up the entire view
        header = self.COMlist.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.scan_serial()
        self.connect_serial()

        self.Back.clicked.connect(self.close)
        self.ScanSerial.clicked.connect(self.scan_serial)
        self.ConnectSerial.clicked.connect(self.connect_serial)
        self.DisconnectSerial.clicked.connect(self.disconnect_serial)

    def reconnect_serial(self):
        if self.scan_serial():
            self.connect_serial()

    def checkserial_msg(self):
        # self.output_serial(self.serial.data.serial_msg)
        self.scan_serial()

    def output_serial(self, text):
        self.SerialOutput.moveCursor(QtGui.QTextCursor.End)
        self.SerialOutput.ensureCursorVisible()
        self.SerialOutput.append(text)

    def connect_serial(self):
        selected = self.COMlist.currentRow()
        selected_device = self.COMlist.item(selected, 0)
        if selected_device != None:
            # self.serial.com = selected_device.text()
            # response = str(self.serial.attemptconnect())
            self.output_serial(response)
        else:
            self.output_serial("Please select a device")

    def disconnect_serial(self):
        # self.output_serial(self.serial.disconnect())
        pass

    def scan_serial(self):
        # comlist = self.serial.scan()
        comlist = []
        self.COMlist.setRowCount(0)
        for p in comlist:
            rowpos = self.COMlist.rowCount()

            self.COMlist.insertRow(rowpos)
            device = QtWidgets.QTableWidgetItem(p.device)
            device.setFlags(Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            descrip = QtWidgets.QTableWidgetItem(p.description)
            descrip.setFlags(Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            self.COMlist.setItem(rowpos, 0, device)
            self.COMlist.setItem(rowpos, 1, descrip)

            if '/dev/ttyUSB' in p.device:
                self.COMlist.selectRow(rowpos)
                return True
