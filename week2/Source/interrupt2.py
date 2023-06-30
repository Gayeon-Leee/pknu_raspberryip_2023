import RPi.GPIO as GPIO
import time

button = 6; red = 22; blue = 27;
count = 0;

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, GPIO.HIGH)
GPIO.output(blue, GPIO.HIGH)

def callbackfunc(channel):
	global count
	count = count + 1
	GPIO.output(red, GPIO.LOW)
	GPIO.output(blue, GPIO.HIGH)
	time.sleep(3)
	GPIO.output(red, GPIO.HIGH)
	GPIO.output(blue, GPIO.LOW)
	time.sleep(3)
	GPIO.output(red, GPIO.HIGH)
	GPIO.output(blue, GPIO.HIGH)
	print(f'Interrupt! {count}')

GPIO.add_event_detect(button, GPIO.RISING, callback=callbackfunc)

try:
	while True:
		print(":):")
		time.sleep(2)
except KeyboardInterrupt:
	GPIO.cleanup()
