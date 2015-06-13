#!/usr/bin/env python
from threading import Thread
import time

def add(x, y):
	a, m = 10., 1. # shape and mode
	while True:
        #time.sleep(1)
		print 'add : %s + %s = %s' % (x, y, x + y)

def add2(x, y):
	while True:
		#time.sleep(2)
		print 'add2 : %s + %s = %s' % (x, y, x + y)


th = Thread(target=add, args=(1, 2))
th2 = Thread(target=add2, args=(1, 2))
th.start()
th2.start()
