```python
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
import pickle
import os.path

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('calendar', 'v3', credentials=creds)

def create_event(service, start_time_str, end_time_str, summary, description=None, location=None):
    start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%dT%H:%M:%S")
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'America/Los_Angeles',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return service.events().insert(calendarId='primary', body=event).execute()

def send_calendar_invite(start_time_str, end_time_str, summary, description=None, location=None):
    service = authenticate_google_calendar()
    event = create_event(service, start_time_str, end_time_str, summary, description, location)
    print(f'Event created: {event.get("htmlLink")}')
```
