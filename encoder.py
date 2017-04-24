import time
import math
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(37,GPIO.IN)

for i in range(10000):
  if GPIO.input(37) == 1
    GPIO.putput(38,1)
  else
    GPIO.output(37,0)
	
GPIO.cleanup()
