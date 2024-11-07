import time
import pyfirmata


board = pyfirmata.ArduinoMega('COM7')
iterator = pyfirmata.util.Iterator(board)
iterator.start()

class led:
    def __init__(self, pin):
        self.pin = pin
        self.port = board.digital[pin]
        self.state = 2
    
                
        
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
                led.port.write(blinkCounter)               
            if led.state == 2:
                led.port.write(1)
            
            
blinkCounter = 0