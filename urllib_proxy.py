# -*- coding:utf-8 -*-
from urllib import request as urllib2

# 代理开关
proxySwitch = True
# 构建handeler处理器对象 参数是代理IP和端口号
httpProxy_handeler = urllib2.ProxyHandler({'http': '182.110.13.243:808'})
#
nonProxy_handeler = urllib2.ProxyHandler({})

if proxySwitch:
    opener = urllib2.build_opener(httpProxy_handeler)
else:
    opener = urllib2.build_opener(nonProxy_handeler)

# 构建一个全局的opener
urllib2.install_opener(opener)
headers = {
    'Host': 'blog.csdn.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Referer': 'https://www.baidu.com/link?url=suCOqTBE0tA9cOasmGs7Zakllh9BlrF8DZ2zCaaHAzh63rWSdjMqCE_hSxyDlhKf2OUHcbg1pOMG-lZ8PbrGrIA3THUxlAi1t5Bd1iLXYEm&wd=&eqid=d255ce510002b0ad000000035a6719d9',
}
url = r'http://blog.csdn.net/wangbowj123/article/details/79133708'
request = urllib2.Request(url=url, headers=headers)
response = urllib2.urlopen(request)

print(response.read().decode())