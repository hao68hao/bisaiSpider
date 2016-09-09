#-*- codeing:utf-8 -*-

import torndb

db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")

class selectDB():
    def __init__(self):
        self.racename = ""
        self.raceadd = ""
        self.racetime = ""
        self.racenote = ""

    def dbtwo(self):

        dbtow = []
        for dbDate in db.query('select * from raceDB.raceIRS where raceTime like "%2017%"'):
            raceinfo = (dbDate.racename, dbDate.racetime, dbDate.racenote, dbDate.raceadd)
            dbtow.append(raceinfo)
            print dbtow()

selectdb = selectDB()
print selectdb.dbtwo()




