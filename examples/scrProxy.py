import sys
from PyQt4.QtGui import QApplication, QMessageBox
from PyQt4.QtCore import QEvent
from PyOnyxScreen import ScreenProxy, ScreenCommand

class OnyxQWidget(QMessageBox):
   def __init__(self):
      QMessageBox.__init__(self)
      self.setText("Hello, World!")
      self.exec_()
      
   def event(self, event):
        ret =  QMessageBox.event(self, event)
        if (event.type()==QEvent.UpdateRequest) and ScreenProxy.instance().isUpdateEnabled():
             ScreenProxy.instance().updateWidget(self, ScreenProxy.GU, True, ScreenCommand.WAIT_ALL)
        return ret
 
a = QApplication(sys.argv)

wid = OnyxQWidget()
 
print wid
