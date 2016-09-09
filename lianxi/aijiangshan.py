# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
import chardet
# from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")

url = 'http://www.phonedm.com/race/race.jsp?racelisttype'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read()

    #转换编码
    x = chardet.detect(content)
    content = content.decode(x["encoding"])

    pattern = re.compile('<div class="racerowwords">(.+?)<div class="racerowline">',re.S)
    items = re.findall(pattern,content)

    for item in items:
        #正则表达式,除报名时间外
        pattern = re.compile('<div class="racename.*?><a href="race.*?>(.*?)</div>(.*?)<div class="applehui1_14">(.*?)</div>(.*?)<div class="racetime applehui1_14">(.*?)</div>(.*?)<div class="raceheight applehui2_14">(.*?)</div>',re.S)
        bisaiNmae = re.findall(pattern,item)
        for bisaiNA in bisaiNmae:
            # 正则表达式,除报名截至时间外
            print '\n比赛名称:',bisaiNA[0].strip(),'\n比赛地点:',bisaiNA[2].strip(),'\n比赛时间:',bisaiNA[4].strip(),'\n比赛爬升:',bisaiNA[6].strip()

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason



#########正则表达式组成############

        #正则表达式,全部
        # pattern = re.compile('<div class="racename.*?><a href="race.*?>(.*?)</div>(.*?)<div class="applehui1_14">(.*?)</div>(.*?)<div class="racetime applehui1_14">(.*?)</div>(.*?)<div class="raceheight applehui2_14">(.*?)</div>.*?<div.*?class="racefollow.*?applehui1_14.*?>.*?<div class="racefollowword.*?>(.*?)</div>.*?<div class="racefollowword".*?style="margin-top:4px.*?>(.*?)</div>(.*?)<div class="racefollowword">(.*?)</div>',re.S)
        # pattern = re.compile('<div class="racename.*?><a href="race.*?>(.*?)</div>(.*?)<div class="applehui1_14">(.*?)</div>(.*?)<div class="racetime applehui1_14">(.*?)</div>(.*?)<div class="raceheight applehui2_14">(.*?)</div>(.*?)<div.*?class="racefollow.*?applehui1_14.*?>.*?<div class="racefollowword.*?>(.*?)</div>.*?<div class="racefollowword".*?style="margin-top:4px.*?>(.*?)</div>(.*?)<div class="racefollowword">(.*?)</div>',re.S)
        # pattern = re.compile('<div class="racename.*?><a href="race.*?>(.*?)</div>.*?<div class="applehui1_14”>(.*?)</div>.*?<div class="racetime applehui1_14">(.*?)</div>.*?<div.*?class="racefollow.*?applehui1_14.*?>.*?<div class="racefollowword.*?>(.*?)</div>.*?<div class="racefollowword".*?style="margin-top:4px.*?>(.*?)</div>.*?<div class="racefollowword">(.*?)</div>.*?<div class="raceheight applehui2_14">(.*?)</div>',re.S)
        #正则表达式,除报名时间外
        # pattern = re.compile('<div class="racename.*?><a href="race.*?>(.*?)</div>(.*?)<div class="applehui1_14">(.*?)</div>(.*?)<div class="racetime applehui1_14">(.*?)</div>(.*?)<div class="raceheight applehui2_14">(.*?)</div>',re.S)
        #正则表达式,报名截至时间
        # pattern = re.compile('<div.*?class="racefollow.*?applehui1_14.*?>.*?<div class="racefollowword.*?>(.*?)</div>.*?<div class="racefollowword".*?style="margin-top:4px.*?>(.*?)</div>(.*?)<div class="racefollowword">(.*?)</div>',re.S)


        #正则表达式,全部
            # print bisaiNA[0].strip(),bisaiNA[2].strip(),bisaiNA[4].strip(),bisaiNA[6].strip(),bisaiNA[8].strip(),bisaiNA[9].strip(),bisaiNA[11].strip()
            # print bisaiNA[0].strip(),bisaiNA[2].strip()

            # print bisaiNA[0].strip(),bisaiNA[1].strip(),bisaiNA[2].strip(),bisaiNA[3].strip(),bisaiNA[4].strip(),bisaiNA[5].strip(),bisaiNA[6].strip()
            # 正则表达式,除报名时间外
            # print bisaiNA[0].strip(),bisaiNA[2].strip(),bisaiNA[4].strip(),bisaiNA[6].strip()
            # 正则表达式,报名截至时间
            # print bisaiNA[0].strip(),bisaiNA[1].strip(),bisaiNA[3].strip()

#########正则表达式分解############
    # 抓取内容区域:<div class="racerowwords">(.+?)<div class="racerowline">
    # 名称:<div class="racename.*?><a href="race.*?>(.*?)</div>(.*?)
    # 地点:<div class="applehui1_14">(.*?)</div>(.*?)
    # 比赛时间:<div class="racetime applehui1_14">(.*?)</div>(.*?)
    # 海拔:<div class="raceheight applehui2_14">(.*?)</div>
    # 报名时间:<div.*?class="racefollow.*?applehui1_14.*?>.*?<div class="racefollowword.*?>(.*?)</div>.*?<div class="racefollowword".*?style="margin-top:4px.*?>(.*?)</div>(.*?)<div class="racefollowword">(.*?)</div>

##########if.....else语句###########
        # if status == 1:
        #     pattern = re.compile('<div class="racename.*?><a href="race.*?>(.*?)</div>(.*?)<div class="applehui1_14">(.*?)</div>(.*?)<div class="racetime applehui1_14">(.*?)</div>(.*?)<div class="raceheight applehui2_14">(.*?)</div>',re.S)
        #     bisaiNmae = re.findall(pattern,item)
        #     for bisaiNA in bisaiNmae:
        #         print bisaiNA[0].strip(),bisaiNA[2].strip(),bisaiNA[4].strip(),bisaiNA[6].strip()
        # elif status == 2:
        #     pattern = re.compile('<div.*?class="racefollow.*?applehui1_14.*?>.*?<div class="racefollowword.*?>(.*?)</div>.*?<div class="racefollowword".*?style="margin-top:4px.*?>(.*?)</div>(.*?)<div class="racefollowword">(.*?)</div>',re.S)
        #     bisaiNmae = re.findall(pattern,item)
        #     for bisaiNA in bisaiNmae:
        #         print bisaiNA[0].strip(),bisaiNA[1].strip(),bisaiNA[3].strip()





