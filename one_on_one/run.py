from datetime import datetime
from group import GCGroup
from pair import GCPair
from schedule import GCSchedule


group = GCGroup()
pair = GCPair()
schedule = GCSchedule()


group_dict = group.get()
print group_dict

pairs = pair.get_pairs_not_your_group(group_dict)
print pairs

test_pairs = [('Alex Etling', 'Ursula Lopez-Palm')]
schedule.schedule(test_pairs)

schedule.schedule(test_pairs, meeting_dt=datetime.now())
