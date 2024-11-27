import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
from GUI.menu import Ui_MainWindow
from arduino.comunicador import arduino
from confirmarDialog import ConfirmarDialog
from nombreDialog import Dialog
from PyQt5.QtCore import QTimer


with open("data/controllers.json", "r") as file:
    global controles
    controles = dict(sorted(json.load(file).items()))
caracteres = ['mouseUp','mouseDown','mouseRight','mouseLeft','mouseClickLeft','mouseClickRight','shift','control','tab','printscreen','space','enter','up', 'down', 'right', 'left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '-', '_', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '+', '=', ':', ';', '"', '\'','f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']
class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.
        self.ui.CerrarButton.setGeometry(271,1,161,23)
        # Haces un array con todos los caracteres seleccionables y despues la pones de accion en todos los combo box
        global widgets, comboBox
        self.controlActivado = False
        widgets = [self.ui.XNegCar,self.ui.XPosCar,self.ui.YNegCar,self.ui.YPosCar,self.ui.XNegCar_2,self.ui.XPosCar_2,self.ui.YNegCar_2,self.ui.YPosCar_2,self.ui.L3Sel,self.ui.R3Sel,self.ui.Boton1Sel,self.ui.Boton2Sel,self.ui.Boton3Sel,self.ui.Boton4Sel,self.ui.Boton5Sel,self.ui.Boton6Sel,self.ui.Boton7Sel,self.ui.Boton8Sel]
        for i in widgets:
            i.addItems(caracteres)
            i.setMaxVisibleItems(10)
        comboBox = self.ui.controlesComboBox
        comboBox.addItems(controles.keys())
        
        self.timerArduino = QTimer(self)
        self.timerArduino.start(16)  # 60 fps (esperemos que ande al mismo tienpo que el arduino por arte de magia)
        if self.controlActivado:
            self.timerArduino.timeout.connect(self.refrescarArduino)
        
        
    def sortearControl(self):
        orden_inverso = self.ui.SortButton.text() == "A-Z"
        self.ui.SortButton.setText("Z-A" if orden_inverso else "A-Z")
        comboBox.clear()
        comboBox.addItems(sorted(controles.keys(), reverse=orden_inverso))
           
    def cargarControl(self):
        controlActual = controles.get(self.ui.controlesComboBox.currentText())
        claves = ["XNegCar", "XPosCar", "YNegCar", "YPosCar","XNegCar_2", "XPosCar_2", "YNegCar_2", "YPosCar_2","L3Sel","R3Sel","Boton1Sel", "Boton2Sel", "Boton3Sel", "Boton4Sel","Boton5Sel", "Boton6Sel", "Boton7Sel", "Boton8Sel"]
        for i in range(len(widgets)):
            widgets[i].setCurrentText(controlActual.get(claves[i]))

    def guardarControl(self):
        dialogo = Dialog(controles, widgets, comboBox)
        dialogo.exec_()  
        
    def eliminarControl(self):
        confirmar = ConfirmarDialog(controles, self.ui.controlesComboBox)
        confirmar.exec_()
        
    def desactivarControl(self):
        self.controlActivado = False
        self.setEnabled(False)
        self.ui.AceptarButton.setEnabled(True)
        plaquinia.cerrarComunicacion()
        for e in widgets:
            e.setEnabled(True)
        
    def aplicarControl(self):

        self.controlActivado = True
        self.setEnabled(False)
        self.ui.CerrarButton.setEnabled(True)
        temp = []
        for e in widgets:
            temp.append(e.currentText()) # agarro todos los textos de los combobox
        global plaquinia
        plaquinia = arduino(temp)
        plaquinia.empezarComunicacion()
        for e in widgets:
            e.setEnabled(False)
      
    def refrescarArduino(self):
          if self.controlActivado:
                plaquinia.simularTeclas(plaquinia.recibirTeclas())
              
        
    def buscarControl(self):
        aBuscar = self.ui.searchLineEdit.text()
        if aBuscar != "":
            self.ui.controlesComboBox.clear()
            self.ui.controlesComboBox.showPopup()
            for elemento in controles.keys():
                if aBuscar in elemento:
                    self.ui.controlesComboBox.addItem(elemento)
        else:
            self.ui.controlesComboBox.clear()
            self.ui.controlesComboBox.addItems(controles.keys())
        
            
if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).i
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    app.setStyle("Windows")
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.
    
# event loop?    eee no se
"""
while True:
    if controlActivado:
        plaquinia.recibirTeclas()"""