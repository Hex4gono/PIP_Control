import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot

"""
from Archivo convertido con pyside2-uic archivo.ui > interfaz.py
import nombre de la clase del archivo convertido
"""
from menu import Ui_MainWindow

class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.
        self.ui.CerrarButton.clicked.connect(self.close)#Boton para cerrar
        #Haces un array con todos los caracteres seleccionables y despues la pones de accion en todos los combo box
        caracteres = ['↑', '↓', '→', '←', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '-', '_', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '+', '=', ':', ';', '"', '\'']
        self.ui.XNegCar.addItems(caracteres)
        self.ui.XPosCar.addItems(caracteres)
        self.ui.YNegCar.addItems(caracteres)
        self.ui.YPosCar.addItems(caracteres)
        self.ui.XNegCar_2.addItems(caracteres)
        self.ui.XPosCar_2.addItems(caracteres)
        self.ui.YNegCar_2.addItems(caracteres)
        self.ui.YPosCar_2.addItems(caracteres)
        self.ui.Boton1Sel.addItems(caracteres)
        self.ui.Boton2Sel.addItems(caracteres)
        self.ui.Boton3Sel.addItems(caracteres)
        self.ui.Boton4Sel.addItems(caracteres)
        configuraciones = ["configuracion 1", "configuracion 2", "configuracion 3", "configuracion 4", "configuracion 5", "configuracion 6", "configuracion 7", "configuracion 8", "configuracion 9"]
        self.ui.comboBox.addItems(configuraciones)
        
if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.
 