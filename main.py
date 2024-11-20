import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
import json
import serial # type: ignore
import pyautogui # type: ignore


"""
from Archivo convertido con pyside2-uic archivo.ui > interfaz.py
import nombre de la clase del archivo convertido
"""
from GUI.menu import Ui_MainWindow


with open("data/controllers.json", "r") as file:
    controles = json.load(file)

"""
arduino = serial.Serial("COM8", 9600)
arduino.Open()
"""
caracteres = ['mouseUp','mouseDown','mouseRight','mouseLeft','mouseClickLeft','mouseClickRight','up', 'down', 'right', 'left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '-', '_', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '+', '=', ':', ';', '"', '\'']
class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.
        self.ui.CerrarButton.clicked.connect(self.close)#Boton para cerrar
        self.ui.cargarButton
        self.ui.guardarButton
        #Haces un array con todos los caracteres seleccionables y despues la pones de accion en todos los combo box
        global widgets 
        widgets = [self.ui.XNegCar,self.ui.XPosCar,self.ui.YNegCar,self.ui.YPosCar,self.ui.XNegCar_2,self.ui.XPosCar_2,self.ui.YNegCar_2,self.ui.YPosCar_2,self.ui.Boton1Sel,self.ui.Boton2Sel,self.ui.Boton3Sel,self.ui.Boton4Sel,self.ui.Boton5Sel,self.ui.Boton6Sel,self.ui.Boton7Sel,self.ui.Boton8Sel]
        for i in widgets:
            i.addItems(caracteres)
        self.ui.controlesComboBox.addItems(controles.keys())
        print(controles)
        
    def cargarControl(self):
        controlActual = controles[self.ui.controlesComboBox.currentText()]
        for tecla in controlActual.values():
            if tecla not in caracteres:
                print("la tecla en el json no es valida")
                break
        claves = ["XNegCar", "XPosCar", "YNegCar", "YPosCar","XNegCar_2", "XPosCar_2", "YNegCar_2", "YPosCar_2","Boton1Sel", "Boton2Sel", "Boton3Sel", "Boton4Sel","Boton5Sel", "Boton6Sel", "Boton7Sel", "Boton8Sel"]
        for i in range(len(widgets)):
            widget = widgets[i]
            clave = claves[i]
            valor = controlActual.get(clave)
            widget.setCurrentText(valor)
        
    def guardarControl(self):
        pass
    
    
    
if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.
 