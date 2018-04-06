# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/5 下午8:41
"""
from pyquery import PyQuery as pq
from urllib import request
import re
import os

base_path = os.path.dirname(__file__)

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'
}

url = 'https://re.taobao.com/search?spm=a231k.8165028.0782702702.203.63732e63wGLcj1&prepvid=300_10.177.76.199_119596_1522932011677&extra=&keyword=%E8%BF%9E%E8%A1%A3%E8%A3%992018%20%20%E9%95%BF&frontcatid=&isinner=1&refpid=420435_1006&page={}&rewriteKeyword&_input_charset=utf-8'


def crawler(page):
    req = request.Request(url=url.format(page), headers=headers)

    res = request.urlopen(req)
    if res.status == 200:
        result = res.read().decode('utf-8')
        __resolve_page(content=result)
    else:
        return None


def __resolve_page(content):
    __crawl_pic_list(content)


def __crawl_pic_list(content):
    """
    提取照片并保存
    :param content:
    :return:
    """
    d = pq(content)
    item = d('#searchResult')('.item')
    for i in item.items():
        file_name = i('.title').attr('title').replace('/', '')
        print(file_name)
        file_path = i('img').attr('data-ks-lazyload').replace('260', '560')
        file_p = base_path + '/pic/' + file_name + '.jpg'
        with open(file_p, 'wb') as file:
            res = request.urlopen(file_path)
            file.write(res.read())


if __name__ == '__main__':
    # crawler(1)
    # crawler(2)
    # crawler(3)
    # crawler(4)

    from threading import Thread

    for i in range(5, 100):
        Thread(target=crawler, args=(i,)).start()
