import time
from neopixel import *
from Tkinter import *

LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 8     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

def color(strip, color):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()	
		
def show_values(value):
    print (red.get(), green.get(), blue.get())
    color(strip, Color(green.get(),red.get(),blue.get()))

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
try:
	print ('Welcome to the ColorMixer Tool, press CTRL + C to exit from the terminal.')
	for i in range(3):
		color(strip, Color(255, 0, 0))  # Green
		time.sleep(0.3)
		color(strip, Color(0, 255, 0))  # Red
		time.sleep(0.3)
		color(strip, Color(0, 0, 255))  # Blue
		time.sleep(0.3)
	color(strip, Color(0,0,0))
	master = Tk()
	red = Scale(master, from_=0, to=255, orient=HORIZONTAL, label= "Red", command=show_values, length= 300)
	red.pack()
	green = Scale(master, from_=0, to=255, orient=HORIZONTAL, label= "Green", command=show_values, length= 300)
	green.pack()
	blue = Scale(master, from_=0, to=255, orient=HORIZONTAL, label= "Blue", command=show_values, length= 300)
	blue.pack()
	mainloop()
except KeyboardInterrupt:
	print("Exit")
	color(strip, Color(0,0,0))
	
