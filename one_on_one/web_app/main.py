import json
from flask import Flask, render_template, request
import arrow

from one_on_one.group import GCGroup
from one_on_one.pair import GCPair
from one_on_one.schedule import GCSchedule

group_instance = GCGroup()
pair_instance = GCPair()
schedule_instance = GCSchedule()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/people')
def people():
    group = group_instance.get()
    return render_template("people.html", group=group, group_string=json.dumps(group))

@app.route('/pairs', methods=["POST"])
def pairs():
    group = json.loads(request.form["group"])
    exclude_list_string = request.form["exclude_list"].rstrip('\n\t ')
    exclude_list = map(lambda input: input.strip(), exclude_list_string.split(',') if exclude_list_string else [])\

    pairs = pair_instance.get_pairs(group, exclude_list=exclude_list)
    return render_template("pairs.html", pairs=pairs, pairs_string=json.dumps(pairs))

@app.route('/schedule', methods=["POST"])
def schedule():
    pairs = json.loads(request.form["pairs"])
    meeting_date_string = request.form["meeting_date"]
    meeting_dt = arrow.get(meeting_date_string).datetime if meeting_date_string else None

    schedule_instance.schedule(pairs, meeting_dt=meeting_dt)
    return render_template("schedule.html")

if __name__ == "__main__":
    app.run(port=80)
