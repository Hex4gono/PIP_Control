import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSlot
from GUI.menu import Ui_MainWindow
from GUI.nameprompt import Ui_Dialog
from GUI.promptconfirmar import Ui_ConfirmarDialog
def guardarControl(self):
    dialogo = Dialog()
    dialogo.exec_()  
        
def eliminarControl(self):
    a = ConfirmarDialog() 
    a.exec_()  
    