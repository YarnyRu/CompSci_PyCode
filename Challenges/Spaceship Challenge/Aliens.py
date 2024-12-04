import random
from time import sleep
aliens = False
while True:
    aliens = random.choice([True, False])
    if aliens:
        print("Beware aliens!")
    else:
        print("All quiet on the alien front")
    sleep(2)