import json
from flask import Flask, render_template, request

from one_on_one.group import GCGroup
from one_on_one.pair import GCPair
from one_on_one.schedule import GCSchedule

group_class = GCGroup
pair_class = GCPair
schedule_class = GCSchedule

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/people')
def people():
    group = group_class().get()
    return render_template("people.html", group=group, group_string=json.dumps(group))

@app.route('/pair', methods=["POST"])
def pair():
    group = json.loads(request.form["group"])
    pairs = GCPair().get_pairs(group)
    return render_template("pairs.html", pairs=pairs, pairs_string=json.dumps(pairs))

@app.route('/schedule', methods=["POST"])
def schedule():
    pairs = json.loads(request.form["pairs"])
    schedule_class().schedule(pairs)
    return render_template("schedule.html")

if __name__ == "__main__":
    app.run(debug=True)
