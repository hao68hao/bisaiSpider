# -*- coding: utf-8 -*-
import json
import urllib2
import chardet



# db = torndb.Connection("127.0.0.1:3306", "iaskDB", user="root", password="h@o@0315")
# print db

page = 3
url = 'http://42trip.com/races/?ajaxLoad&registerStatus=-1&country=-1&city=-1&smart=-1&raceType=-1&startTime=-1&endTime=-1&page=' + str(page) + '&limit=8'
# uru = 'http://42trip.com/races/?ajaxLoad&registerStatus=-1&country=-1&city=-1&smart=-1&raceType=-1&startTime=-1&endTime=-1&page=3&limit=8'
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    #将网页的内容传入变量
    content = response.read().decode('utf-8')

    x = json.loads(content)
    for yxy in x:
        print "\n所在国家:",yxy["countryName"],\
            "\n所在城市:",yxy["cityName"],\
            "\n比赛名称:",yxy["cnName"],\
            "\n比赛时间:",yxy["raceTime"],\
            "\n报名状态:",yxy["eventStatus"],\
            "\n比赛项目:",yxy["raceType"]



except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
except Exception as es:
    print es



