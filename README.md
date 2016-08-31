### The Goal
The goal of this project was to provide a basic tool for scheduling One on Ones at a company.

### Code Structure / Program Pieces
The project has three key classes, all of which should be subclassed:
* Group: The group class returns a dictionary of {'GroupName': [group_list, ...]}
* Pair: Takes in the dictionary output by Group and returns a list pairs of people [(Person1, Person2), ...]
* Schedule: Takes in a list of pairs and schedules meetings for those pairs. Scheduling meetings can be whatever is needed for your company

I have implemented 1 subclass for each class type to be use at [GameChanger](gc.com)

### Running and Testing Locally
Follow these steps to run and test locally
* Setup a virtualenv
* Run `source <name_of_virtualenv>/bin/activate`
* In this repo run `pip install -r requirements.txt; pip install -r test_requirements.txt`
* Run `export PYTHONPATH=$PYTHONPATH; python one_on_one/web_app/main.py`

Note: You might need to run the web app on a different port then 80. You can do this by setting the environment variable: `ONE_ON_ONE_PORT`
