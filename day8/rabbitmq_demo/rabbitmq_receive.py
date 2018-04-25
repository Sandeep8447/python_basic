# -*- coding:utf-8 -*-
__auth__ = 'christian'

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print "[x] Received %r" % body

channel.basic_consume(
    callback,
    queue='hello',
    no_ack=True
)

print "[*] Waiting for messages. To exit press CTRL+C"

channel.start_consuming()


#  The average distribution.
#  if we send the 'hello world!' messages three times, and run rabbitmq_receive.py as three different client,
#  the we will find that each of three clients received a message.
#