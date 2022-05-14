from __future__ import print_function
import os.path
from typing import List

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
import Config
from models.score_row import ScoreRow

SCOPES = ['https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = Config.WordleConfig.SHEETS_SPREADSHEET_ID
SAMPLE_RANGE_NAME = Config.WordleConfig.SHEET_AND_CELL_RANGE

"""Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


def update(score_rows: List[ScoreRow]):
    body = {
        "values":
            [score_row.to_array() for score_row in score_rows]
    }
    return sheet.values().update(spreadsheetId=SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_NAME, valueInputOption='USER_ENTERED', body=body).execute()



if __name__ == '__main__':
    # print(update("today", "1", "2", "3", "4", "5"))
    pass