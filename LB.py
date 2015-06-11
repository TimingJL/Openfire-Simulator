#!/usr/bin/env python
#coding=utf-8
import pika
import scheduler

credentials = pika.PlainCredentials('timing','ttsailab')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='104.236.113.133',port = 5672, virtual_host = 'timing', credentials = credentials))
channel = connection.channel()

#cm_list = ['cm_01','cm_02','cm_03']
cm_list = ['cm_01']
for i in range(len(cm_list)):
	channel.exchange_declare(exchange=cm_list[i], type='direct')
	channel.queue_declare(queue=cm_list[i], durable=True)
	channel.queue_bind(exchange=cm_list[i],
                      queue=cm_list[i])

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    #print " [x] Received %r" % (body,)
    #scheduler.mRR(body, cm_list)
    scheduler.mRandom(body, cm_list)


channel.basic_consume(callback,
                      queue='LBQ',
                      no_ack=True)

channel.start_consuming()