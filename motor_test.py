import time
import math
import sys
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

def pwm(v1,v2):
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
			GPIO.output(32,0)
			GPIO.output(36,1)
			GPIO.output(38,0)
			GPIO.output(40,1)
		else:
			if v2 != 0:
				GPIO.output(32,1)
				GPIO.output(36,0)
				GPIO.output(38,1)
				GPIO.output(40,0)
		if math.fabs(v1) <= math.fabs(v2):
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
			time.sleep(0.05*math.fabs(v2))
			GPIO.output(32,0)
			GPIO.output(36,0)
			GPIO.output(38,0)
			GPIO.output(40,0)
			time.sleep(0.05*math.fabs(math.fabs(v1) - math.fabs(v2)))
			GPIO.output(29,0)
			GPIO.output(31,0)
			GPIO.output(33,0)
			GPIO.output(35,0)
			time.sleep(0.05 - 0.05*math.fabs(v1))

fl = open('flag.txt','w')
fl.write('yes')
fl.close()

for i in range(10000):
	fl = open('flag.txt','r')
	input_flag = fl.readlines()
	fl.close()
	flag = ','.join(input_flag)
	if flag == 'stop':
		GPIO.cleanup()
		sys.exit()
	if flag == 'yes':
		f = open('share.txt','r')
		input_raw1 = f.readlines()
		f.close()
		up = ','.join(input_raw1[0:1])
		yoko = ','.join(input_raw1[1:2])
	#if input == 'stop':
	#	break
	#up_point = input.find('up')
	#koron_point = input.find(':')
	#yoko_point = input.find('yoko')
	#up = input[up_point+2:koron_point]
	#yoko = input[yoko_point+4:len(input)-yoko_point+4]
	pwm(float(up),float(yoko))

GPIO.cleanup()
