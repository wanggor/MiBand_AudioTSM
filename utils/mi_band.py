# -*- coding: utf-8 -*-
from PyQt5.QtCore import QThread, pyqtSignal
import random
import time

class MiBand(QThread):
    value = pyqtSignal(int)
    def __init__(self,parent=None):
        super(MiBand, self).__init__(parent)
        self.loop = True
        
    def run(self):
        n = 40
        while self.loop:
            n = (n +3)%120
            self.value.emit(n)
            time.sleep(1)