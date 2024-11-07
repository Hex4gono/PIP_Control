from GUIs import label,interfaz
from StandardFirmata import arduino
import time
import json
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from palabrino.GUIs.label import Ui_MainWindow




screen = arduino.display(25)
running = True
screen.leds[2].state = 0



class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.

if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.


#  Main Loop
while running:
    screen.refresh()
    blinkCounter+=1
    if blinkCounter > 1:
        blinkCounter = 0
    time.sleep(0.5)








