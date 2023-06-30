import RPi.GPIO as GPIO
import time

swPin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def callbackfunc(channel): # callback 함수
	#if GPIO.input(swPin) == GPIO.HIGH:
	print("Interrupt!")

GPIO.add_event_detect(swPin, GPIO.RISING, callback=callbackfunc) #callback='호출할 함수' 로 callback 실행하는거

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()
