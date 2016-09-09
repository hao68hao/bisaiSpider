#-*- coding:utf-8 -*-
import urllib2
import re
import sys
import torndb

reload(sys)
sys.setdefaultencoding('utf8')
db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")

class IRSRACE:

    def __init__(self,baseUrl):
        self.baseURL = baseUrl
        self.content = "" #定一个变量用于存储贴吧的数据
        self.file = None
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # self.headers = { 'User-Agent' : user_agent }
        # replacetool = tool.Tool()

    #抓取网页页面的全部代码
    def getpageContents(self,page):
        try:
            url = self.baseURL + str(page)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            contents = response.read().decode('utf-8')
            # print contents
            return contents

        except urllib2.HTTPError, e:
            if hasattr(e,"reason"):
                print u"连接网页失败",e.reason
                return None

    #根据正则表达式抓取具体的内容
    def getContents(self,page):
        pattern = re.compile('<div class="race-itemlist clearfix">(.+?)</div> -->',re.S)
        result = re.findall(pattern,page)
        for k in result:
            pattern = re.compile('<div class="itemname.*?<strong><a href="/bundled_.*?>(.*?)</a>.*?<div class="attr">(.*?)</div>.*?<span class="itemtime.*?>(.*?)</span>.*?<div class="col-md-3">.*?>(.*?)</div>',re.S)
            items = re.findall(pattern,k)
            for k in items:
                # print "\n比赛名称:",k[0].strip(),"\n比赛地点:",k[1].strip(),"\n比赛时间:",k[2].strip(),"\n比赛报名时间:",k[3].strip()
                temp = "{0} {1} {2} {3}".format(k[0].strip(),k[1].strip(),k[2].strip(),k[3].strip())
                self.torndbConn(k)
                self.content += temp

    #获取所有的页码数
    def getAllPageNum(self):
        page = self.getpageContents(1)
        pattern = re.compile('<a href="/bundled_races?month=all&amp;page=66">(.*?)</a>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    '''
    #将获取的内容输出为txt文件
    def writeData(self):
        if not self.content:
            return
        if self.file is None:
            self.file = open("irsRace--1.txt","w")
        self.file.write(self.content)

    #定义一个析构函数用于自动关闭创建的文件句柄
    def __del__(self):
        if self.file is not None:
            self.file.close()
    '''

    def torndbConn(self,k):
         # print k
        try:
            exe = "insert into raceIRS(raceName,raceADD,raceTime,raceBETime) values ('%(raceName)s', '%(raceADD)s', '%(raceTime)s', '%(raceBETime)s')" % dict(raceName=k[0].strip(),
                                                raceADD=k[1].strip(),
                                                raceTime=k[2].strip(),
                                                raceBETime=k[3].strip())

            print exe
            db.execute(exe)
        except Exception as e:
            print (e)

baseUrl = 'http://iranshao.com/bundled_races?month=all&page='
irsRace = IRSRACE(baseUrl)
# nums = irsRace.getAllPageNum()
for n in xrange(1, 66):
    print '正在写入数据'
    irsRace.getContents(irsRace.getpageContents(n))
    # irsRace.writeData() #getContents  已经将要写入的内容整理好了，直接调用写入即可。
# print '========df',irsRace.getAllPageNum()

