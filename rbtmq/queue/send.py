# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/7 下午9:36
"""
import sys
from rbtmq.rabbitmq_client import channel

message = ' '.join(sys.argv[1:]) or "Hello World! i feel never could be happy again"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(" [x] Sent %r" % message)
