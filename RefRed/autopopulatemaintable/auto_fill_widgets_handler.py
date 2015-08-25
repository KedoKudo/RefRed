from PyQt4.QtGui import QApplication
from PyQt4 import QtCore
import time

class AutoFillWidgetsHandler(object):
    
    def __init__(self, parent=None):
        self.parent = parent
        self.setup()
        self.start()
        
    def setup(self):
        self.parent.ui.progressBar_check2.setValue(0)
        self.parent.ui.progressBar_check5.setValue(0)
        self.parent.ui.progressBar_check2.setVisible(False)
        self.parent.ui.progressBar_check5.setVisible(False)
        self.parent.ui.check1.setVisible(False)
        self.parent.ui.check2.setVisible(False)
        self.parent.ui.check3.setVisible(False)
        self.parent.ui.check4.setVisible(False)
        self.parent.ui.check5.setVisible(False)
    
    def start(self):
        self.parent.ui.frame_autofill_check_status.setVisible(True)
        QApplication.processEvents()
        
    def end(self):
        time.sleep(2)
        self.parent.ui.frame_autofill_check_status.setVisible(False)
        self.parent.ui.progressBar_check3.setValue(0)
        self.parent.ui.progressBar_check5.setValue(0)
        self.parent.ui.progressBar_check3.setVisible(False)
        self.parent.ui.progressBar_check5.setVisible(False)
        self.parent.ui.check1.setVisible(False)
        self.parent.ui.check2.setVisible(False)
        self.parent.ui.check3.setVisible(False)
        self.parent.ui.check4.setVisible(False)
        self.parent.ui.check5.setVisible(False)
        
    def step1(self):
        self.parent.ui.check1.setVisible(True)
        QApplication.processEvents()
        
    def step2(self):
        self.parent.ui.check2.setVisible(True)
        QApplication.processEvents()
        
    def step3(self):
        self.parent.ui.check3.setVisible(True)
        QApplication.processEvents()

    def step4(self):
        self.parent.ui.check4.setVisible(True)
        QApplication.processEvents()

    def step5(self):
        self.parent.ui.check5.setVisible(True)
        QApplication.processEvents()

class DelayClosing(QtCore.QThread):
    
    def setup(self, parent, delay=3):
        self.parent = parent
        self.delay = delay
        
    def run(self):
        time.sleep(self.delay)
        self.parent.ui.frame_autofill_check_status.setVisible(False)
        QApplication.processEvents()
        