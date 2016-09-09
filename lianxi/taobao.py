# -*- coding:utf-8 -*-
import urllib2
import urllib
import re

class TaobaoMM():

    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self, pageindex):
        url = self.siteURL + "?page=" + str(pageindex)

        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('GBK')

    def getContents(self,pageindex):
        page = self.getPage(pageindex)
        parrent = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
        # <div class="list-item".*?pic-word.*?
        # <a href="(.*?)".*?
        # <img src="(.*?)".*?
        # <a class="lady-name.*?>(.*?)</a>.*?
        # <strong>(.*?)</strong>.*?
        # <span>(.*?)</span>'
        # ,re.S)
        items = re.findall(parrent,page)
        contents = []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4]])
        return contents

    #获取MM个人详情页面
    def getDetailPage(self,infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read().decode('GBK')

    #获取所有的文字简介
    def getBrief(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        result = re.match(pattern,page)
        # return self.tool.replace(result.group(1))
        return self.tool.replace(result.group(1))

    def getAllImg(self,page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
        content = re.search(pattern,page)
        patternImg = re.compile('<img.*?src="(.*?)"',re.S)
        images = re.findall(patternImg,content.group(1))
        return images

    # #保存多张写真图片
    def savaImgs(self,images,name):
        number = 1
        print u"发现",name,u"共有",len(images),u"张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = 'jpg'
            fileName = name + "/" + str(number) + "." + fTail
            self.saveImg(imageURL,fileName)
            number += 1

    # 保存头像
    def saveIcon(self,iconURL,name):
        splitPath = iconURL,split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL,fileName)

    # 保存个人简介
    def saveBrief(self,content,name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName,"w+")
        print u"正在偷偷保存她的个人信息为",fileName
        f.write(content,encode('utf-8'))

    #传入图片地址，文件名，保存单张图片
    def saveImg(self,imageURL,fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print u"正在保存一张图片为",fileName
        f.close()

    #创建新目录
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        #不存在   False
        isExists=os.path.exists(path)
        if not isExists:
            print u"偷偷新建了名字叫做",path,u'的文件夹'
            os.makedirs(path)
            return True
        else:
            print u"名为",path,'的文件夹已经创建成功'
            return False

    #将一页淘宝MM的信息保存起来
    #将一页淘宝MM的信息保存起来
    def savePageInfo(self,pageIndex):
        #获取第一页淘宝MM列表
        contents = self.getContents(pageIndex)
        for item in contents:
            #item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
            print u"发现一位模特,名字叫",item[2],u"芳龄",item[3],u",她在",item[4]
            print u"正在偷偷地保存",item[2],"的信息"
            print u"又意外地发现她的个人地址是",item[0]
            #个人详情页面的URL
            detailURL = item[0]
            #得到个人详情页面代码
            detailPage = self.getDetailPage(detailURL)
            #获取个人简介
            brief = self.getBrief(detailPage)
            #获取所有图片列表
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            #保存个人简介
            self.saveBrief(brief,item[2])
            #保存头像
            self.saveIcon(item[1],item[2])
            #保存图片
            self.saveImgs(images,item[2])

    #传入起止页码，获取MM图片
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print u"正在偷偷寻找第",i,u"个地方，看看MM们在不在"
            self.savePageInfo(i)

spider = TaobaoMM()
spider.savePagesInfo(2,10)