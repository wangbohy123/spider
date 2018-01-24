# -*- coding:utf-8 -*-
from urllib import request as urllib2
from urllib import parse
import threading
import time
import random

def spyder():
    # 构建一个request请求
    url = r'http://blog.csdn.net/wangbowj123/article/details/79133708'
    ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    ]
    header = random.choice(ua_list)
    headers = {
        'Host': 'blog.csdn.net',
        'User-Agent': header,
        'Referer': 'https://www.baidu.com/link?url=suCOqTBE0tA9cOasmGs7Zakllh9BlrF8DZ2zCaaHAzh63rWSdjMqCE_hSxyDlhKf2OUHcbg1pOMG-lZ8PbrGrIA3THUxlAi1t5Bd1iLXYEm&wd=&eqid=d255ce510002b0ad000000035a6719d9',
    }
    dic = {
        'articleId':'79133708',
        'pageindex':'2',
    }
    # 使用代理服务器
    # http_proxyHandeler = urllib2.ProxyHandler({'http': '61.135.217.7:80'})
    # opener = urllib2.build_opener(http_proxyHandeler)
    # urllib2.install_opener(opener)
    # data = parse.urlencode(dic).encode('utf-8')
    request = urllib2.Request(url=url, headers=headers)
    response = urllib2.urlopen(request)
    # print(response.read().decode())
    print(response.getcode())
    #print(response.read().decode())
    t = random.randint(20,30)
    print('休息{}秒'.format(t))
    time.sleep(t)


if __name__ == '__main__':
    theads = []
    for i in range(20):
        t = threading.Thread(target=spyder)
        theads.append(t)
    for t in theads:
        t.setDaemon(True)
        t.start()
        t.join()

