#!/usr/bin/env python
import pika
import time
import thread
#from threading import Time
import numpy as np
from collections import deque

credentials = pika.PlainCredentials('timing','ttsailab')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='104.236.113.133',port = 5672, virtual_host = 'timing', credentials = credentials))
channel = connection.channel()

queue_name = 'cm_01'
#msg_queue = deque([])
msg_queue = []
#a, m = 1., 1. # shape and mode
#task_list = []

channel.queue_declare(queue=queue_name, durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def out(msg_queue):
	#numpy.random.pareto
	#http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.pareto.html
	a, m = 1., 1. # shape and mode
	s = np.random.pareto(a, 1) + m
	time.sleep(s)
	if len(msg_queue)!=0:
		msg_queue.popleft()
    	print 'pop'
    	print msg_queue


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    #time.sleep( body.count('.') )
    #print " [x] Done"
    #task_list.append(body)
    msg_queue.append(body)
    #print task_list
    print 'in queue'
    print msg_queue
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name)
channel.start_consuming()

thread.start_new_thread(out,(msg_queue))