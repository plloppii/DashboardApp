import time
import serial
import serial.tools.list_ports
from Client.g_serial import *
from Client.g_client import *
from Client.g_data import *

from touchdisplay import *
from watchdogthread import *
from personality import Personality

import sys
import threading
import os

if __name__ == "__main__":

    data_thread = g_data()
    client_conn = g_client(data_thread)
    serial_conn = g_serial(data_thread)
    data_thread.start()

    personality = Personality(False, "/Volumes", "/Users/jct/localgcode")

    app = QtWidgets.QApplication(sys.argv)

    properties = {}
    for line in open("config.properties"):
        properties[line.split("=")[0]] = line.split("=")[1].strip()

    app.setApplicationName(properties["name"])
    app.setApplicationVersion(properties["version"])

    display = TouchDisplay(client_conn, serial_conn, personality)
    display.show()
    jt_thread = WatchdogThread(display.print_pop, personality.watchpoint)
    jt_thread.start()
    app.exec_()
