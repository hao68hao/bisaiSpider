# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import tool

class Tool:
    #去除img标签,1-7位空格,&nbsp;
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    #将多行空行删除
    removeNoneLine = re.compile('\n+')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.removeNoneLine,"\n",x)
        #strip()将前后多余内容删除
        return x.strip()

class BDTB:

    def __init__(self,baseUrl,seeLZ,floorTag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaulTitle = u"百度贴吧"
        self.floorTag = floorTag

    #获取页面的内容
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,原因是:", e.reason
                return None

    #获取帖子首页的标题
    def getTitle(self,page):
        # page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取帖子所有的页码
    def getPageNum(self,page):
        # page = self.getPage(1)
        pattern = re.compile('<li class="l_reply_num.*?><span.*?>(.*?)</span>',re.S)
        result = re.search(pattern, page)
        if result:
            # print result.group(1)
            return result.group(1).strip
        else:
            return None

    #获取每一层楼的内容,传入页面内容:
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    #设置文件的标题
    def setFileTitle(self,title):
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaulTitle + ".txt","w+")

    #向文件写入每一楼的信息
    def writeData(self,contents):
        for item in contents:
            if self.floorTag == '1':
                floorLine = "\n" + str(self.floor) + u"-------------------------------------------\n"
                self.file.write(floorLine)
                self.file.write(item)
                self.floor += 1

    # 开始
    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)

        if pageNum == None:
            print "URL失效,请重试"
            return
        try:
            print "该帖子共有" + str(pageNum) + "页"
            for i in range(1,int(pageNum)+1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        except IOError,e:
            print "写入异常,原因" + e.message
        finally:
            print "写入任务完成"

print u"请输入贴子代号"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
seeLZ = raw_input("是否只获取楼主发言,是输入1,否输入0\n")
floorTag = raw_input("是否写入楼层信息,是输入1,否输入0\n")
bd = BDTB(baseURL,seeLZ,floorTag)
bd.start()