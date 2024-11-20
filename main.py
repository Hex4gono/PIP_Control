#clases
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
import json
import serial # type: ignore
import pyautogui # type: ignore
from GUI.menu import Ui_MainWindow

# variables
ArduinoPort = "COM8"
with open("data/controllers.json", "r") as file:
    controles = json.load(file)

serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = ArduinoPort
serialInst.open()





caracteres = ['mouseUp','mouseDown','mouseRight','mouseLeft','mouseClickLeft','mouseClickRight','up', 'down', 'right', 'left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '-', '_', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '+', '=', ':', ';', '"', '\'']
class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.
        self.ui.CerrarButton.clicked.connect(self.close)#Boton para cerrar
        self.ui.cargarButton
        #Haces un array con todos los caracteres seleccionables y despues la pones de accion en todos los combo box
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
        self.ui.Boton5Sel.addItems(caracteres)
        self.ui.Boton6Sel.addItems(caracteres)
        self.ui.Boton7Sel.addItems(caracteres)
        self.ui.Boton8Sel.addItems(caracteres)
        self.ui.controlesComboBox.addItems(controles.keys())
        print(controles)

        
    def cargarControl(self):
        controlActual = controles[self.ui.controlesComboBox.currentText()]
        for tecla in controlActual.values():
            if tecla not in caracteres:
                print("la tecla en el json no es valida")
                break
        print(controlActual)
        print(controlActual["Boton1Sel"])
        self.ui.XNegCar.currentText() == controlActual["XNegCar"]
        self.ui.XPosCar.currentText() == controlActual["XPosCar"]
        self.ui.YNegCar.currentText() == controlActual["YNegCar"]
        self.ui.YPosCar.currentText() == controlActual["YPosCar"]
        self.ui.XNegCar_2.currentText() == controlActual["XNegCar_2"]
        self.ui.XPosCar_2.currentText() == controlActual["XPosCar_2"]
        self.ui.YNegCar_2.currentText() == controlActual["YNegCar_2"]
        self.ui.YPosCar_2.currentText() == controlActual["YPosCar_2"]
        self.ui.Boton1Sel.currentText() == controlActual["Boton1Sel"]
        self.ui.Boton2Sel.currentText() == controlActual["Boton2Sel"]
        self.ui.Boton3Sel.currentText() == controlActual["Boton3Sel"]
        self.ui.Boton4Sel.currentText() == controlActual["Boton4Sel"]
        self.ui.Boton5Sel.currentText() == controlActual["Boton5Sel"]
        self.ui.Boton6Sel.currentText() == controlActual["Boton6Sel"]
        self.ui.Boton7Sel.currentText() == controlActual["Boton7Sel"]
        self.ui.Boton8Sel.currentText() == controlActual["Boton8Sel"] 
        
if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.
    
while True:
	if serialInst.in_waiting:
		packet = serialInst.readline()
		print(packet.decode('utf').rstrip('\n'))
 