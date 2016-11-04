import time
from neopixel import *


# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 8     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# Define functions which animate LEDs in various ways.
def color(strip, color):
	if color == "red":
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(255,0,0))
			strip.show()
	elif color == "green":
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(0,255,0))
			strip.show()
	elif color == "blue":
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(0,0,255))
			strip.show()
	else:
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, color)
			strip.show()
			
def chaser(strip):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(255,0,0))
		strip.show()
		time.sleep(0.01)
		strip.setPixelColor(i, Color(0,0,0))
		strip.show()
		time.sleep(0.01)
		


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()
try:
	print ('Press Ctrl-C to quit.')
	for i in range(3):
		chaser(strip)
	for i in range(3):
		color(strip, Color(255, 0, 0))  # Green
		time.sleep(0.3)
		color(strip, Color(0, 255, 0))  # Red
		time.sleep(0.3)
		color(strip, Color(0, 0, 255))  # Blue
		time.sleep(0.3)
	color(strip, Color(0,0,0))
except KeyboardInterrupt:
	print("Exit")
	color(strip, Color(0,0,0))
	
