# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/7 下午9:27
"""
import pika

from pika import PlainCredentials

__config_mq = {
    'host': '192.168.91.129',
    'port': 5672,
    'virtual_host': '/vhost',
    'credentials': PlainCredentials(username='mojito', password='mojito'),
}

connect = pika.BlockingConnection(pika.ConnectionParameters(**__config_mq))

channel = connect.channel()
