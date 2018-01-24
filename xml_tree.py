# -*- coding:utf-8 -*-

from lxml import etree

html = etree.parse('hello.html')

result = etree.tostring(html, pretty_print=True)

print(result)