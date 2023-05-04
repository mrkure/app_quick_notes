# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:03:13 2022

@author: mrkure
"""
# from mklib.lib_io import mkIO
# mkIO.activate_env(1, "work", __file__, 0)

import os
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QSystemTrayIcon, QAction, QMenu, QApplication

from lib._main_gui import Window, UI


class Notes(QSystemTrayIcon, QWidget):
    def __init__(self):
        super(QSystemTrayIcon, self).__init__()
        super(QWidget, self).__init__()        
     
#%% TRAY SETTINGS
        
        self.icon_running   = QIcon( rf'{os.path.dirname(__file__)}\res\dg.ico' )          
        self.icon_stopped   = QIcon( rf'{os.path.dirname(__file__)}\res\dr.ico')   

        self.menu           = QMenu() 
        self.setContextMenu(self.menu)
        self.setIcon(self.icon_running)
        self.option_close = QAction("Close")
        self.menu.addAction(self.option_close)
        self.window = Window(UI)
      
        self.window.hidden_signal.connect(self.on_window_hide)
        self.option_close.triggered.connect(self.on_close)   
        self.activated.connect(self.on_icon_click)
        
        self.running = True       
        self.setVisible(True)  
 
#%% METHODS
    def on_window_hide(self, string):
        self.window.hide()
        self.setIcon(self.icon_stopped)
        self.running = False
        

#%% CALLBACKS      
    def on_icon_click(self, button):   
        if button == 2 or button == 3:  # left click
            print('icon right click')
            if self.running:
                self.window.hide()
                self.setIcon(self.icon_stopped)
                self.running = False
            else:
                self.window.show()
                self.setIcon(self.icon_running)
                self.running = True

                        
    def on_close(self): 
        self.window.save_data()
        self.window.close()
        self.hide()
        QtCore.QCoreApplication.quit()  

#%% MAIN  
if __name__ == "__main__":
    app = QApplication([])
    notes = Notes()
    app.exec()