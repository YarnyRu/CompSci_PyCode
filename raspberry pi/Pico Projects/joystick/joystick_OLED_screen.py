from machine import Pin, ADC, SoftI2C
import utime
import ssd1306

# You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Start pixel in middle of screen
screen_x = 64
screen_y = 32
oled.fill(0)
#oled.pixel(screen_x, screen_y, 1)
oled.ellipse(screen_x, screen_y, 2, 2, 1, True)
oled.show()

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(17,Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
   
    # Adjust pixel x coordinate based on joystick deflection
    if (xValue < 300):
        screen_x -= 6
    elif (xValue < 5000):
        screen_x -= 3
    elif (xValue < 20000):
        screen_x -= 1
    elif (xValue > 60000):
        screen_x += 6
    elif (xValue > 45000):
        screen_x += 3
    elif (xValue > 35000):
        screen_x += 1
   
    # Bounds check
    if (screen_x < 0):
        screen_x = 0
    elif (screen_x > 127):
        screen_x = 127
       
    # Adjust pixel y coordinate based on joystick deflection
    # Note: for display, positive change is down, negative is up
    if (yValue < 300):
        screen_y += 6
    elif (yValue < 5000):
        screen_y += 3
    elif (yValue < 20000):
        screen_y += 1
    elif (yValue > 60000):
        screen_y -= 6
    elif (yValue > 45000):
        screen_y -= 3
    elif (yValue > 35000):
        screen_y -= 1

    # Bounds check
    if (screen_y < 0):
        screen_y = 0
    elif (screen_y > 63):
        screen_y = 63

    # Display updated pixel
    oled.fill(0)
    #oled.pixel(screen_x, screen_y, 1)
    oled.ellipse(screen_x, screen_y, 2, 2, 1, True)
    oled.show()

    #print("X: " + xStatus + ", Y: " + yStatus + "  button status: " + buttonStatus)
    utime.sleep(0.1)