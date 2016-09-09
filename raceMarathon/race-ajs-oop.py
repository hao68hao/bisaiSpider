#-*- coding:utf-8 -*-
import urllib2
import re
import sys
import chardet
import torndb

reload(sys)
sys.setdefaultencoding("utf-8")
db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")

class IJSRACE:

    def __init__(self):
        self.content = "" #定义一个变量接收getpageContents的内容
        self.file = None

        # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # headers = { 'User-Agent' : user_agent }

    def getpageContents(self):
        try:
            url = 'http://www.phonedm.com/race/race.jsp?racelisttype'
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            contents = response.read()
            print contents

            #转换编码
            x = chardet.detect(contents)
            contents = contents.decode(x["encoding"])

            # self.content = contents
            # return self.content
            return contents
        except urllib2.HTTPError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print u"连接网页失败",e.reason

    def getContents(self):
        x = self.getpageContents()
        pattern = re.compile('<div class="racerowwords">(.+?)<div class="racerowline">',re.S)
        items = re.findall(pattern,x)
        self.content = '' #清空self.content内容,不将HTML代码传入需要的结果中.
        for item in items:
            pattern = re.compile('<div class="racename.*?><a href="race.*?>(.*?)</a>(.*?)<div class="applehui1_14">(.*?)</div>(.*?)<div class="racetime applehui1_14">(.*?)</div>(.*?)<div class="raceheight applehui2_14">(.*?)</div>',re.S)
            bisaiName = re.findall(pattern,item)
            for bisaiNA in bisaiName:
                temp = "{0} {1} {2} {3}".format(bisaiNA[0].strip(),bisaiNA[2].strip(),bisaiNA[4].strip(),bisaiNA[6].strip())
                self.torndbConn(bisaiNA)
                self.content += temp

    def getAllPage(self):
        pass

    '''
    #将获取的内容输出为txt文件
    def writeData(self):
        if not self.content:
            return
        if self.file is None:
            self.file = open("ajs-1.txt","w")
        self.file.write(self.content)

    #定义一个析构函数用于自动关闭创建的文件句柄
    def __del__(self):
        if self.file is not None:
            self.file.close()
    '''

    def torndbConn(self,bisaiNA):
        # print bisaiNA
        try:
            exe = "insert into raceAJS(raceName,raceADD,raceTime,raceNote) values ('%(raceName)s', '%(raceADD)s'," \
                  " '%(raceTime)s', '%(raceNote)s')" % dict(raceName=bisaiNA[0].strip(),
                                                        raceADD=bisaiNA[2].strip(),
                                                        raceTime=bisaiNA[4].strip(),
                                                        raceNote=bisaiNA[6].strip())
            print(exe)
            db.execute(exe)
        except Exception as e:
            print(e)

ijsRace = IJSRACE()
ijsRace.getContents()
# ijsRace.writeData()

