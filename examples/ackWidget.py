#!/usr/bin/env python

from sys import argv,exit
from PyQt4.QtGui import QApplication,QMessageBox
from PyQt4.QtCore import QObject
import PyOnyx.ui

if __name__ == "__main__":
   app = QApplication(argv)
   app.setApplicationName("ack_widget")
   
   if len(argv) < 3:
      print "ack_widget <title_text> <message_text>"
      print "Exit value (0) for 'Yes' and (-1) for 'No'"
      exit(-10)

   about = PyOnyx.ui.MessageDialog(QMessageBox.Icon(QMessageBox.Information), app.tr(argv[1]), app.tr(argv[2]), QMessageBox.No | QMessageBox.Yes)


   decision = about.exec_()

   if decision == 16384:
      # 16384 - Yes
      exit(0)
   else:
      # 65536 - No
      exit(-1)
