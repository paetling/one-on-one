from group import GCGroup
from pair import GCPair


group = GCGroup()
pair = GCPair()


group_dict = group.get()
print group_dict

pairs = pair.get_pairs(group_dict)
print pairs


