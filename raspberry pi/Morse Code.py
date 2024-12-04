# Morse Code Messages using LEDs on the Raspberry Pi
from gpiozero import LED
from time import sleep
red = LED(4)
red.off()

while True:
    #Flash S in Morse (dot dot dot)
    for i in range(0, 3):
        red.on()
        sleep(0.3)
        red.off()
        sleep(0.3)
    sleep(1)
    #Flash O in Morse (dash dash dash)
    for i in range(0, 3):
        red.on()
        sleep(1)
        red.off()
        sleep(1)
    sleep(1)
    #Flash S in Morse (dot dot dot)
    for i in range(0, 3):
        red.on()
        sleep(0.3)
        red.off()
        sleep(0.3)
    sleep(2)

    
 