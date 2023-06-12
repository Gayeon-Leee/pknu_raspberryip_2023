# LED 깜빡이기
import RPi.GPIO as GPIO
import time

signal_pin = 18

#GPIO.setmode(GPIO.BOARD) # pin map에서 1~40 쓰는거
GPIO.setmode(GPIO.BCM) #pin map에서 GPIO 18, GROUND 등
GPIO.setup(signal_pin, GPIO.OUT) #GPIO18핀에 출력 설정

while (True):
    GPIO.output(signal_pin, True) #GPIO18핀에 전압 시그널 ON
    time.sleep(0.1) #2초동안 불 킴
    GPIO.output(signal_pin, False) #GPIO18핀 전압 시그널 OFF
    time.sleep(0.1) #1초동안 불 끈 상태로 대기