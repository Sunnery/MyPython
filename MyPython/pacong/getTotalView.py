# -*- coding:utf-8 -*-
'''
Created on 2016-8-11

@author: 研发
'''
import urllib
import re

def getNums(url):
    page = urllib.urlopen(url)
    html = page.read
    reg = r'<span class="view">+(\d+) 浏览</span>+'
    regObj = re.compile(reg)
    nums = re.findall (regObj , html )
    return nums

nums = getNums("http://wiki.guesslive.com/")
print nums