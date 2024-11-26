import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import pyqtSlot
import json
import pyautogui # type: ignore
from GUI.menu import Ui_MainWindow
from GUI.nameprompt import Ui_Dialog
from GUI.promptconfirmar import Ui_ConfirmarDialog
from arduino.comunicador import arduino

with open("data/controllers.json", "r") as file:
    controles = json.load(file)
    controles = dict(sorted(controles.items()))
caracteres = ['mouseUp','mouseDown','mouseRight','mouseLeft','mouseClickLeft','mouseClickRight','up', 'down', 'right', 'left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '-', '_', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '+', '=', ':', ';', '"', '\'']
class ConfirmarDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ConfirmarDialog()
        self.ui.setupUi(self)
        self.setGeometry(300, 300, 300, 100)
        
    def eliminacionConfirmada(self):
        controles.pop(comboBox.currentText())
        with open("data/controllers.json",'w') as file:
            json.dump(controles, file, indent = 4)
        comboBox.clear()
        comboBox.addItems(controles.keys())
    
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Ventana Secundaria')
        self.setGeometry(300, 300, 250, 150)

        
    def aceptarguardar(self):
        nombreconfig = self.ui.nombreguardar.text()
        x = {nombreconfig:{}}
        for i in range(len(widgets)):
            x[nombreconfig][widgets[i].objectName()] = widgets[i].currentText()
        controles.update(x)
        with open("data/controllers.json",'w') as file:
            json.dump(controles, file, indent = 4)
        
        comboBox.clear()
        comboBox.addItems(controles.keys())

class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.
        self.ui.CerrarButton.setGeometry(271,1,161,23)
        # Haces un array con todos los caracteres seleccionables y despues la pones de accion en todos los combo box
        global widgets 
        widgets = [self.ui.XNegCar,self.ui.XPosCar,self.ui.YNegCar,self.ui.YPosCar,self.ui.XNegCar_2,self.ui.XPosCar_2,self.ui.YNegCar_2,self.ui.YPosCar_2,self.ui.Boton1Sel,self.ui.Boton2Sel,self.ui.Boton3Sel,self.ui.Boton4Sel,self.ui.Boton5Sel,self.ui.Boton6Sel,self.ui.Boton7Sel,self.ui.Boton8Sel,self.ui.L3Sel,self.ui.R3Sel]
        for i in widgets:
            i.addItems(caracteres)
        global comboBox
        comboBox = self.ui.controlesComboBox
        comboBox.addItems(controles.keys())
    def sortearControl(self):
        if self.ui.SortButton.text == "A-Z":
            self.ui.SortButton.setText("Z-A")
            comboBox.clear()
            controles = dict(sorted(controles.items(),reverse=True))
            comboBox.addItems(controles.keys())
        else:
            self.ui.SortButton.setText("A-Z")
            comboBox.clear()
            controles = dict(sorted(controles.items()))
            comboBox.addItems(controles.keys())
        
    def cargarControl(self):
        controlActual = controles[self.ui.controlesComboBox.currentText()]
        for tecla in controlActual.values():
            if tecla not in caracteres:
                print("la tecla en el json no es valida, no deberia estar pasando esto")
                break
        claves = ["XNegCar", "XPosCar", "YNegCar", "YPosCar","XNegCar_2", "XPosCar_2", "YNegCar_2", "YPosCar_2","Boton1Sel", "Boton2Sel", "Boton3Sel", "Boton4Sel","Boton5Sel", "Boton6Sel", "Boton7Sel", "Boton8Sel","L3Sel","R3Sel"]
        for i in range(len(widgets)):
            widgets[i].setCurrentText(controlActual.get(claves[i]))
  

    def guardarControl(self):
        dialogo = Dialog()
        dialogo.exec_()  
        
    def eliminarControl(self):
        a = ConfirmarDialog() 
        a.exec_()  
    
    def desactivarControl(self):
        self.setEnabled(False)
        self.ui.AceptarButton.setEnabled(True)
        self.coso.cerrarComunicacion()
    
    def aplicarControl(self):
        self.setEnabled(False)
        self.ui.CerrarButton.setEnabled(True)
        self.coso = arduino()
        self.coso.empezarComunicacion()
        
    
    
     
if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.