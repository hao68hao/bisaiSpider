#-*- conding:utf-8 -*-

from flask import Flask,render_template
from modelsirs import Race
import torndb
app = Flask(__name__)

@app.route("/raceypw")
def tableRace():
    race = []
    db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")
    for raceInfo in db.query("SELECT * FROM raceDB.raceYPW"):
        raceCon = Race(raceInfo.raceName, raceInfo.raceTime, raceInfo.beginBM, raceInfo.endBM, raceInfo.raceNote)
        race.append(raceCon)
    return render_template("raceypw.html", ypw=race)

if __name__ == '__main__':
    app.run(debug=True)