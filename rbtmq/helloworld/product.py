# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/7 下午8:44
"""
from rbtmq.rabbitmq_client import channel

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='i hare him , i hate him, i feel never could be happy again')
print(" [x] Sent 'Hello World!'")
