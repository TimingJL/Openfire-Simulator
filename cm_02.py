#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('timing','ttsailab')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='104.236.113.133',port = 5672, virtual_host = 'timing', credentials = credentials))
channel = connection.channel()

queue_name = 'cm_02'

channel.queue_declare(queue=queue_name, durable=True)
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    #time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue=queue_name)

channel.start_consuming()