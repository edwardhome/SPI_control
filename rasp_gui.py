from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PySide2.QtCore import Qt

# export DISPLAY=':0.0' 利用該指令遠端ssh開啟gui程式

def handleCalc():
    QMessageBox.about(window,"Message","Hello Raspberry Pi")

def stop():
    app.quit()

app = QApplication([]) #建立應用程式
window = QMainWindow() #建立視窗物件
window.resize(800,480) #確定視窗大小
window.move(0,0) #開啟左上角在螢幕的位置
window.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

button = QPushButton("Test",window)
button.move(100,100)
button.resize(100,100)
button.clicked.connect(handleCalc)

button_stop = QPushButton("stop",window)
button_stop.move(100,250)
button_stop.resize(100,100)
button_stop.clicked.connect(stop)

window.show()
app.exec_()