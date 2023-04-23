# -*- coding: utf-8 -*- #

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from mainUI import ui
from win32api import GetLastError
from win32gui import (FindWindow, ShowWindow, MessageBox,
                      GetWindowText, SetWindowText)
from win32con import *

class Dialog(ui):
    def __init__(self, parent = None):
        super(Dialog, self).__init__(parent)
        self.initUI(self)
        self.thisHwnd = FindWindow(None, self.windowTitle())
        
    def initUI(self, t):
        self.Find.clicked.connect(self.FindF)
        self.Tset.clicked.connect(self.changeTitle)
        self.hide.clicked.connect(self.hideWin)
        self.mini.clicked.connect(self.minWin)
        self.restore.clicked.connect(self.reWin)
        self.max.clicked.connect(self.maxWin)
        
    def maxWin(self):
        ShowWindow(self.hwnd, SW_MAXIMIZE)
        
    def reWin(self):
        ShowWindow(self.hwnd, SW_RESTORE)
        
    def minWin(self):
        ShowWindow(self.hwnd, SW_MINIMIZE)
        
    def hideWin(self):
        ShowWindow(self.hwnd, SW_HIDE)
        
    def changeTitle(self):
        if not self.chT.text():
            MessageBox(self.thisHwnd, "请输入要设置的标题！", "警告",
                       MB_ICONWARNING | MB_OK)
            return
        SetWindowText(self.hwnd, self.chT.text())
        MessageBox(self.thisHwnd, "设置完成！", "提示", MB_ICONINFORMATION
                   |MB_OK)
        
    def FindF(self):
        self.title = (self.titleInput.text() if self.titleInput.text() else
               None)
        self.cls = (self.classInput.text() if self.classInput.text() else
             None)
        self.hwnd = (int(self.handleInput.text()) if self.handleInput.text() else
              None)
        if self.hwnd == None:
            self.hwnd = FindWindow(self.cls, self.title)
        if self.hwnd == 0:
            MessageBox(self.thisHwnd, "输入的数据无效！", "错误", MB_ICONERROR|MB_OK)
            return
        self.chT.setText(GetWindowText(self.hwnd))
        self.Hset.setText(str(self.hwnd))

if __name__ == '__main__':
    app = QApplication([])
    win = Dialog()
    win.show()
    app.exec_()
