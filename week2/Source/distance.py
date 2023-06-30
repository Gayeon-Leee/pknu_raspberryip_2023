import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig = 23
echo = 24
print("초음파 거리 측정기")

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, False)
print("초음파 출력 초기화")
time.sleep(2)

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
		print("Distnace : %.1f cm" %distance)
		time.sleep(0.4)

except KeyboardInterrupt:
	print("거리 측정 완료")
	GPIO.cleanup()
