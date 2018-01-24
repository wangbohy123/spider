# -*- coding:utf-8 -*-
from urllib import request as urllib2
from urllib import parse

url = r'http://www.renren.com/963438127/profile'
headers = {
	'Host':'zhibo.renren.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
	'Cookie':'anonymid=jcq5vjyv-gtxo0h; depovince=GW; jebecookies=263472cd-2cc9-4d29-a69b-f88ddedb853c|||||; _r01_=1; ick_login=4c9235dd-0d51-4cdc-9cf7-7a95996ff1cd; t=43acd6b2e5a187f49df8046146479ea97; societyguester=43acd6b2e5a187f49df8046146479ea97; id=963438127; xnsid=e240e3f6',
	'Connection':'keep-alive',
	'Upgrade-Insecure-Requests':'1',
}

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
print(response.read().decode())

