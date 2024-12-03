import serial # type: ignore
import pyautogui # type: ignore
from PyQt5.QtCore import QThread, pyqtSignal
import json
# aca voy a poner una clase para la conexion con arduino


class arduino:
    
    def __init__(self, inputs):
        # como argumento recibe una lista de los inputs
        self.inputs = inputs
        with open(r"data/config.json","r") as file:
            # no le gusta a json que cargue el archivo 2 veces
            a = json.load(file)
            self.sens = a["sensibilidad"]
            self.zm = a["zona muerta"]
    
    def empezarComunicacion(self,port = 'COM1', baudRate = 9600):
        try:
            self.ser = serial.Serial(port,baudRate)
        except FileNotFoundError as error:
            print(f"no se pudo abrir la comunicacion, conecte el arduino a {port}, error : {error}")
            raise
        except Exception as error:
            print(f"no se pudo abrir la comunicacion con puerto {port}, error: {error}")
            
    def cerrarComunicacion(self):
        try: 
            self.ser.close()
        except NameError:
            print("Error: se trato de cerrar un puerto no abierto previamente")
            
    def recibirTeclas(self):
        # [l3,r3,botones(1-8),joysticks]
        self.teclasASimular = []
        self.teclasList = list(self.ser.readline())
        print(self.teclasList)
        for tecla in self.teclasList:
            # digital
            if tecla == 1:
                self.teclasASimular.append(True)
            # analog
            elif tecla > self.zm:
                self.teclasASimular.append(False)
                self.teclasASimular.append(True)
                
            elif tecla < -self.zm:
                self.teclasASimular.append(True)
                self.teclasASimular.append(False)   
            # fake
            else:
                self.teclasASimular.append(False)
                
        return self.teclasASimular
    
    
    def simularTeclas(self, teclasBool):
        teclasKeys = self.inputs  # se me chispoteo asi que tengo que poner esto para no complicarme tanto
        print(f"\n{teclasBool},\n{teclasKeys}")
        for i in range(0, len(teclasKeys)):
            if teclasBool[i]:
                if "mouse" in teclasKeys[i]:
                    # mover el mouse
                    if "Left" in teclasKeys[i]:
                        pyautogui.moveRel(-self.sens)
                            
                    if "Right" in teclasKeys[i]:
                        pyautogui.moveRel(self.sens)
                        
                    if "Up" in teclasKeys[i]:
                        pyautogui.moveRel(0, -self.sens)
                            
                    if "Down" in teclasKeys[i]:
                        pyautogui.moveRel(0, self.sens)
                        
                elif "clickLeft" in teclasKeys[i]:
                        # clickear
                    pyautogui.mouseDown(button="left")
                        
                elif "clickRight" in teclasKeys[i]:
                    pyautogui.mouseDown(button="right")    
                    
                else:
                    # tecla comun
                    pyautogui.keyDown(teclasKeys[i])
                    
            else:
                if "mouse" in teclasKeys[i]:
                    if "ClickLeft" in teclasKeys[i]:
                        # clickear
                        pyautogui.mouseUp(button="left")
                        
                    if "ClickRight" in teclasKeys[i]:
                        pyautogui.mouseUp(button="right")
                    
                else:
                    pyautogui.keyUp(teclasKeys[i])
                    
        
        
    