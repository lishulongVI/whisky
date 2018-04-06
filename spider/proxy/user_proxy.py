# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/5 上午9:57
"""

from urllib import request
import re
import json

proxy_url = 'http://www.xicidaili.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
}


def __dict_proxys(li: list):
    gg = []
    length = len(li)
    for i in range(0, length, 6):
        di = {
            'ip': li[i],
            'port': li[i + 1],
            'address': li[i + 2],
            'protocol': li[i + 3],
            'expire': li[i + 4],
            'timestamp': li[i + 5],
        }
        gg.append(di)
    return gg


def get_proxy_info():
    with open('proxy_ip_info.csv', 'r') as f:
        c = f.readline()
        ips = json.loads(c)
        return ips

        # req = request.Request(url=proxy_url, headers=headers)
        # response = request.urlopen(req)
        # if response.status == 200:
        #     content = response.read().decode('utf-8')
        #     tds = re.findall(r'<td>(.*?)</td>', content, re.I | re.M)
        #     c = __dict_proxys(tds)
        #     with open('proxy_ip_info.csv', 'w') as f:
        #         f.write(json.dumps(c))
        #     return __dict_proxys(tds)
        # return None


def use_proxy(url):
    ip_info = get_proxy_info()[0]
    proxy_ip = {ip_info.get('protocol'): '{}:{}'.format(ip_info.get('ip'), ip_info.get('port'))}
    print(proxy_ip)
    proxy = request.ProxyHandler(proxy_ip)
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener=opener)
    response = request.urlopen(url=url)
    if response.status == 200:
        content = response.read().decode('utf-8')
        return content
    return None


if __name__ == '__main__':
    print(get_proxy_info())
    print(use_proxy('https://www.baidu.com'))
