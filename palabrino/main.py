import interfaz
import arduino
import time
import json





screen = arduino.display(25)
running = True
screen.leds[2].state = 0




#  Main Loop
while running:
    screen.refresh()
    blinkCounter+=1
    if blinkCounter > 1:
        blinkCounter = 0
    time.sleep(0.5)








