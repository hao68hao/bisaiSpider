#-*- conding:utf-8 -*-

from flask import Flask,render_template
from modelsRace import Race
import torndb
app = Flask(__name__)

@app.route("/raceajs")
def tableRace():
    race = []
    db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")
    for raceInfo in db.query("SELECT * FROM raceDB.raceAJS"):
        raceCon = Race(raceInfo.raceName, raceInfo.raceADD, raceInfo.raceTime, raceInfo.raceNote)
        race.append(raceCon)
    return render_template("raceajs.html", ajs=race)

if __name__ == '__main__':
    app.run(debug=True)

