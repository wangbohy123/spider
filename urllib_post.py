# -*- coding:utf-8 -*-
from urllib import request as urllib2
from urllib import parse
url = r'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
key = 'hello'
headers = {
    'Host':'fanyi.youdao.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Referer':'http://fanyi.youdao.com/',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With':'XMLHttpRequest',
    'Connection':'keep-alive',
}
postData = {
    'i':key,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1516611906797',
    'sign':'9bc3470f0087106d71ee4ac904c271db',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'false',
}
data = parse.urlencode(postData).encode('utf-8')
request = urllib2.Request(url=url, data=data, headers=headers)
response = urllib2.urlopen(request)
print(response.read().decode('utf-8'))


