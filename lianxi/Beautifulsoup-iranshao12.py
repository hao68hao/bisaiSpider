# -*- coding: utf-8 -*-
import urllib2
import urllib
import re
import sys

# import torndb

reload(sys)
sys.setdefaultencoding('utf8')

page = 10
url = 'http://iranshao.com/bundled_races?month=all&page=' + str(page)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

#定义一个字典
stortes = []

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    #将网页的内容传入变量
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="race-itemlist clearfix">(.+?)</div> -->',re.S)

    items = re.findall(pattern,content)



    for item in items:
        # print item
        pattern = re.compile('<div class="itemname.*?<strong><a href="/bundled_.*?>(.*?)</a>.*?<div class="attr">(.*?)</div>.*?<span class="itemtime.*?>(.*?)</span>.*?<div class="col-md-3">.*?>(.*?)</div>',re.S)
        # pattern = re.compile('<div class="col-md-3">.*?>(.*?)</div>',re.S)
        bisaiNmae = re.findall(pattern,item)

        for k in bisaiNmae:
            # print k[0].strip(),k[1].strip(),k[2].strip(),k[3].strip()
            #数字存入字典后打印
            stortes.append([k[0].strip(),k[1].strip(),k[2].strip(),k[3].strip()])
            print len(stortes)



except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

        # soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
        # print "一获取所有的链接::::::"
        # 
        # links = soup.find_all('a', )
        # for link in links:
        #     print link.name, link['href'], link.get_text()
        #
        # print "二获取lacie链接::::::"
        # link_node = soup.find('a',href="http://example.com/lacie")
        # print link_node.name, link_node['href'], link_node.get_text()
        #
        # print "三正则表达式匹配::::::"
        # link_node = soup.find('a', href=re.compile(r"ill"))
        # print link_node.name, link_node['href'], link_node.get_text()
        #
        # print "四获取文字::::::"
        # p_node = soup.find('p', class_="title")
        # print p_node.name, p_node.get_text()





