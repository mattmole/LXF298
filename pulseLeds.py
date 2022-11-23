import machine
import neopixel
import time
    
#Pulse all LEDs
#Define number of pixels, create an object to set colours / brightnesses, store pulseTime in a variable (in seconds) and finally, the number of loop iterations (which controls the smoothness of the fade)
numPixels = 8
np = neopixel.NeoPixel(machine.Pin(1), numPixels)
pulseTime = 2
numLoops = 100
#Run forever
while True:
    #Now, for numLoops, iteratively set the brightness of each LED to a value that gets larger each time
    for a in range(1,numLoops):   
        #Update each LED
        for i in range(0,numPixels):
            np[i] = (int(a*254/numLoops),0,0)
        #Write the values to the LEDs
        np.write()
        #Wait for a short period of time before increasing the brightness
        time.sleep(pulseTime/(2*numLoops))
    #Now, for numLoops, iteratively set the brightness of each LED to a value that gets smaller each time
    for a in range(numLoops,1,-1): 
        #Update each LED  
        for i in range(0,numPixels):
            np[i] = (int(a*254/numLoops),0,0)
        #Write the values to the LEDs
        np.write()
        #Wait for a short period of time before increasing the brightness
        time.sleep(pulseTime/(2*numLoops))
