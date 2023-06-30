import RPi.GPIO as GPIO
import time

buzzerPin = 21

melody = [261, 293, 329, 349, 392, 440, 493, 523]
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

buzz = GPIO.PWM(buzzerPin, 440) 	# 440Hz 갖는 객체 생성

try:
	while True:
		buzz.start(50)

		direction = input('키 입력 : [1|2|3|4|5|6|7|8] ')

		if direction == '1':
			buzz.ChangeFrequency(melody[0])
		elif direction == '2':
			buzz.ChangeFrequency(melody[1])
		elif direction == '3':
			buzz.ChangeFrequency(melody[2])
		elif direction == '4':
			buzz.ChangeFrequency(melody[3])
		elif direction == '5':
			buzz.ChangeFrequency(melody[4])
		elif direction == '6':
			buzz.ChangeFrequency(melody[5])
		elif direction == '7':
			buzz.ChangeFrequency(melody[6])
		elif direction == '8':
			buzz.ChangeFrequency(melody[7])
	buzz.stop() #pwm 종료
	time.sleep(1)
	
except KeyboardInterrupt:
	GPIO.cleanup()
