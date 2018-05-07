# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/6 上午11:34

@TODO : pyinstaller -F -w -i manage.icoi little_net.py

"""

from urllib import request
from pyquery import PyQuery as pq
import base64
from threading import Thread
from queue import Queue
import ssl
import copy
import time

from multiprocessing.pool import ThreadPool

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'
}

#
url = base64.b64decode('aHR0cDovL3d3dy4wODYwMDIuY29tLw==').decode('utf-8')
cloud_url = base64.b64decode('aHR0cDovL3lpaGFvcXVuenUuY29tLw==').decode('utf-8')
share_url = base64.b64decode('aHR0cHM6Ly93d3cuYmRxdW56dS5jb20v').decode('utf-8')

result1 = list()
result2 = list()
result3 = list()

req_queue = Queue()


def get_content(url):
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(url=req)
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
        result1.append(a[1:] if a.find('享') >= 0 else a)


def __multi(i):
    a = i('a').attr('href')
    if a is not None:
        req = request.Request(url=a, headers=headers)
        res = request.urlopen(req)
        if res.status == 200:
            d = pq(res.read().decode('utf-8'))('.topic-view')
            result2.append(d('a').attr('href'))


def resolve_cloud(content):
    df = pq(content)
    blocks = df('.title')
    for i in blocks.items():
        a = Thread(target=__multi, args=(i,))
        a.start()
        req_queue.put(a)
    while req_queue.qsize() > 0:
        a = req_queue.get()
        a.join()


def resolve_share(content):
    df = pq(content)
    blocks = df('tr')
    for i in blocks.items():
        a = i('span').text().split(' ')[1]
        result3.append(a)


def top_N(result, N=100):
    for i, v in enumerate(result):
        if i < N:
            print(v)
        else:
            break


pool = ThreadPool(3)


def rewrite():
    # resolve_cloud(get_content(url=cloud_url))
    # resolve_little(get_content(url=url))
    #
    # resolve_share(get_content(url=share_url))

    pool.map(resolve_cloud, [get_content(url=cloud_url)])
    pool.map(resolve_little, [get_content(url=url)])
    pool.map(resolve_share, [get_content(url=share_url)])


if __name__ == '__main__':
    # Thread(target=resolve_little, args=(get_content(url=url),)).start()
    # Thread(target=resolve_cloud, args=(get_content(url=cloud_url),)).start()
    # Thread(target=resolve_share, args=(get_content(url=share_url),)).start()

    while True:
        print('解析第一渠道，请稍等.....')
        rewrite()
        res1 = copy.deepcopy(result1)
        res2 = copy.deepcopy(result2)
        res3 = copy.deepcopy(result3)
        res1.extend(res2)
        res1.extend(res3)
        time.sleep(2)
        print('解析第二渠道，请稍等.....')
        rewrite()
        result1.extend(result3)
        result1.extend(result2)
        retD = list(set(result1).difference(set(res1)))

        print('*' * 10 + '解析出可用链接长度：{}'.format(len(retD)))
        top_N(retD, 5)
        print('*' * 10 + '解析出可能失效链接长度：{}'.format(len(result1)))
        top_N(result1, 5)

        result1 = list()
        result2 = list()
        result3 = list()







#
