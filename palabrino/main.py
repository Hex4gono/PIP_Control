import time
import pyfirmata
import interfaz

board = pyfirmata.ArduinoMega('COM7')

class led:
    def __init__(self, pin):
        self.pin = pin #posicion [x, y]
        self.port = board.digital[pin]
        self.state = 0
    
                
        
class display:
    def __init__(self, ledAmount):
        self.leds = []
        self.ledAmount = ledAmount
        for i in range(2, ledAmount + 2):
            self.leds.append(led(i))  #led.pin
            
    def refresh(self):
        for led in self.leds:
            if led.state == 0:
                led.port.write(0)
            if led.state == 1:
                led.port.write(variablerandomquenecesitoparaquetitile)               
            if led.state == 2:
                led.port.write(1)
            
            
screen = display(25)
running = True
variablerandomquenecesitoparaquetitile = 0

screen.leds[2].state = 0

while running:
    screen.refresh()
    variablerandomquenecesitoparaquetitile+=1
    if variablerandomquenecesitoparaquetitile > 1:
        variablerandomquenecesitoparaquetitile = 0
    time.sleep(0.5)








