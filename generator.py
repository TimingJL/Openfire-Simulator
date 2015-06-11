#coding=utf-8
import pika
import time
import sys

import math
import random
import time

#Generate Random Timings for a Poisson Process
#http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/
def nextTime(rateParameter):
    return -math.log(1.0 - random.random()) / rateParameter

#to establish a connection with RabbitMQ server
credentials = pika.PlainCredentials('timing','ttsailab')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='104.236.113.133',port = 5672, virtual_host = 'timing', credentials = credentials))
channel = connection.channel()

#task generator
while True:
    t = nextTime(1/4.0)
    time.sleep(t)


    channel.basic_publish(exchange='LB',
                      routing_key='',
                      body=str(t))
    print t