import serial # type: ignore

# aca voy a poner una clase para la conexion con arduino


class arduino:
    def __init__(self):
        pass
    
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
        self.teclasList = []
        self.teclasString = self.ser.readLine()
        for tecla in self.teclasString:
            if tecla == "1":
                self.teclasList.append(True)
            else:
                self.teclasList.append(False)
    