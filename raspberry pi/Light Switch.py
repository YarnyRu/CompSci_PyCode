from gpiozero import LED, Button
from time import sleep

red_led = LED(17)
btn = Button(4)

while True:
    if btn.is_pressed:
        print("Button is pressed")
        red_led.on()
        sleep(5)
        red_led.off()