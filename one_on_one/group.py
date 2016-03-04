from lxml import html
import requests

class Group(object):
    def get(self):
        """
            This class should be subclassed with each subclass implementing
            this method. This method returns a dictionary where keys
            are group names and the values are lists of people
        """
        raise NotImplementedError

class GCGroup(Group):
    BLACK_LIST = ['Tom Leach', 'Patricia Wintermuth', 'Spencer Wright', 'Sean Wheeler']
    GC_URL = 'https://gc.com/team'

    def get(self):
        """
            This method does a simply web scrape of GC_URL with an attempt to grab each employee at
            GameChanger's name
        """
        return_dict = {}
        page = requests.get(self.GC_URL)
        html_element = html.fromstring(page.content)
        groups = html_element.find_class('plm')
        employee_groups = html_element.find_class('pls')

        for i,group in enumerate(groups):
            group_name = group.text_content().strip()
            if group_name != 'CUSTOMER SUPPORT':
                return_dict[group.text_content().strip()] = []
                employee_group = employee_groups[i]
                for employee in employee_group.find_class('yui3-u-1-5'):
                    links = list(employee.iterlinks())
                    name = links[1][0].text_content().strip()
                    if name not in self.BLACK_LIST:
                        return_dict[group.text_content().strip()].append(name)
        return return_dict
