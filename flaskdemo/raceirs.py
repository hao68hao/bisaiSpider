#-*- conding:utf-8 -*-

from flask import Flask,render_template
from modelsirs import Race
import torndb
app = Flask(__name__)

@app.route("/raceirs")
def tableRace():
    race = []
    db = torndb.Connection("127.0.0.1:3306", "raceDB", user="root", password="198168")
    for raceInfo in db.query("SELECT * FROM raceDB.raceIRS"):
        raceCon = Race(raceInfo.raceName, raceInfo.raceADD, raceInfo.raceTime, raceInfo.raceBETime)
        race.append(raceCon)
    return render_template("raceirs.html", irs=race)

if __name__ == '__main__':
    app.run(debug=True)