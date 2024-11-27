import serial # type: ignore

# aca voy a poner una clase para la conexion con arduino


class arduino:
    def __init__(self, inputs):
        self.inputs = inputs
    
    def empezarComunicacion(self,port = 'COM8', baudRate = 9600):
        try:
            self.ser = serial.Serial(port,baudRate)
        except Exception as error:
            print(f"no se pudo abrir la comunicacion: {error}")
            
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
            elif abs(tecla) > 50:
                self.teclasASimular.append(True)
            else:
                self.teclasASimular.append(False)
    