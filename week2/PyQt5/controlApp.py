from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import RPi.GPIO as GPIO
import time
from threading import Thread

ledPin = 12
buzzPin = 15
tigPin = 23; echoPin = 24;

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzPin, GPIO.OUT)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

melody = [261, 293, 329, 349, 392, 440, 493, 523]
buzz = GPIO.PWM(buzzPin, 440)

class WindowClass(QMainWindow) :
	def __init__(self):
		super().__init__()
		uic.loadUi("control.ui", self)

		self.btnled_On.clicked.connect(self.btnledOn_clicked)
		self.btnled_Off.clicked.connect(self.btnledOff_clicked)
		self.btnbuzz1.clicked.connect(self.btnbuzzOn_clicked)
		self.btnbuzz2.clicked.connect(self.btnbuzzOff_clicked)

		self.buzzer_thread = None
	
	def btnledOn_clicked(self):
		GPIO.output(ledPin, GPIO.LOW)
		print("btnled_ON Clicked!")

	def btnledOff_clicked(self):
		GPIO.output(ledPin, GPIO.HIGH)
		print("btnled_Off Clicked!")

	def btnbuzzOn_clicked(self):
		print("btnbuzz_ON Clicked!")
		self.buzzer_thread = Thread(target=self.buzzer_on)
		self.buzzer_thread.start()	
		#btnbuzzOn_clidked 함수 진행 중에 off 함수 진행하면 부저 중지하기 위해 스레드 사용

	def btnbuzzOff_clicked(self):
		buzz.stop()
		print("btnbuzz_Off Clicked!")

	def buzzer_on(self):
		buzz.start(50)
		for i in range(len(melody)):
			buzz.ChangeFrequency(melody[i])
			time.sleep(0.5)
		buzz.stop()
			
if __name__ == "__main__":
	app = QApplication(sys.argv)
	mywindow = WindowClass()
	mywindow.show()
	sys.exit(app.exec_())

