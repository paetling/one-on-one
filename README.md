Want a GroupGetter class which has a get method which returns a dictionary groupName -> list of users

Want a randomizer class when passed a group returns back a list of pairs

want a schedule which takes a list of pairs and schedules an email with them

gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com




In [151]: start_doc = {'date': '2015-01-11', 'timezone': 'America/New_York', 'datetime': '2016-01-11 10:15:00'}

In [152]: alex = {'id': '117884301256921225253', 'email': 'alex@gc.com'}

In [153]: urs = {'id': '113860276892981950132', 'email': 'ursula@gc.com'}

In [154]: doc = {'creator': {'id': '108828400597329574792'}, 'attendees': [alex, urs], 'start': start_doc}

In [155]: doc = {'creator': {'id': '108828400597329574792'}, 'attendees': [alex, urs], 'start': start_doc}

In [156]: service1.events().insert(calendarId='gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com', body=doc, sendNotifications=True)
Out[156]: <googleapiclient.http.HttpRequest at 0x107623bd0>

In [157]: service1.events().insert(calendarId='gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com', body=doc, sendNotifications=True).execute()
---------------------------------------------------------------------------
HttpError                                 Traceback (most recent call last)
<ipython-input-157-53b86565fcaf> in <module>()
----> 1 service1.events().insert(calendarId='gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com', body=doc, sendNotifications=True).execute()

/Users/dayman/one-on-one/lib/python2.7/site-packages/oauth2client/util.pyc in positional_wrapper(*args, **kwargs)
    138                 elif positional_parameters_enforcement == POSITIONAL_WARNING:
    139                     logger.warning(message)
--> 140                 else:  # IGNORE
    141                     pass
    142             return wrapped(*args, **kwargs)

/Users/dayman/one-on-one/lib/python2.7/site-packages/googleapiclient/http.pyc in execute(self, http, num_retries)
    727       callback(resp)
    728     if resp.status >= 300:
--> 729       raise HttpError(resp, content, uri=self.uri)
    730     return self.postproc(resp, content)
    731

HttpError: <HttpError 400 when requesting https://www.googleapis.com/calendar/v3/calendars/gamechanger.io_8ag52p72ocos9b61g7tcdt98ds%40group.calendar.google.com/events?alt=json&sendNotifications=true returned "Missing end time.">

In [158]: end_doc = {'date': '2015-01-11', 'timezone': 'America/New_York', 'datetime': '2016-01-11 10:45:00'}

In [159]: doc = {'creator': {'id': '108828400597329574792'}, 'attendees': [alex, urs], 'start': start_doc, 'end': end_doc}

In [160]: service1.events().insert(calendarId='gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com', body=doc, sendNotifications=True).execute()
---------------------------------------------------------------------------
HttpError                                 Traceback (most recent call last)
<ipython-input-160-53b86565fcaf> in <module>()
----> 1 service1.events().insert(calendarId='gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com', body=doc, sendNotifications=True).execute()

/Users/dayman/one-on-one/lib/python2.7/site-packages/oauth2client/util.pyc in positional_wrapper(*args, **kwargs)
    138                 elif positional_parameters_enforcement == POSITIONAL_WARNING:
    139                     logger.warning(message)
--> 140                 else:  # IGNORE
    141                     pass
    142             return wrapped(*args, **kwargs)

/Users/dayman/one-on-one/lib/python2.7/site-packages/googleapiclient/http.pyc in execute(self, http, num_retries)
    727       callback(resp)
    728     if resp.status >= 300:
--> 729       raise HttpError(resp, content, uri=self.uri)
    730     return self.postproc(resp, content)
    731

HttpError: <HttpError 403 when requesting https://www.googleapis.com/calendar/v3/calendars/gamechanger.io_8ag52p72ocos9b61g7tcdt98ds%40group.calendar.google.com/events?alt=json&sendNotifications=true returned "Forbidden">

In [161]: doc = {'creator': {'id': '108828400597329574792'}, 'attendees': [alex, urs], 'start': start_doc, 'end': end_doc}
KeyboardInterrupt

In [161]: alex
Out[161]: {'email': 'alex@gc.com', 'id': '117884301256921225253'}

In [162]: doc = {'creator': {'id': '117884301256921225253'}, 'attendees': [alex, urs], 'start': start_doc, 'end': end_doc}

In [163]: service1.events().insert(calendarId='gamechanger.io_8ag52p72ocos9b61g7tcdt98ds@group.calendar.google.com', body=doc, sendNotifications=True).execute()




I have the right to add calendar events just not guests -- do not pass ids in attendees jsut pass emails
cannot set creator properly
