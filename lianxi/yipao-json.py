# -*- coding: utf-8 -*-
import json
import urllib2
import chardet
# import torndb


# db = torndb.Connection("127.0.0.1:3306", "iaskDB", user="root", password="h@o@0315")
# print db

page = 1
url = 'http://www.erun360.com/action/EventService.ashx?op=seach&g=0&t=0&lx=99&p=' + str(page) + '&key='

try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    #将网页的内容传入变量
    content = response.read().decode('GB2312')
    print content

    x = json.loads(content)
    for yxy in x:
        print "\n比赛名称:",yxy["cTitle"],"\n比赛时间:",yxy["dRaceBegin"],"\n报名开始时间:",yxy["dJoinBegin"],"报名结束时间:",yxy["dJoinEnd"],"\n备注:",yxy["item"]

        db.execute("INSERT INTO raceYPW(raceName,raceTime,beginBM,endBM,raceNote) VALUES (%(rid)s,%(raceName)s,%(raceTime)s,%(beginBM)s,%(endBM)s,%(raceNote)s)",
                raceName=yxy["cTitle"],
                raceTime=yxy["dRaceBegin"],
                beginBM=yxy["dJoinBegin"],
                endBM=yxy["dJoinEnd"],
                raceNote=yxy["item"])

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
except Exception as es:
    print es



# CREATE TABLE `iaskDB`.`yipao_net` (
#   `raceName` VARCHAR(45) NOT NULL,
#   `raceTime` VARCHAR(45) NULL,
#   `beginBM` VARCHAR(45) NULL,
#   `endBM` VARCHAR(45) NULL,
#   `raceNote` VARCHAR(45) NULL,
#   PRIMARY KEY (`raceName`));

 # def insert(self, data):
 #        now = str(datetime.datetime.now())
 #        return self.execute("INSERT INTO tb_live(user_id, `name`, category, "
 #                            "publish_time, public, online_people, play_time, poster,"
 #                            "`desc`, position, channel, create_at, update_at)VALUES("
 #                            "%(user_id)s, %(name)s, %(category)s, %(publish_time)s,"
 #                            "%(public)s, %(online_people)s, %(play_time)s, %(poster)s,"
 #                            "%(desc)s, %(position)s, %(channel)s, %(create_at)s, %(update_at)s)",
 #                            user_id=data["user_id"],
 #                            name=data["name"],
 #                            category=data["category"],
 #                            publish_time=data["publish_time"],
 #                            public=data["public"],
 #                            poster=data["poster"],
 #                            online_people=data["online_people"],
 #                            play_time=data["play_time"],
 #                            desc=data["desc"],
 #                            position=data["position"],
 #                            channel=data["channel"],
 #                            create_at=now,
 #                            update_at=now)
 #


# LTER TABLE `iaskDB`.`yipao_net`
# CHANGE COLUMN `raceName` `raceName` VARCHAR(45) CHARACTER SET 'utf8' NOT NULL ,
# CHANGE COLUMN `raceTime` `raceTime` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL ,
# CHANGE COLUMN `beginBM` `beginBM` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL ,
# CHANGE COLUMN `endBM` `endBM` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL ;
