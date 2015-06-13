#!/usr/bin/env python
import pika
import time
import thread
#from threading import Time
import numpy as np
from collections import deque
from threading import Thread
import parameter

credentials = pika.PlainCredentials(parameter.username, parameter.password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=parameter.host,port = 5672, virtual_host = parameter.vhost, credentials = credentials))
channel = connection.channel()

queue_name = 'cm_01'
msg_queue = deque([])

channel.queue_declare(queue=queue_name, durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'


def out():
    #numpy.random.pareto
    #http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.pareto.html
    a, m = 10., 1. # shape and mode
    while True:        
        s = np.random.pareto(a, 1) + m
        time.sleep(s)
        if msg_queue:
            msg_queue.popleft()
            print '\n pop' + str(s)
            print msg_queue


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    msg_queue.append(body)
    print '\n in queue'
    print msg_queue
    ch.basic_ack(delivery_tag = method.delivery_tag)
    #thread.start_new_thread(Threadfun, (msg_queue, 2, lock))

th = Thread(target=out)
th.start()

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=queue_name)
channel.start_consuming()







