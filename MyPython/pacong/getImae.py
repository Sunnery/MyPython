# -*-coding:utf-8 -*-
'''
Created on 2016-8-11

@author: Jerry
'''
import urllib
import re
from base64 import encode

def getHTML(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getElement(html,reg):
    #reg = r'src="(.+?\.jpg)" pic_ext'
    #reg = r'<span class="view">+(\d+) 浏览</span>+'
    regObj = re.compile(reg)
    urls = re.findall(regObj, html)
    return urls


html = getHTML("http://wiki.guesslive.com/")

reg_total_page = r'1 / +(\d+) +'
total_page = getElement(html, reg_total_page)[0];
# print total_page;

#获取所有文章
reg_article= r'<article>+(\d+)</article>+'
#获取阅读量
reg_view_num= r'<span class="view">+([\s\S]*) 浏览</span>+'
#获取文章标题
reg_title= r'>+([\s\S]*)</a> <span class="view">+'
#获取文章链接
reg_title= r'<hgroup><h2><a href="+([\s\S]*) ">+'

total_view = 0
most_popular = 0

for i in range(1,int(total_page)+1):
    url = "".join(["http://wiki.guesslive.com/?page=",str(i)])
    html = getHTML(url)
    articles = str(html).index("<article>")
    print articles
    for article in articles:
        view_num = getElement(article,reg_view_num)
        print article
        print '-------------------------------'


print "".join(["wiki最受欢迎文章阅读量： ",str(most_popular)])        
print "".join(["wiki文章总阅读量： ",str(total_view)])
        
         
