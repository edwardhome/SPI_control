from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtUiTools import QUiLoader
import os
# export DISPLAY=':0.0' 利用該指令遠端ssh開啟gui程式
class Stats(QtCore.QObject): #該類別必須為QObject，才可以調用sender
    def __init__(self):
        super().__init__()
        self.ui =QUiLoader().load("main.ui")        
        self.ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint) #使其無邊框
        self.ui.resize(800,480)
        self.ui.move(0,0)
        self.ui.stop.clicked.connect(self.stop)
        self.ui.open.clicked.connect(self.open)
        self.ui.shutdown.clicked.connect(self.shutdown)
    def stop(self):
        app.quit()
    def open(self):
        pass
    def close(self):
        pass
    def add(self):
        pass
    def sub(self):
        pass
    def shutdown(self):
        qm = QMessageBox.question(self.ui,"您確定要關機","確定嗎？",QMessageBox.Yes |QMessageBox.No, QMessageBox.Yes)
        if qm == QMessageBox.Yes:
            os.system("shutdown -t 60")
        else:
            pass
app = QApplication([])
window = Stats()
window.ui.show()
app.exec_()


