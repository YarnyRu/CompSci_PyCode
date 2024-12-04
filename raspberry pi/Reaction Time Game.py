from gpiozero import LED, Button
from time import time, sleep
from random import randint

led = LED(17)
btn = Button(4)

while True:
    sleep(randint(1,10))
    led.on()
    start = time()
    btn.wait_for_press()
    end = time()
    led.off()
    print(end - start)
    btn.wait_for_press()
  


