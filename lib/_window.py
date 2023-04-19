# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:38:40 2023

@author: CAZ2BJ
"""
import os, sys, time
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import QPoint, pyqtSignal

from lib_save_load import Tools

UI = rf'{os.path.dirname(__file__)}\window.ui' 

import ctypes
user32 = ctypes.windll.user32
monitors_num = user32.GetSystemMetrics(80)

class Window(QtWidgets.QWidget):
    
    hidden_signal = pyqtSignal(str)
    
    def __init__(self, UI):
        super(Window, self).__init__()
        uic.loadUi(UI, self)
        self.setWindowFlags ( QtCore.Qt.FramelessWindowHint  | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool ) 
        
        # if switched from 3 mons to 1 and app would be out of bounds
        self.dic = Tools.load_params()
        if (self.dic['x'] > 1900 or self.dic["x"] < 0) and monitors_num == 1:
            self.dic['x'] = 500
        # set geometry and ui components
        self.setGeometry(self.dic["x"], self.dic["y"], self.dic["w"], self.dic["h"])        
        self.textEdit.setText(self.dic["string"])        
        sizegrip = QtWidgets.QSizeGrip(self)
        sizegrip.setStyleSheet("background-color: gray;") 
        self.verticalLayout.addWidget(sizegrip, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        # signall connections
        self.pushButton_2.clicked.connect(self.on_top_changed)
        self.pushButton.clicked.connect(self.on_hide)
        self.textEdit.textChanged.connect(self.on_text_changed)
        self.on_top = True
        self.show()
        
#%% METHODS    
    def save_data(self):
        self.dic['x'] = self.frameGeometry().x() 
        self.dic['y'] = self.frameGeometry().y()
        self.dic['w'] = self.frameGeometry().width()  
        self.dic['h'] = self.frameGeometry().height()  
        self.dic['string'] = self.textEdit.toPlainText()
        Tools.save_params(self.dic)          

#%% SIGNALS        
    def on_top_changed(self):
        if self.on_top:
            self.setWindowFlags ( QtCore.Qt.FramelessWindowHint  |  QtCore.Qt.Tool ) 
            self.show()
            self.on_top = False
            
        else:
            self.setWindowFlags ( QtCore.Qt.FramelessWindowHint  | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool ) 
            self.show()
            self.on_top = True            
        
    def on_text_changed(self):
        self.save_data()
                
    def on_hide(self):
        self.hidden_signal.emit('hidden')

#%% EVENTS        
    def resizeEvent(self, event):
        self.resizing_time = time.time()

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()
        print("old", self.oldPos.y() ,"window", self.geometry().y())

    def mouseMoveEvent(self, evt):
        if  time.time() - self.resizing_time > 0.4:
            print(self.oldPos.y() - self.geometry().y())
            delta = QPoint(evt.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = evt.globalPos()    

    def enterEvent(self, event):
        print('enter event')
        self.mouse_over_app = True
        
    def leaveEvent(self, event):
        print('leave event')
   

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(UI)
    app.exec_() 
