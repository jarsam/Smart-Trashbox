import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
x = 0
while x < 100:
	GPIO.output(3,True)
	GPIO.output(5,0)
	GPIO.output(8,1)
	time.sleep(0.0005*x)
	GPIO.output(3,False)
	GPIO.output(5,False)
	GPIO.output(8,False)
	time.sleep(0.05 - 0.0005*x)
	x += 1
while x > 0:
	GPIO.output(3,1)
	GPIO.output(8,1)
	time.sleep(0.0005*x)
	GPIO.output(3,0)
	GPIO.output(8,0)
	time.sleep(0.05 - 0.0005*x)
	x -= 1
GPIO.cleanup()
