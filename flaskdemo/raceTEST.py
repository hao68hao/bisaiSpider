#-*- conding:utf-8 -*-

from flask import Flask,render_template
from modelsajs import ajsRace
from modelsirs import irsRace
from modelsypw import ypwRace
import torndb
app = Flask(__name__)
db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")

@app.route("/raceajs")
def tableajsRace():
    raceajs = []
    # db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")
    for raceInfo in db.query("SELECT * FROM raceDB.raceAJS"):
        raceajsCon = ajsRace(raceInfo.raceName, raceInfo.raceADD, raceInfo.raceTime, raceInfo.raceNote)
        raceajs.append(raceajsCon)
    return render_template("raceajs.html", ajs=raceajs)

@app.route("/raceirs")
def tableirsRace():
    raceirs = []
    # db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")
    for raceInfo in db.query("SELECT * FROM raceDB.raceIRS"):
        raceirsCon = irsRace(raceInfo.raceName, raceInfo.raceADD, raceInfo.raceTime, raceInfo.raceBETime)
        raceirs.append(raceirsCon)
    return render_template("raceirs.html", irs=raceirs)

@app.route("/raceypw")
def tableypwRace():
    raceypw = []
    # db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")
    for raceInfo in db.query("SELECT * FROM raceDB.raceYPW"):
        raceypwCon = ypwRace(raceInfo.raceName, raceInfo.raceTime, raceInfo.beginBM, raceInfo.endBM, raceInfo.raceNote)
        raceypw.append(raceypwCon)
    return render_template("raceypw.html", ypw=raceypw)

if __name__ == '__main__':
    app.run(debug=True)

