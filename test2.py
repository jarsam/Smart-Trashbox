import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

for i in range(1,5):
	for j in range(0,100):
		GPIO.output(5,1)
		GPIO.output(6,0)
		time.sleep(0.01 - 0.002*i)
		GPIO.output(5,0)
		GPIO.output(6,0)
		time.sleep(0.002*i)

GPIO.cleanup()
