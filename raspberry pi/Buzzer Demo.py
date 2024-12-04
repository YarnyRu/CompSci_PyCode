from gpiozero import Buzzer
buzzer = Buzzer(17)

## Turn on the buzzer
buzzer.on()
## Turn off the buzzer
buzzer.off()
## Beep the buzzer (on and off for 1 second)
buzzer.beep()
## Beep the buzzer on and off for 0.1 seconds 10 times
buzzer.beep(0.1, 0.1, 10)

#Alternative to using buzzer, playing a sound
import pygame
pygame.init()
my_sound = pygame.mixer.Sound('path/to/my/soundfile.wav')
my_sound.play()
#download sounds from https://soundbible.com/royalty-free-sounds-1.html

#for the laser beam pointer
from gpiozero import LightSensor
ldr = LightSensor(pin number)
ldr.when_dark = lambda: print("INTRUDER!")

  #then all that remains is to connect the laser pointer into a drinking straw and line it up with the LDR
  #so that only light from there will affect it
  