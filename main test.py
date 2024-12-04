import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import json
from GUI.menu import Ui_MainWindow
from confirmarDialog import ConfirmarDialog
from nombreDialog import Dialog
from configuracionDialog import ConfiguracionDialog
import serial  # type: ignore
import pyautogui  # type: ignore


class ArduinoThread(QThread):
    """Hilo para manejar la comunicación con Arduino."""
    data_received = pyqtSignal(list, list)  # Señal para enviar datos recibidos a la GUI

    def __init__(self, arduino_instance):
        super().__init__()
        self.arduino = arduino_instance
        self.running = False

    def run(self):
        """Lógica del hilo: recibir datos continuamente mientras esté activo."""
        self.running = True
        while self.running:
            try:
                teclasASimular, teclasList = self.arduino.recibirTeclas()
                self.data_received.emit(teclasASimular, teclasList)
            except Exception as e:
                print(f"Error en la comunicación con Arduino: {e}")
                self.running = False

    def stop(self):
        """Detener el hilo."""
        self.running = False
        self.wait()


class arduino:
    """Clase para manejar la comunicación y simulación con Arduino."""

    def __init__(self, inputs):
        self.inputs = inputs
        with open(r"data/config.json", "r") as file:
            config = json.load(file)
            self.sens = config["sensibilidad"]
            self.zm = config["zona muerta"]

    def empezarComunicacion(self, port="COM1", baudRate=9600):
        try:
            self.ser = serial.Serial(port, baudRate)
        except Exception as error:
            print(f"No se pudo abrir la comunicación con el puerto {port}, error: {error}")

    def cerrarComunicacion(self):
        try:
            self.ser.close()
        except AttributeError:
            print("Error: se intentó cerrar un puerto no abierto previamente")

    def recibirTeclas(self):
        """Recibir datos desde Arduino."""
        self.teclasASimular = []
        self.teclasList = list(map(int, self.ser.readline().decode("utf-8").strip()[1:-1].split(",")))  # Decodificar datos
        for tecla in self.teclasList:
            if tecla == 1:
                self.teclasASimular.append(True)
            elif abs(tecla) > self.zm:  # Usar zona muerta
                self.teclasASimular.append(True)
            else:
                self.teclasASimular.append(False)
        return self.teclasASimular, self.teclasList

    def simularTeclas(self, inputs, inputKeys):
        """Simular teclas según datos recibidos."""
        for i in range(len(inputKeys)):
            if inputs[i]:
                if "mouse" in inputKeys[i]:
                    if "ClickLeft" in inputKeys[i]:
                        pyautogui.mouseDown(button="left")
                    elif "ClickRight" in inputKeys[i]:
                        pyautogui.mouseDown(button="right")
                    elif "Left" in inputKeys[i]:
                        pyautogui.moveRel(-self.sens, 0)
                    elif "Right" in inputKeys[i]:
                        pyautogui.moveRel(self.sens, 0)
                    elif "Up" in inputKeys[i]:
                        pyautogui.moveRel(0, -self.sens)
                    elif "Down" in inputKeys[i]:
                        pyautogui.moveRel(0, self.sens)
                else:
                    pyautogui.keyDown(inputKeys[i])
            elif "mouse" in inputKeys[i]:
                if "ClickLeft" in inputKeys[i]:
                    pyautogui.mouseUp(button="left")
                elif "ClickRight" in inputKeys[i]:
                    pyautogui.mouseUp(button="right")
            else:
                pyautogui.keyUp(inputKeys[i])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CerrarButton.setGeometry(271, 1, 161, 23)
        self.ui.ConfiguracionButton.setStyleSheet("background-image : url(assets/configGear.png);")

        global widgets, comboBox
        self.controlActivado = False
        widgets = [self.ui.XNegCar, self.ui.XPosCar, self.ui.YNegCar, self.ui.YPosCar,
                   self.ui.XNegCar_2, self.ui.XPosCar_2, self.ui.YNegCar_2, self.ui.YPosCar_2,
                   self.ui.L3Sel, self.ui.R3Sel, self.ui.Boton1Sel, self.ui.Boton2Sel,
                   self.ui.Boton3Sel, self.ui.Boton4Sel, self.ui.Boton5Sel, self.ui.Boton6Sel,
                   self.ui.Boton7Sel, self.ui.Boton8Sel]
        
        caracteres = ['mouseUp','mouseDown','mouseRight','mouseLeft','mouseClickLeft','mouseClickRight','shift','control','tab','printscreen',
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

        self.arduino_instance = None
        self.arduino_thread = None

    def aplicarControl(self):
        """Configurar y activar la comunicación con Arduino."""
        self.controlActivado = True
        self.ui.CerrarButton.setEnabled(True)
        self.ui.AceptarButton.setEnabled(False)
        temp = [e.currentText() for e in widgets]

        self.arduino_instance = arduino(temp)
        self.arduino_instance.empezarComunicacion()

        self.arduino_thread = ArduinoThread(self.arduino_instance)
        self.arduino_thread.data_received.connect(self.procesarDatosArduino)
        self.arduino_thread.start()

        for widget in widgets:
            widget.setEnabled(False)

    def desactivarControl(self):
        """Desactivar la comunicación con Arduino."""
        self.controlActivado = False
        self.ui.CerrarButton.setEnabled(False)
        self.ui.AceptarButton.setEnabled(True)
        if self.arduino_thread:
            self.arduino_thread.stop()
        if self.arduino_instance:
            self.arduino_instance.cerrarComunicacion()

        for widget in widgets:
            widget.setEnabled(True)

    def procesarDatosArduino(self, teclasASimular, teclasList):
        """Procesar los datos recibidos del hilo de Arduino."""
        self.arduino_instance.simularTeclas(teclasASimular, self.inputs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
