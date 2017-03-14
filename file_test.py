import sys
import time

for i in range(0,60):
	f = open('share.txt','r')
	for row in f:
		print row
	f.close()
	time.sleep(1)

