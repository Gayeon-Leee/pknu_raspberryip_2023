import RPi.GPIO as GPIO
import time

pin = 13
melody = [261, 293, 329, 349, 392, 440, 493, 523]
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

buzz = GPIO.PWM(pin, 440)

try:
	buzz.start(50)
	key = int(input('키 입력 : 1 ~ 9'))
	buzz.ChangeFrequency(melody[key])
	buzz.stop()
	
except KeyboardInterrupt:
	GPIO.cleanup()

