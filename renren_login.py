# -*- coding:utf-8 -*-
from urllib import request as urllib2
from urllib import parse
from http import cookiejar

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}

# 通过cookiejar()类构建一个cookieJar对象，用来保存cookie的值
cookie = cookiejar.CookieJar()

# 通过HTTPCookieProcessor()对象构建一个处理器对象，用来处理cookie
# 参数是CookieJar对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

formData = {
    'email':'18839159573',
    'password':'wangbo123',
}
data = parse.urlencode(formData).encode('utf-8')
opener = urllib2.build_opener(cookie_handler)

url = r'http://www.renren.com/PLogin.do'

request = urllib2.Request(url=url,data=data ,headers=headers)

response = opener.open(request)

#print(response.read().decode())


response2 = opener.open('http://www.renren.com/963457938/profile')
print(response2.read().decode())