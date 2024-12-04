import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
import json
import time
from GUI.menu import Ui_MainWindow
from confirmarDialog import ConfirmarDialog
from nombreDialog import Dialog
from configuracionDialog import ConfiguracionDialog
from arduino.comunicador import arduino


class ArduinoThread(QThread):
    
    datos = pyqtSignal(list)  # a este coso no le gusta que lo llamen adentro del constructor
    def __init__(self, arduinoInst):
        super().__init__()
        self.arduino = arduinoInst
        self.running = False

    def run(self):
        # recibe datos continuamente
        self.running = True
        while self.running:
            try:
                teclasASimular = self.arduino.recibirTeclas()
                self.datos.emit(teclasASimular)
            except Exception as e:
                print(f"Error en la comunicación con Arduino: {e}")
                self.running = False
            time.sleep(0.05)


    def stop(self):
        """Detener el hilo."""
        self.running = False
        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CerrarButton.setGeometry(271, 1, 161, 23)
        self.ui.ConfiguracionButton.setIcon(QIcon("assets/configGear.png"))
        
        global widgets, comboBox
        self.controlActivado = False
        widgets = [self.ui.XNegCar, self.ui.XPosCar, self.ui.YNegCar, self.ui.YPosCar,
                   self.ui.XNegCar_2, self.ui.XPosCar_2, self.ui.YNegCar_2, self.ui.YPosCar_2,
                   self.ui.L3Sel, self.ui.R3Sel, self.ui.Boton1Sel, self.ui.Boton2Sel,
                   self.ui.Boton3Sel, self.ui.Boton4Sel, self.ui.Boton5Sel, self.ui.Boton6Sel,
                   self.ui.Boton7Sel, self.ui.Boton8Sel]
        
        caracteres = ['mouseUp','mouseDown','mouseRight','mouseLeft','clickLeft','clickRight','shift','control','tab','printscreen',
                      'space','enter','up', 'down', 'right', 'left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.', '-',
                      '_', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '/', '\\', '|', '+', '=', ':',
                      ';', '"', '\'','f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']

        with open("data/controllers.json", "r") as file:
            global controles
            controles = dict(sorted(json.load(file).items()))
        comboBox = self.ui.controlesComboBox
        comboBox.addItems(controles.keys())

        for widget in widgets:
            widget.addItems(caracteres)
            widget.setMaxVisibleItems(10)


    def aplicarControl(self):
        try:
            self.controlActivado = True
            self.ui.CerrarButton.setEnabled(True)
            self.ui.AceptarButton.setEnabled(False)
            
            temp = []
            for e in widgets:
                temp.append(e.currentText())

            self.arduinoInst = arduino(temp)
            self.arduinoInst.empezarComunicacion()

            self.arduino_thread = ArduinoThread(self.arduinoInst)
            self.arduino_thread.datos.connect(self.recibirDatosArduino)
            self.arduino_thread.start()

            for widget in widgets:
                widget.setEnabled(False)
        except AttributeError:
            pass
        
    def cargarControl(self):    
        try:
            controlActual = controles.get(self.ui.controlesComboBox.currentText())
            claves = ["XNegCar", "XPosCar", "YNegCar", "YPosCar","XNegCar_2", "XPosCar_2", "YNegCar_2", "YPosCar_2","L3Sel","R3Sel",
                    "Boton1Sel","Boton2Sel", "Boton3Sel", "Boton4Sel","Boton5Sel", "Boton6Sel", "Boton7Sel", "Boton8Sel"]
            for i in range(len(widgets)):
                widgets[i].setCurrentText(controlActual.get(claves[i]))
        except AttributeError:
            pass
            
    
    def sortearControl(self):
        orden_inverso = self.ui.SortButton.text() == "A-Z"
        self.ui.SortButton.setText("Z-A" if orden_inverso else "A-Z")
        comboBox.clear()
        comboBox.addItems(sorted(controles.keys(), reverse=orden_inverso))
            
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
             
    def guardarControl(self):
        dialogo = Dialog(controles, widgets, comboBox)
        dialogo.exec_()  
        
    def eliminarControl(self):
        confirmar = ConfirmarDialog(controles, self.ui.controlesComboBox)
        confirmar.exec_()
          
    def abrirConfig(self):
        with open("data/config.json", "r") as file:
            config = ConfiguracionDialog(json.load(file))
            config.exec_()      
             
    def desactivarControl(self):
        """Desactivar la comunicación con Arduino."""
        self.controlActivado = False
        self.ui.CerrarButton.setEnabled(False)
        self.ui.AceptarButton.setEnabled(True)
        if self.arduino_thread:
            self.arduino_thread.stop()
        if self.arduinoInst:
            self.arduinoInst.cerrarComunicacion()

        for widget in widgets:
            widget.setEnabled(True)

    def recibirDatosArduino(self):
        self.arduinoInst.simularTeclas(self.arduinoInst.recibirTeclas())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
