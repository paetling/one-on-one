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
    GC_URL = 'https://gc.com/team'

    def get(self):
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
                    name_link = links[1][0]
                    return_dict[group.text_content().strip()].append(name_link.text_content().strip())
        return return_dict
