import serial # type: ignore
import pyautogui # type: ignore

# aca voy a poner una clase para la conexion con arduino


class arduino:
    def __init__(self, inputs):
        # como argumento recibe una lista de los inputs
        self.inputs = inputs
    
    def empezarComunicacion(self,port = 'COM1', baudRate = 9600):
        while True:
            try:
                self.ser = serial.Serial(port,baudRate)
            except Exception as error:
                print(f"no se pudo abrir la comunicacion con puerto {port}, error: {error}")
                port = input("Ingrese otro puerto : ")
                continue
            break
            
    def cerrarComunicacion(self):
        try: 
            self.ser.close()
        except NameError:
            print("Error: se trato de cerrar un puerto no abierto previamente")
            
    def recibirTeclas(self):
        # [l3,r3,botones(1-8),joysticks]
        self.teclasASimular = []
        self.teclasList = list(self.ser.readLine())
        for tecla in self.teclasList:
            if tecla == 1:
                self.teclasASimular.append(True)
            elif abs(tecla) > 200:
                self.teclasASimular.append(True)
            else:
                self.teclasASimular.append(False)
        return self.teclasASimular, self.teclasList
    
    def simularTeclas(self, inputs, inputKeys):
        for i in range(0, len(inputKeys)):
            if inputs[i]:
                if "mouse" in inputKeys[i]:
                    # mover el mouse
                    if "ClickLeft" in inputKeys[i]:
                        # clickear
                        pyautogui.leftClick()
                        continue
                    
                    elif "ClickRight" in inputKeys[i]:
                        pyautogui.rightClick()
                        continue
                    
                    else: # ineficiente pero tengo sueno
                        if "Left" in inputKeys[i]:
                            pyautogui.moveRel(-20)
                            
                        if "Right" in inputKeys[i]:
                            pyautogui.moveRel(20)
                            
                        if "Up" in inputKeys[i]:
                            pyautogui.moveRel(yOffset=-20)
                            
                        if "Down" in inputKeys[i]:
                            pyautogui.moveRel(yOffset=20)
                        
                else:
                    # tecla comun
                    pyautogui.press(inputKeys[i])
        
        
    