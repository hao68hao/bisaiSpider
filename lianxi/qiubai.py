# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

url = 'http://www.qiushibaike.com/hot/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

filename = 'qiubai.txt'
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)

    content = response.read().decode('utf-8')
    pattern = re.compile('<div class="article block untagged mb15" (.+?)>(.+?)<div class="single-clear"></div>',re.S)
    items = re.findall(pattern,content)

    for item in items:
        pattern = re.compile('<h2>(.+?)</h2>(.+?)<div class="content">(.+?)<!--.+?-->',re.S)
        j = re.findall(pattern,item[1])
        for k in j:
            print k[0],k[2]

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

