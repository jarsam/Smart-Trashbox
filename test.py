import time
import math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

def pmw(v1,v2):
		if v1 > 0:
			GPIO.output(29,1)
			GPIO.output(31,0)
			GPIO.output(33,1)
			GPIO.output(35,0)
		else:
			if v1 != 0:
				GPIO.output(29,0)
				GPIO.output(31,1)
				GPIO.output(33,0)
				GPIO.output(35,1)
		if v2 > 0:
			GPIO.output(32,1)
			GPIO.output(36,0)
			GPIO.output(38,1)
			GPIO.output(40,0)
		else:
			if v2 != 0:
				GPIO.output(32,0)
				GPIO.output(36,1)
				GPIO.output(38,0)
				GPIO.output(40,1)
		if v1 <= v2:
			time.sleep(0.05*math.fabs(v1))
			GPIO.output(29,0)
			GPIO.output(31,0)
			GPIO.output(33,0)
			GPIO.output(35,0)
			time.sleep(0.05*math.fabs(math.fabs(v2) - math.fabs(v1)))
			GPIO.output(32,0)
			GPIO.output(36,0)
			GPIO.output(38,0)
			GPIO.output(40,0)
			time.sleep(0.05 - 0.05*math.fabs(v2))
		else:
			#time.sleep(0.05*math.fabs(v2))
			GPIO.output(32,0)
			GPIO.output(36,0)
			GPIO.output(38,0)
			GPIO.output(40,0)
			time.sleep(0.05*v1)
			GPIO.output(29,0)
			GPIO.output(31,0)
			GPIO.output(33,0)
			GPIO.output(35,0)
			time.sleep(0.05 - 0.05*v1)

for i in range(50):
	#input = raw_input()
	#if input == 'stop':
	#	break
	#up_point = input.find('up')
	#koron_point = input.find(':')
	#yoko_point = ipput.find('yoko')
	#up = float(input[up_point+2,koron_point])
	#yoko = float(input[koron_point+1,len(input)])
	GPIO.output(29,1)
	GPIO.output(31,0)
	GPIO.output(33,1)
	GPIO.output(35,0)
GPIO.output(29,0)
GPIO.output(31,0)
GPIO.output(33,0)
GPIO.output(35,0)

GPIO.cleanup()
