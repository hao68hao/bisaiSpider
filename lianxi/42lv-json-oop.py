# -*- coding: utf-8 -*-
import json
import urllib2

# class YPRace:
#     def __index__(self):
#         self.items = ""
#
#     def getPage(self,pageNum):
#         try:
#             url = 'http://www.erun360.com/action/EventService.ashx?op=seach&g=0&t=0&lx=99&p=' + str(pageNum) + '&key='
#             req = urllib2.Request(url)
#             response = urllib2.urlopen(req)
#             content = response.read().decode('GB2312')
#             self.items = json.loads(content)
#             for yxy in self.items:
#                 print "\n比赛名称:",yxy["cTitle"],"\n比赛时间:",yxy["dRaceBegin"],"\n报名开始时间:",yxy["dJoinBegin"],"报名结束时间:",yxy["dJoinEnd"],"\n备注:",yxy["item"]
#
#         except urllib2.URLError,e:
#             if hasattr(e, "reason"):
#                 print "连接失败", e.reason
#                 return None
#
# yipaoRace = YPRace()
# print yipaoRace.getPage(3)

class tripFTRace:

    def __index__(self):
        self.items = ""

    def getPage(self,pageNum):
        try:
            url = 'http://42trip.com/races/?ajaxLoad&registerStatus=-1&country=-1&city=-1&smart=-1&raceType=-1&startTime=-1&endTime=-1&page=' + str(pageNum) + '&limit=8'
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            content = response.read()
            self.items = json.loads(content)
            # print self.items

            for yxy in self.items:
                print "\n所在国家:", yxy["countryName"], \
                    "\n所在城市:", yxy["cityName"], \
                    "\n比赛名称:", yxy["cnName"], \
                    "\n比赛时间:", yxy["raceTime"], \
                    "\n报名状态:", yxy["eventStatus"], \
                    "\n比赛项目:", yxy["raceType"]

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print u"连接失败,错误代码:", e.code
            if hasattr(e, "reason"):
                print u"连接失败,错误原因:", e.reason
        except Exception as es:
            print es

ftLVrace = tripFTRace()
print ftLVrace.getPage(4)

