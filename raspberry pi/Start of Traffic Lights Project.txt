# Start of Traffic Lights Project for the Raspberry Pi
from gpiozero import LED
from time import sleep
# These pin numbers (17, 27, 10) need to correspond to the pins you connect your jumper wires to on the 40 pin header on the Raspberry Pi
red_led = LED(17)
yel_led = LED(27)
grn_led = LED(10)
while True:
    # Red light on
    red_led.on()
    yel_led.off()
    grn_led.off()
    sleep(2)
    # Now continue to add in the full sequence of lights