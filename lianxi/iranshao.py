# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import sys
import tool

reload(sys)
sys.setdefaultencoding('utf8')

page = 10
url = 'http://iranshao.com/bundled_races?month=all&page=' + str(page)

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
replacetool = tool.Tool()

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    #将网页的内容传入变量
    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="race-itemlist clearfix">(.+?)</div> -->',re.S)
    items = re.findall(pattern,content)
    for item in items:
        pattern = re.compile('<div class="itemname.*?<strong><a href="/bundled_.*?>(.*?)</a>.*?<div class="attr">(.*?)</div>.*?<span class="itemtime.*?>(.*?)</span>.*?<div class="col-md-3">.*?>(.*?)</div>',re.S)
        bisaiNmae = re.findall(pattern,item)
        for k in bisaiNmae:
            print "\n比赛名称:",k[0].strip(),"\n比赛地点:",k[1].strip(),"\n比赛时间:",k[2].strip(),"\n比赛报名时间:",k[3].strip()

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason


#连接数据库
# def createDataBaseConn(self):
#         db = torndb.Connection(MYSQL_CONFIG_MASTER["server"],
#                 "live",
#                 user=MYSQL_CONFIG_MASTER["username"],
#                 password=MYSQL_CONFIG_MASTER["password"],
#                 time_zone="+8:00")
#         return db


    #content = content.replace("\r", "")
    #content = content.replace("\n", "")
    #content = content.replace("\t", "")
    # content = content.replace(" ", "")

    #====正则表达式====
    # 比赛名称
    # <div class="itemname.*?<strong><a href="/bundled_.*?>(.*?)</a>
    # 比赛地点
    # <div class="attr">(.*?)</div>
    # 比赛时间
    # <span class="itemtime.*?>(.*?)</span>
    # 比赛状态及报名时间
    # <div class="col-md-3">.*?>(.*?)</div>
