#coding=utf-8
#!/usr/bin/env python
import pika
import sys
import random
import parameter

credentials = pika.PlainCredentials(parameter.username, parameter.password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=parameter.host,port = 5672, virtual_host = parameter.vhost, credentials = credentials))
channel = connection.channel()

def mRR(task, cm_list):
    #print " [x] Received %r" % (task,)
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=task,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
    #print " [x] Sent %r" % (message,)


def mRandom(task, cm_list):
	#print cm_list
	#print cm_list[0]
	#print len(cm_list)
	#print random.randint(0,len(cm_list)-1)

	r = random.randint(0,len(cm_list)-1)
	
	channel.basic_publish(exchange=cm_list[r],
                  routing_key=cm_list[r],
                  body=task,
                  properties=pika.BasicProperties(
                     delivery_mode = 2, # make message persistent
                  ))