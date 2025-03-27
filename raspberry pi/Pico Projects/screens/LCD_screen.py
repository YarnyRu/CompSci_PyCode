# Project 4 from https://github.com/geeekpi/picokit/tree/main
# Processor temperature display

from machine import Pin, SoftI2C, ADC
from pico_i2c_lcd import I2cLcd
from time import sleep, sleep_ms
import utime

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(4), scl=Pin(5), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

try:
   
    while True:
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = 27 - (reading - 0.706)/0.001721
        lcd.putstr("Hello RPi Pico!\n")
        lcd.putstr("CPU Temp:%.2f" % temperature)
        utime.sleep(2)
        sleep(1)
        lcd.clear()

except KeyboardInterrupt:
    # Turn off the display when the code is interrupted by the user
    print("Keyboard interrupt")
    lcd.backlight_off()
    lcd.display_off()