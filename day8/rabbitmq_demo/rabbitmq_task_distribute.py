# -*- coding:utf-8 -*-
__auth__ = 'christian'

import sys
import pika, time

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))

