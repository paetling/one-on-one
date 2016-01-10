from unittest import TestCase
from one_on_one.group import GCGroup

class TestGCGroup(TestCase):
    def test_get(self):
        gc_group = GCGroup()
        gc_group.GC_URL = 'https://web.archive.org/web/20150319083649/https://gc.com/team'
        expected_group = {'BUSINESS DEV & PARTNERSHIPS': ['Jeff Kamrath'],
                          'MARKETING': ['Sean Wheeler',
                                        'Spencer Wright',
                                        'Kyleigh Callender',
                                        'Wellington Smith',
                                        'David Kennedy',
                                        'Crawford Roark',
                                        'Joe Yevoli',
                                        'Grace Mashore',
                                        'Sasha Herman',
                                        'Maura Cheeks'],
                          'TALENT OPS': ['Ursula Lopez-Palm',
                                         'Jenny Trumbull',
                                         'Amanda Ross'],
                          'TEST & RELEASE': ['Eric Han',
                                             'Joe Vacca',
                                             'Peter Spiewak'],
                          'PRODUCT MANAGEMENT': ['Abhinav Suraiya'],
                          'DESIGNERS': ['Wai-Jee Ho',
                                        'Keith Esernio',
                                        'Briana Czubkowski',
                                        'Ronni Tan',
                                        'Kelly Helfrich',
                                        'Tom Mudgett',
                                        'Ryan Welch'],
                          'ENGINEERS': ['Jerry Hsu',
                                        'Ben Yelsey',
                                        'Travis Thieman',
                                        'Tom Leach',
                                        'Brian Bernberg',
                                        'Nick Schultz',
                                        'Scott Morse',
                                        'Alex Etling',
                                        'Eduardo Arenas',
                                        'Gabriel Khaselev',
                                        'Zach Markin',
                                        'Harris Osserman',
                                        'Rohi Bagaria',
                                        'Anatoly Shikolay',
                                        'Erik Taubeneck',
                                        'Kristian Kristensen',
                                        'Jordan Singleton']}

        self.assertEquals(gc_group.get(), expected_group)
