from machine import Pin
from utime import sleep
import _thread

led = Pin('GP18', Pin.OUT)
btn = Pin('GP15', Pin.IN, Pin.PULL_DOWN)
buzzer = Pin(16, Pin.OUT)
led.off()
global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
    while True:
        if btn.value() == 1:
            button_pressed = True
        utime.sleep(0.01)
        
_thread.start_new_thread(button_reader_thread, ())

if button_pressed == True:
    led.value(1)
    for i in range(10):
        buzzer.value(1)
        sleep(0.2)
        buzzer.value(0)
        sleep(0.2)
    global button_pressed
    button_pressed = False