The goal of this project was to provide a basic tool for scheduling One on Ones at a company.
The project has three key classes, all of which should be subclassed:
    Group: The group class returns a dictionary of {'GroupName': [group_list, ...]}
    Pair: Takes in the dictionary output by Group and returns a list pairs of people [(Person1, Person2), ...]
    Schedule: Takes in a list of pairs and schedules meetings for those pairs. Scheduling meetings can be whatever is needed for your company

I have implemented 1 subclass for each class type to be use at [GameChanger](gc.com)

I hope to still add a web interface for accessing and using these classes and their methods.
