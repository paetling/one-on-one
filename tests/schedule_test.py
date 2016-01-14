from datetime import datetime

from unittest import TestCase
from mock import Mock, call, patch
from one_on_one.schedule  import GCSchedule

class TestGCSchedule(TestCase):
    def setUp(self):
        self.gc_schedule = GCSchedule()

    def test_get_gc_email(self):
        fake_directory_access = Mock()
        fake_directory_access.users().list().execute.return_value = {'users': []}

        with self.assertRaises(KeyError):
            self.gc_schedule.get_gc_email(fake_directory_access, 'Alex Etling')
        fake_directory_access.users().list.assert_has_calls([call(),
                                                             call(customer='my_customer', query="name:Alex Etling"),
                                                             call().execute(),
                                                             call(customer='my_customer', query="name:Etling"),
                                                             call().execute(),
                                                             call(customer='my_customer', query="name:Alex"),
                                                             call().execute()])

    def test_get_gc_email_no_type_error(self):
        fake_directory_access = Mock()
        fake_directory_access.users().list().execute.return_value = {}

        with self.assertRaises(KeyError):
            self.gc_schedule.get_gc_email(fake_directory_access, 'Alex Etling')
        fake_directory_access.users().list.assert_has_calls([call(),
                                                             call(customer='my_customer', query="name:Alex Etling"),
                                                             call().execute(),
                                                             call(customer='my_customer', query="name:Etling"),
                                                             call().execute(),
                                                             call(customer='my_customer', query="name:Alex"),
                                                             call().execute()])

    def test_create_meeting(self):
        fake_directory_access = Mock()
        fake_calendar_access = Mock()
        fake_get_gc_email = Mock()
        self.gc_schedule.get_gc_email = fake_get_gc_email

        fake_get_gc_email.side_effect = ["alex@gc.com", "bob@gc.com"]

        expected_body = {'attendees': [{'email': 'alex@gc.com'}, {'email': 'bob@gc.com'}],
                         'start': {'date': '2016-01-01', 'timezone': 'America/New_York', 'datetime': '2016-01-01 10:00:00'},
                         'end': {'date': '2016-01-01', 'timezone': 'America/New_York', 'datetime': '2016-01-01 10:30:00'},
                         'summary': 'Peer One on One: Alex Etling and Bob Notreal',
                         'description': 'This is a chance to meet and talk with someone else at GC. If you are not sure what to talk about, consult this link: http://jasonevanish.com/2014/05/29/101-questions-to-ask-in-1-on-1s/'}

        self.gc_schedule.create_meeting(('Alex Etling', 'Bob Notreal'),
                                        '2016-01-01 10:00:00',
                                        '2016-01-01 10:30:00',
                                        fake_calendar_access,
                                        fake_directory_access)
        fake_calendar_access.events().insert.assert_has_calls([call(calendarId='gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com',
                                                                    body=expected_body,
                                                                    sendNotifications=True),
                                                               call().execute()])



