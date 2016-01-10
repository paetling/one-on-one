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

    def test_get_group_key_with_most_people_1(self):
        group_dict = {'engineers': ['guy1', 'girl1', 'guy2'],
                      'design': ['girl2', 'guy3'],
                      'marketing': ['girl3']}
        self.assertEquals('engineers', self.gc_pair.get_group_key_with_most_people(group_dict))

    def test_get_group_key_with_most_people_2(self):
        group_dict = {'engineers': ['guy1', 'girl1', 'guy2'],
                      'design': ['girl2', 'guy3'],
                      'marketing': ['girl3', 'guy4', 'girl4', 'guy5']}
        self.assertEquals('marketing', self.gc_pair.get_group_key_with_most_people(group_dict))

    def test_get_group_key_with_most_people_3(self):
        group_dict = {'engineers': ['guy1', 'girl1', 'guy2'],
                      'design': ['girl2', 'guy3', 'guy3'],
                      'marketing': ['girl3']}
        self.assertIn(self.gc_pair.get_group_key_with_most_people(group_dict), ['engineers', 'design'])

    def test_get_group_key_with_most_people_4(self):
        group_dict = {}
        self.assertEquals('', self.gc_pair.get_group_key_with_most_people(group_dict))

    def test_total_people_1(self):
        group_dict = {'engineers': ['guy1', 'girl1', 'guy2'],
                      'design': ['girl2', 'guy3'],
                      'marketing': ['girl3']}
        self.assertEquals(6, self.gc_pair.total_people(group_dict))

    def test_total_people_2(self):
        group_dict = {}
        self.assertEquals(0, self.gc_pair.total_people(group_dict))

    def test_remove_all_empty_groups(self):
        group_dict = {'engineers': ['guy1', 'girl1', 'guy2'],
                      'design': ['girl2', 'guy3'],
                      'marketing': []}
        self.assertEquals(sorted(['engineers', 'design', 'marketing']), sorted(group_dict.keys()))

        self.gc_pair.remove_all_empty_groups(group_dict)
        self.assertEquals(sorted(['engineers', 'design']), sorted(group_dict.keys()))

        group_dict['design'] = []
        self.gc_pair.remove_all_empty_groups(group_dict)
        self.assertEquals(['engineers'], group_dict.keys())

        group_dict['engineers'] = []
        self.gc_pair.remove_all_empty_groups(group_dict)
        self.assertEquals([], group_dict.keys())



