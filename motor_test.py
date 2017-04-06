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

input_list = [1,2,3,4]
wheel_r = #hankei

def move(x,y):
		#フォトインタラプタ：タイヤ29,31→1;33,35→2;32,36→3;38,40→4とする（仮）
		photo = [GPIO.input(1),	GPIO.input(2),	GPIO.input(3),	GPIO.input(4)]
		rotate = [0,0,0,0]
		end_flag = 0
		if x > 0:
			GPIO.output(29,1)
			GPIO.output(31,0)
			GPIO.output(33,1)
			GPIO.output(35,0)
		else:
			if x != 0:
				GPIO.output(29,0)
				GPIO.output(31,1)
				GPIO.output(33,0)
				GPIO.output(35,1)
		if y > 0:
			GPIO.output(32,0)
			GPIO.output(36,1)
			GPIO.output(38,0)
			GPIO.output(40,1)
		else:
			if y != 0:
				GPIO.output(32,1)
				GPIO.output(36,0)
				GPIO.output(38,1)
				GPIO.output(40,0)
		while end_flag != 3:
			for i in range(4):
				if photo[i] != GPIO.input(input_list[i]):
					photo[i] = (photo[i]+1)%2
					rotate[i] += 1
			if rotate[0]*4*3.141592*wheel_r < abs(x) and (end_flag & 1) == 0:
				if rotate[0] - rotate[1] > 2:
					GPIO.output(29,0)
					GPIO.output(31,0)
				else:
					if x > 0:
						GPIO.output(29,1)
						GPIO.output(31,0)
					else:
						GPIO.output(29,0)
						GPIO.output(31,1)
				elif rotate[1] - rotate[0] > 2:
					GPIO.output(33,0)
					GPIO.output(35,0)
				else:
					if x > 0:
						GPIO.output(33,1)
						GPIO.output(35,0)
					else:
						GPIO.output(33,0)
						GPIO.output(35,1)
			else:
				GPIO.output(29,1)
				GPIO.output(31,1)
				GPIO.output(33,1)
				GPIO.output(35,1)
				end_flag += 1
			if rotate[2]*4*3.141592*wheel_r < abs(y) and (end_flag & 2) == 0:
				if rotate[3] - rotate[4] > 2:
					GPIO.output(32,0)
					GPIO.output(36,0)
				else:
					if y > 0:
						GPIO.output(32,1)
						GPIO.output(36,0)
					else:
						GPIO.output(32,0)
						GPIO.output(36,1)
				elif rotate[4] - rotate[3] > 2:
					GPIO.output(38,0)
					GPIO.output(40,0)
				else:
					if y > 0:
						GPIO.output(38,1)
						GPIO.output(40,0)
					else:
						GPIO.output(38,0)
						GPIO.output(40,1)
			else:
				GPIO.output(32,1)
				GPIO.output(36,1)
				GPIO.output(38,1)
				GPIO.output(40,1)
				end_flag += 2
			
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
	move(float(up),float(yoko))

GPIO.cleanup()
