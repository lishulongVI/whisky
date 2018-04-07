# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/7 下午11:11
"""
import sys
from rbtmq.rabbitmq_client import channel

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 2 else 'info'
severity = ['black', 'white', 'yellow']
message = ' '.join(sys.argv[2:]) or 'Hello World!'
for i in severity:
    channel.basic_publish(exchange='direct_logs',
                          routing_key=i,
                          body=message)
print(" [x] Sent %r:%r" % (severity, message))
