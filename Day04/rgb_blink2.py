#LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17; green = 27; blue = 22 # ground 역살

# 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True)

try:
    while True:
        GPIO.output(red, False) # RED ON
        GPIO.output(green, True)
        GPIO.output(blue, True) # BLUE ON => 이렇게 동시에 키면 색 섞여서 나옴!
        time.sleep(1)
        GPIO.output(red, True)
        GPIO.output(green, False)   # GREEN ON
        GPIO.output(blue, True)
        time.sleep(1)
        GPIO.output(red, True)
        GPIO.output(green, True)
        GPIO.output(blue, False)    # BLUE ON
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.output(red, True)
    GPIO.output(green, True)
    GPIO.output(blue, True)
    GPIO.cleanup()