import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 23; echo = 24
buzzPin = 21

print("감지 센서")

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(buzzPin, GPIO.OUT)
buzz = GPIO.PWM(buzzPin, 440)

GPIO.output(trig, False)
print("출력 초기화")
time.sleep(2)

buzz.start(50)

try:
	while True: 
		GPIO.output(trig, True)
		time.sleep(0.00001)
		GPIO.output(trig, False)

		while GPIO.input(echo) == 0:
			start = time.time()

		while GPIO.input(echo) == 1:
			stop = time.time()

		check_time = stop - start
		distance = check_time * 34300 / 2
		print("Distance : %.1f cm" %distance)

		if distance < 10 :
#			buzz.start(50)
			time.sleep(0.5)
			buzz.ChangeFrequency(440)
			print("Warning!")

		else :
			buzz.ChangeFrequency(0.1)
#		buzz.stop()
except KeyboardInterrupt:
	print("거리 측정 종료")
	GPIO.cleanup()


