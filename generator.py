#coding=utf-8
import pika
import time
import sys

import math
import random
import time
import parameter

#Generate Random Timings for a Poisson Process
#http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/
def nextTime(rateParameter):
    return -math.log(1.0 - random.random()) / rateParameter

#to establish a connection with RabbitMQ server
credentials = pika.PlainCredentials(parameter.rabbitmq_username, parameter.rabbitmq_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=parameter.rabbitmq_host,port = 5672, virtual_host = parameter.rabbitmq_vhost, credentials = credentials))
channel = connection.channel()

#task generator
while True:
    t = nextTime(1/0.5)
    time.sleep(t)


    channel.basic_publish(exchange='LB',
                      routing_key='',
                      body=str(t))
    print t