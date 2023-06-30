import time
import RPi.GPIO as GPIO


#pins = { 'a': 17, 'b': 27, 'c': 22, 'd': 10, 'e': 9, 'f': 11, 'g': 0}
a = 17; b = 27; c = 22; d = 10; e = 9; f = 11; g = 8 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(a, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(c, GPIO.OUT)
GPIO.setup(d, GPIO.OUT)
GPIO.setup(e, GPIO.OUT)
GPIO.setup(f, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)

try:
	while(True):
		#GPIO.output(a, True)
		#GPIO.output(b, True)
		#GPIO.output(c, True)
		#GPIO.output(d, True)
		#GPIO.output(e, True)
		#GPIO.output(f, True)
		#GPIO.output(g, True)
		#time.sleep(0.2)
		#GPIO.output(a, False)
		#GPIO.output(b, False)
		#GPIO.output(c, False)
		#GPIO.output(d, False)
		#GPIO.output(e, False)
		#GPIO.output(f, False)
		#GPIO.output(g, False)
		#time.sleep(0.2)

		
except KeyboardInterrupt:
	GPIO.cleanup()


