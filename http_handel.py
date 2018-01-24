# -*- coding:utf-8 -*-
from urllib import request as urllib2
import urllib

# 构建一个http handeler处理器对象 支持处理HTTP请求
http_handeler = urllib2.HTTPHandler()

# 调用build_opener方法构造一个自定义opener对象 参数是构建的处理器对象
opener = urllib2.build_opener(http_handeler)

request = urllib2.Request('https://tieba.baidu.com/index.html')

response = opener.open(request)

print(response.read().decode('utf-8'))
