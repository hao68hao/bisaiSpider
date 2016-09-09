# -*- coding: utf-8 -*-
import json
import urllib2
import chardet

class yiPao:

    def getPageCode(self,page):
        try:
            url = 'http://www.erun360.com/action/EventService.ashx?op=seach&g=0&t=0&lx=99&p=' + str(page) + '&key='

            request = urllib2.Request(url)
            response = urllib2.urlopen(request)

            #将网页的内容传入变量
            content = response.read().decode('GB2312')
            x = json.loads(content)
            for yxy in x:
                print "\n比赛名称:",yxy["cTitle"],"\n比赛时间:",yxy["dRaceBegin"],"\n报名开始时间:",yxy["dJoinBegin"],"报名结束时间:",yxy["dJoinEnd"],"\n备注:",yxy["item"]
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

x = yiPao()
x.getPageCode(6)
