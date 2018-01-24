# -*- coding:utf-8 -*-
import urllib.request as urllib2
# user_agent是爬虫与反爬虫斗争的第一步
ua_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}
# 通过Request()方法构造一个请求对象
url = r'https://www.baidu.com//'
request = urllib2.Request(url, headers = ua_headers)
print(request.headers,request.type,request.data)

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# 服务器返回的类文件对象支持python文件对象的操作方法
html = response.read()
# 返回状态码
code = response.getcode()
print(html.decode('gb2312'))
print(code)

# 返回实际url  防止重定向
print(response.geturl())

# 返回http响应的报头
print(response.info())
