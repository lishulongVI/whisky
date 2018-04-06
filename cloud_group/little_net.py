# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/6 上午11:34
"""

from urllib import request
from pyquery import PyQuery as pq
import base64
from threading import Thread

#
url = base64.b64decode('aHR0cDovL3d3dy4wODYwMDIuY29tLw==').decode('utf-8')
cloud_url = base64.b64decode('aHR0cDovL3lpaGFvcXVuenUuY29tLw==').decode('utf-8')
share_url = base64.b64decode('aHR0cHM6Ly93d3cuYmRxdW56dS5jb20v').decode('utf-8')


def get_content(url):
    res = request.urlopen(url=url)
    if res.status == 200:
        content = res.read().decode('utf-8')
        return content
    else:
        return None


def resolve_little(content):
    df = pq(content)
    blocks = df('.block')
    for i in blocks.items():
        a = i('a').attr('href')
        print(a[1:] if a.find('享') >= 0 else a)


def resolve_cloud(content):
    df = pq(content)
    blocks = df('.title')
    for i in blocks.items():
        a = i('a').attr('href')
        if a is not None:
            res = request.urlopen(a)
            if res.status == 200:
                d = pq(res.read().decode('utf-8'))('.topic-view')
                print(d('a').attr('href'))


def resolve_share(content):
    df = pq(content)
    blocks = df('tr')
    for i in blocks.items():
        a = i('span').text().split(' ')[2]
        print(a)


if __name__ == '__main__':
    Thread(target=resolve_little, args=(get_content(url=url),)).start()
    Thread(target=resolve_cloud, args=(get_content(url=cloud_url),)).start()
    Thread(target=resolve_share, args=(get_content(url=share_url),)).start()
    # resolve_little()
    # resolve_cloud(get_content(url=cloud_url))
    # resolve_share(get_content(url=share_url))
