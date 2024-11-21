import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSlot
import json
import serial # type: ignore
import pyautogui # type: ignore
from GUI.menu import Ui_MainWindow
from GUI.nameprompt import Ui_Dialog
from GUI.promptconfirmar import Ui_ConfirmarDialog

with open("data/controllers.json", "r") as file:
    controles = json.load(file)
caracteres = ['mouseUp','mouseDown','mouseRight','mouseLeft','mouseClickLeft','mouseClickRight','up', 'down', 'right', 'left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '-', '_', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '+', '=', ':', ';', '"', '\'']
class ConfirmarDialog:
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox
        """
        self.setWindowTitle('Ventana Secundaria')
        self.setGeometry(300, 300, 250, 150)
        """
        
    def eliminacionConfirmada(self):
        pass
    
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Ventana Secundaria')
        self.setGeometry(300, 300, 250, 150)
        self.ui.buttonBox
        
    def aceptarguardar(self):
        nombreconfig = self.ui.nombreguardar.text()
        x = {nombreconfig:{}}
        for i in range(len(widgets)):
            x[nombreconfig][widgets[i].objectName()] = widgets[i].currentText()
        controles.update(x)
        with open("data/controllers.json",'r+') as file:
            json.dump(controles, file, indent = 4)
        comboBox.removeItem
        comboBox.addItem(controles.keys())

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
        print(widgets[0].objectName())
        for i in widgets:
            i.addItems(caracteres)
        global comboBox
        comboBox = self.ui.controlesComboBox
        comboBox.addItems(controles.keys())
        print(controles)
        
    def cargarControl(self):
        controlActual = controles[self.ui.controlesComboBox.currentText()]
        for tecla in controlActual.values():
            if tecla not in caracteres:
                print("la tecla en el json no es valida")
                break
        print(controlActual)
        print(controlActual["Boton1Sel"])
        claves = ["XNegCar", "XPosCar", "YNegCar", "YPosCar","XNegCar_2", "XPosCar_2", "YNegCar_2", "YPosCar_2","Boton1Sel", "Boton2Sel", "Boton3Sel", "Boton4Sel","Boton5Sel", "Boton6Sel", "Boton7Sel", "Boton8Sel"]
        for i in range(len(widgets)):
            widget = widgets[i]
            clave = claves[i]
            valor = controlActual.get(clave)
            widget.setCurrentText(valor)
            
    def guardarControl(self):
        print("me gusta la pa")
        # Crear instancia del diálogo y abrirlo
        dialogo = Dialog()  # Crear una instancia de Dialog
        dialogo.exec_()  # Mostrar el diálogo de manera modal
        print("me gusta la pa")
        
    def eliminarControl(self):    
        # Crear instancia del diálogo y abrirlo
        pepe = ConfirmarDialog()  # Crear una instancia de Dialog
        pepe.exec_()  # Mostrar el diálogo de manera modal
        print("me gusta la pa")

if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.
