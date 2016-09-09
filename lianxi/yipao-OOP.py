# -*- coding: utf-8 -*-
import json
import urllib2

class YPRace:
    def __index__(self):
        self.items = ""

    def getPage(self,pageNum):
        try:
            url = 'http://www.erun360.com/action/EventService.ashx?op=seach&g=0&t=0&lx=99&p=' + str(pageNum) + '&key='
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            content = response.read().decode('GB2312')
            self.items = json.loads(content)
            for yxy in self.items:
                print "\n比赛名称:",yxy["cTitle"],"\n比赛时间:",yxy["dRaceBegin"],"\n报名开始时间:",yxy["dJoinBegin"],"报名结束时间:",yxy["dJoinEnd"],"\n备注:",yxy["item"]

        except urllib2.URLError,e:
            if hasattr(e, "reason"):
                print "连接失败", e.reason
                return None

yipaoRace = YPRace()
print yipaoRace.getPage(3)


