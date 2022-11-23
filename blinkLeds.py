import machine
import neopixel
import time

#Blink all LEDs
#Define number of pixels, create an object to set colours / brightnesses and store blinkDelay in a variable (in seconds)
numPixels = 8
np = neopixel.NeoPixel(machine.Pin(1), numPixels)
blinkDelay = 1
#Run forever
while True:
    #Loop for each LED and set to full brightness in red
    for i in range(0,numPixels):
        np[i] = (254,0,0)
    #Wait for a short period of time and then set the LEDs to on
    time.sleep(blinkDelay)
    np.write()
    #Loop for each LED and set to off
    for i in range(0,numPixels):
        np[i] = (0,0,0)
    #Write values to LEDs
    time.sleep(blinkDelay)
    np.write()