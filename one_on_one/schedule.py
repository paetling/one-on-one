import httplib2
import datetime
import base64
from email.MIMEText import MIMEText

from oauth2client.client import SignedJwtAssertionCredentials
from apiclient import discovery

class Schedule(object):
    def schedule(self, pairs, no_pair=None, meeting_dt=None):
        """ This method is made to be overwritten by subclasses.
            It should take in a list of pairs, and schedule a meeting between
            the pairs of people
            no_pair is an optional argument which represents a person who did not have a pair
            meeting_dt is an optional datetime at which the meetings will start
        """
        raise NotImplementedError

class GCSchedule(Schedule):
    name_mappings = {'Jenny from the Lair': 'Jenny Trumbull'}
    keira_email = 'keira@gc.com'
    def get_credentials(self):
        client_email = 'one-on-one-account@windy-raceway-118617.iam.gserviceaccount.com'
        with open("ConvertedPrivateKey.pem") as f:
            private_key = f.read()
        credentials = SignedJwtAssertionCredentials(client_email,
                                                    private_key,
                                                    ['https://www.googleapis.com/auth/calendar',
                                                     'https://www.googleapis.com/auth/admin.directory.user.readonly',
                                                     'https://mail.google.com/'],
                                                     sub=self.keira_email)
        return credentials

    def get_real_name(self, full_name):
        if full_name in self.name_mappings:
            return self.name_mappings[full_name]
        return full_name

    @staticmethod
    def get_gc_email(directory_access, full_name):
        split_names = full_name.split(' ')
        first_name = split_names[0]
        last_name = split_names[1]

        #Hope to uniquely identify first
        for name in [full_name, last_name, first_name]:
            results = directory_access.users().list(customer='my_customer', query="name:{}".format(name)).execute()
            if len(results.get('users', [])) == 1:
                return results['users'][0]['emails'][0]['address']

        # If you cannot uniquely identify just grab the first email for that users name
        for name in [full_name, last_name, first_name]:
            results = directory_access.users().list(customer='my_customer', query="name:{}".format(name)).execute()
            if len(results.get('users', [])) > 1:
                return results['users'][0]['emails'][0]['address']
        raise KeyError("Cannot identify user from name: {}".format(full_name))

    def create_meeting(self, pair, meeting_start, meeting_end, calendar_access, directory_access):
        email_1 = self.get_gc_email(directory_access, self.get_real_name(pair[0]))
        email_2 = self.get_gc_email(directory_access, self.get_real_name(pair[1]))

        start_doc = {'timeZone': 'America/New_York', 'dateTime': meeting_start}
        end_doc = {'timeZone': 'America/New_York', 'dateTime': meeting_end}

        attendees = [{'email': email_1}, {'email': email_2}]

        body = {'attendees': attendees,
                'start': start_doc,
                'end': end_doc,
                'summary': 'Peer One on One: {} and {}'.format(pair[0], pair[1]),
                'description': 'This is a chance to meet and talk with someone else at GC. If you are not sure what to talk about, consult this link: http://jasonevanish.com/2014/05/29/101-questions-to-ask-in-1-on-1s/'}

        calendar_access.events().insert(calendarId='gamechanger.io_pvrnqe6amftma1ful6vou0ctmo@group.calendar.google.com',
                                        body=body,
                                        sendNotifications=True).execute()

    def send_no_meeting_email(self, user_name, mail_access, directory_access):
        user_email = self.get_gc_email(directory_access, self.get_real_name(user_name))
        message_text = "Hello {},\nThis week we had an odd number of people for peer one on ones.  That means one person did not get paired up with someone.  You happen to be that person this week. You should be paired up again next time!\n\nLet Jenny or Alex know if you have any questions.".format(user_name)
        message = MIMEText(message_text)
        message['to'] = user_email
        message['from'] = self.keira_email
        message['subject'] = "Peer One on Ones this week"
        encodeMessage = {'raw': base64.urlsafe_b64encode(message.as_string())}
        mail_access.users().messages().send(userId='me', body=encodeMessage).execute()

    def schedule(self, pairs, no_pair=None, meeting_dt=None):
        """
            This schedule function is built around Googles Api. Its goal is to schedule
            google calendar events for each set of pairs. To do this it uses the following
            api resources:
                Google Calendar: https://developers.google.com/google-apps/calendar/?hl=en
                Google Directory: https://developers.google.com/admin-sdk/directory/
            It also makes use of Google Service Accounts: https://developers.google.com/identity/protocols/OAuth2ServiceAccount
            If meeting_dt is not passed, assume that the meetings should be schedule a week from today at 10 a.m.
        """
        if meeting_dt is None:
            now = datetime.datetime.now()
            one_week_from_now = now + datetime.timedelta(7)
            meeting_start = datetime.datetime(one_week_from_now.year, one_week_from_now.month, one_week_from_now.day, 10, 30, 0).isoformat()
            meeting_end = datetime.datetime(one_week_from_now.year, one_week_from_now.month, one_week_from_now.day, 11, 0, 0).isoformat()
        else:
            dt_start = datetime.datetime(meeting_dt.year, meeting_dt.month, meeting_dt.day, meeting_dt.hour, meeting_dt.minute, meeting_dt.second)
            dt_end = datetime.datetime(meeting_dt.year, meeting_dt.month, meeting_dt.day, meeting_dt.hour, meeting_dt.minute, meeting_dt.second)
            meeting_start = dt_start.isoformat()
            meeting_end = dt_end.isoformat()
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        calendar_access = discovery.build('calendar', 'v3', http=http)
        directory_access = discovery.build('admin', 'directory_v1', http=http)
        mail_access = discovery.build('gmail', 'v1', http=http)
        for pair in pairs:
            self.create_meeting(pair, meeting_start, meeting_end, calendar_access, directory_access)
        if no_pair:
            self.send_no_meeting_email(no_pair, mail_access, directory_access)

