from unittest import TestCase
from one_on_one.pair import GCPair

class TestGCGroup(TestCase):
    def setUp(self):
        self.gc_pair = GCPair()

    def test_random_from_group(self):
        group_dict = {'engineers': ['girl1'],
                      'marketing': ['guy1'],
                      'design': ['girl2']}
        self.assertEquals(1, len(group_dict['engineers']))
        self.assertEquals(1, len(group_dict['design']))
        self.assertEquals(1, len(group_dict['marketing']))

        for i in range(3):
            person = self.gc_pair.random_from_group_dict(group_dict)

        self.assertEquals(0, len(group_dict['engineers']))
        self.assertEquals(0, len(group_dict['design']))
        self.assertEquals(0, len(group_dict['marketing']))

    def test_random_from_group_exclude_group_crash(self):
        group_dict = {'engineers': ['girl'],
                      'marketing': ['guy']}
        with self.assertRaises(Exception):
            self.gc_pair.random_from_group_dict(group_dict, exclude_groups=['engineers', 'marketing'])

    def test_random_from_group_exclude_people_crash(self):
        group_dict = {'engineers': ['girl'],
                      'marketing': ['guy']}
        with self.assertRaises(Exception):
            self.gc_pair.random_from_group_dict(group_dict, exclude_people=['guy', 'girl'])

    def test_random_from_group_kwargs(self):
        group_dict = {'engineers': ['guy1', 'girl1', 'guy2'],
                      'design': ['girl2', 'guy3'],
                      'marketing': ['girl3']}
        self.assertEquals(3, len(group_dict['engineers']))
        self.assertEquals(2, len(group_dict['design']))
        self.assertEquals(1, len(group_dict['marketing']))

        self.assertEquals(self.gc_pair.random_from_group_dict(group_dict, exclude_people=['guy1',
                                                                                          'girl1',
                                                                                          'guy2',
                                                                                          'guy3',
                                                                                          'girl3']),
                          'girl2')
        self.assertEquals(1, len(group_dict['design']))

        self.assertEquals(self.gc_pair.random_from_group_dict(group_dict, exclude_people=['guy1',
                                                                                          'girl1',
                                                                                          'guy2',
                                                                                          'girl3']),
                          'guy3')
        self.assertEquals(0, len(group_dict['design']))

        self.assertEquals(self.gc_pair.random_from_group_dict(group_dict, exclude_groups=['engineers', 'design']),
                          'girl3')
        self.assertEquals(0, len(group_dict['marketing']))


