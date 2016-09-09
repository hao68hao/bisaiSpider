#-*- coding:utf-8 -*-
import urllib2
import re
import sys
import json
import torndb
# import lianxi.tool

reload(sys)
sys.setdefaultencoding('utf8')
db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")

class YIPAO:

    def __init__(self):
        self.content = "" #定一个变量用于存储贴吧的数据
        self.file = None
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # self.headers = { 'User-Agent' : user_agent }
        # replacetool = tool.Tool()

    #抓取网页页面的全部代码
    def getpageContents(self,page):
        try:
            url = 'http://www.erun360.com/action/EventService.ashx?op=seach&g=0&t=0&lx=99&p=' + str(page) + '&key='
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            contents = response.read().decode('gb2312')
            self.content = contents
            # print self.content
            return self.content

        except urllib2.HTTPError, e:
            if hasattr(e,"reason"):
                print u"连接网页失败",e.reason
                return None

    #根据正则表达式抓取具体的内容
    def getContents(self,page):
        x = json.loads(self.content)
        for yxy in x:
            self.torndbConn(yxy)
            # print "\n比赛名称:",yxy["cTitle"],"\n比赛时间:",yxy["dRaceBegin"],"\n报名开始时间:",yxy["dJoinBegin"],"报名结束时间:",yxy["dJoinEnd"],"\n备注:",yxy["item"]

    #获取所有的页码数
    def getAllPageNum(self):
        pass

    '''
    #将获取的内容输出为txt文件
    def writeData(self):
        if not self.content:
            return
        if self.file is None:
            self.file = open("yipao--2.txt","w")
        self.file.write(self.content)

    #定义一个析构函数用于自动关闭创建的文件句柄
    def __del__(self):
        if self.file is not None:
            self.file.close()
    '''

    def torndbConn(self,yxy):
        # print yxy
        try:
            exe = "insert into raceYPW(raceName,raceTime,beginBM,endBM,raceNote) values ('%(raceName)s', '%(raceTime)s'," \
                  " '%(beginBM)s', '%(endBM)s','%(raceNote)s')" % dict(raceName=yxy["cTitle"].strip(),
                                                        raceTime=yxy["dRaceBegin"].strip(),
                                                        beginBM=yxy["dJoinBegin"].strip(),
                                                        endBM=yxy["dJoinEnd"].strip(),
                                                        raceNote=yxy["item"])
            # print(exe)
            db.execute(exe)
        except Exception as e:
            print(e)



yipao = YIPAO()
nums = yipao.getAllPageNum()
# for n in xrange(1, nums)
for n in xrange(1, 7):
    print '正在写入数据'
    yipao.getContents(yipao.getpageContents(n))
    # yipao.writeData() #getContents  已经将要写入的内容整理好了，直接调用写入即可。
# print '========df',yipao.getAllPageNum()
