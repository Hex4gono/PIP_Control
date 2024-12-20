import serial # type: ignore
import pyautogui # type: ignore
import json


# aca voy a poner una clase para la conexion con arduino

pyautogui.FAILSAFE = False
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
            self.ser = serial.Serial(port,baudRate,timeout = None)
        except FileNotFoundError as error:
            print(f"no se pudo abrir la comunicacion, conecte el arduino a {port}, error : {error}")
            raise
        except Exception as error:
            print(f"no se pudo abrir la comunicacion con puerto {port}, error: {error}")
            
    def cerrarComunicacion(self):
        try: 
            self.ser.close()
        except NameError or AttributeError:
            print("Error: se trato de cerrar un puerto no abierto previamente")
            
    def recibirTeclas(self):
        # [l3,r3,botones(1-8),joysticks]
        self.teclasASimular = []
        buffer = b""
    
        if self.ser.in_waiting > 0:
            
            while b"|s" not in buffer:
                buffer += self.ser.read(self.ser.in_waiting)

            buffer = buffer[buffer.find(b"s|")+ 2 : buffer.find(b"|s")]
            self.teclasList = buffer.strip().decode("utf-8",'ignore').split(",")


            """
            self.teclasList = self.ser.read_until(b"|s")
            self.teclasList = self.teclasList[self.teclasList.find(b"s|") + 2 : self.teclasList.find(b"|s")]
            self.teclasList = self.teclasList.strip().decode("utf-8",'ignore').split(",")
            """
            #self.teclasList = self.ser.readline().strip().decode("utf-8",'ignore').split(",")
            
            for i in range(0, len(self.teclasList)):
                # digital
                try:
                    int(self.teclasList[i])
                except:
                    continue
                if i < 4:
                    # analog
                    if int(self.teclasList[i]) > self.zm:
                        self.teclasASimular.append(False)
                        self.teclasASimular.append(True)
                    
                    elif int(self.teclasList[i]) < -self.zm:
                        self.teclasASimular.append(True)
                        self.teclasASimular.append(False)

                    else:
                        self.teclasASimular.append(False)
                        self.teclasASimular.append(False)
                else:
                    # digital
                    if self.teclasList[i] == "1":
                        self.teclasASimular.append(True)
                    # fake
                    else:
                      self.teclasASimular.append(False)        
             
        else:
            try:
                if not self.ultimo:
                    for i in range(0, len(self.inputs)):
                        self.teclasASimular.append(False)
                else:
                    self.teclasASimular = self.ultimo
            except AttributeError:
                for i in range(0, len(self.inputs)):
                    self.teclasASimular.append(False)
                
        self.ultimo = self.teclasASimular        
        """
        print(self.teclasASimular)
        for e in self.teclasASimular:
            print(e)
        """
        return self.teclasASimular
        
         
        
        
    
    def simularTeclas(self, teclasBool):
        teclasKeys = self.inputs  # se me chispoteo asi que tengo que poner esto para no complicarme tanto
        #print(f"\n{teclasBool}\n{teclasKeys}")
        for i in range(0, len(teclasKeys)):
            try:
                if teclasBool[i]:
                    if "mouse" in teclasKeys[i]:
                        # mover el mouse
                            if "Left" in teclasKeys[i]:
                                pyautogui.moveRel(-self.sens/40, None, _pause = False)
                                    
                            if "Right" in teclasKeys[i]:
                                pyautogui.moveRel(self.sens/40, None, _pause = False)
                                
                            if "Up" in teclasKeys[i]:
                                pyautogui.moveRel(None, -self.sens/40, _pause = False)
                                    
                            if "Down" in teclasKeys[i]:
                                pyautogui.moveRel(None, self.sens/40, _pause = False)

                        
                    elif "clickLeft" in teclasKeys[i]:
                            # clickear
                        pyautogui.mouseDown(button="left", _pause = False)
                            
                    elif "clickRight" in teclasKeys[i]:
                        pyautogui.mouseDown(button="right", _pause = False)    
                        
                    else:
                        # tecla comun
                        pyautogui.keyDown(teclasKeys[i], _pause = False)     
                else:
                    if "mouse" in teclasKeys[i]:
                        if "ClickLeft" in teclasKeys[i]:
                            # clickear
                            pyautogui.mouseUp(button="left", _pause = False)
                            
                        if "ClickRight" in teclasKeys[i]:
                            pyautogui.mouseUp(button="right", _pause = False)
                        
                    else:

                        pyautogui.keyUp(teclasKeys[i], _pause = False)

            except IndexError:
                continue
                    
        
        
    