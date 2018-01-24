# -*- coding:utf-8 -*-
from urllib import request as urllib2
import re
# 利用正则表达式爬取内涵段子
url = r'http://www.neihanpa.com/article/list_5_{}.html'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}
file_name = '内涵段子.txt'
for page in range(2):
    fullurl = url.format(str(page+1))
    request = urllib2.Request(url=fullurl, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('gbk')
    # re.S 如果没有re.S 则是只匹配一行有没有符合规则的字符串，如果没有则下一行重新匹配
    # 如果加上re.S 则是将所有的字符串作为一个整体进行匹配
    pattern = re.compile(r'<div\sclass="f18 mb20">(.*?)</div>',re.S)
    duanzis = pattern.findall(html)
    for duanzi in duanzis:
        duanzi = duanzi.replace('<p>','').replace('</p>','').replace('<br />','\n').replace('&ldquo;','').replace('&rdquo','').replace('&hellip;','')
        try:
            # 将爬取的段子写入文件
            file = open(file_name,'a',encoding='utf-8')
            file.write('\n'.join(duanzi.split()))
            file.close()
        except OSError as e:
            print(e)