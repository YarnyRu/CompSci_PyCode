#Sense-HAT code
from sense_hat import SenseHat
from time import sleep
from random import randint
num = randint(0,10)
sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

sense.clear(black)
#sense.clear(white)
#while True:
#  sense.show_message("Let's get coding!", text_colour=yellow, back_colour=blue, scroll_speed=0.2)

#sense.show_letter("J", text_colour=red, back_colour=white)

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

sense.show_letter("L", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)
sense.show_letter("u", pick_random_colour())
sleep(1)
sense.show_letter("r", pick_random_colour())
sleep(1)
sense.show_letter("a", pick_random_colour())
sleep(1)


sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))
sleep(1)

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)

sleep(3)
sense.flip_v()
sleep(1)
sense.flip_v()
sleep(1)
sense.clear()
