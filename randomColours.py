import machine
import neopixel
import random
import time

#Random chase of colours on each LED.
#Define number of pixels and then create an object to set colours / brightnesses
numPixels = 8
np = neopixel.NeoPixel(machine.Pin(1), numPixels)
#Loop the code forever
while True:
    #Set the colour at random for each pixel, sleep for a small amount of time and then update the LEDs
    for i in range(0,numPixels):
        np[i] = (random.randint(0,254),random.randint(0,254),random.randint(0,254))
        time.sleep(0.2)
        np.write()   