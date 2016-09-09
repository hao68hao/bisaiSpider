# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
#import tool


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
#toolz = tool.Tool()

class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n不
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

class BDTB:
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        self.floor = 1
        self.file = None
        self.content="" #定一个变量用于存储贴吧的数据

    #定义一个析构函数用于自动关闭创建的文件句柄
    def __del__(self):
        if self.file is not None:
            self.file.close()

    #获取页面内容
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            content = response.read()
            return content

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧错误,错误原因",e.reason
                return None

    #获取页面的标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取贴子的所有页码
    def getAllPage(self):
        page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?><span.*?>(.*?)</span>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取页面中每个楼层的贴子内容
    def getContent1(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        for item in items:
            print self.floor, u"楼======-------========---------=========----------"
            temp = self.tool.replace(item)
            print temp
            self.content += temp
            self.floor += 1

    def writeData(self):
        if not self.content:
            return
        if self.file is None:
            self.file = open("tieba0323.txt","w")
        self.file.write(self.content)


baseURL = 'http://tieba.baidu.com/p/4032381165'
bd = BDTB(baseURL,1)
bd.getContent1(bd.getPage(1))
bd.writeData()#getContent1  已经将要写入的内容整理好了，直接调用写入即可。

print u'=======\n',bd.getTitle()
print u'=======\n',bd.getAllPage()





