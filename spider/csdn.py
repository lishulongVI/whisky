# -*- coding: utf-8 -*-
"""
@contact: lishulong.never@gmail.com
@time: 2018/4/5 上午9:40
"""
from urllib import request
# 博客园
url = "https://www.cnblogs.com/"
url = "https://my.csdn.net/"
url = "https://blog.csdn.net"
#
handlers = ("User-Agent",
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36")

op = request.build_opener()
op.add_handlers = [handlers]
request.install_opener(op)

res = request.urlopen(url=url)


print(res.read().decode('utf-8'))


# from spider.proxy.user_proxy import use_proxy
#
#
# print(use_proxy(url))