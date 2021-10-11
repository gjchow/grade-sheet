from __future__ import print_function
import os.path
from typing import List

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def spreadsheet(data, courses):
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

    # spreadsheet_id = create_spreadsheet(service)

    spreadsheet_id = ''
    entries = 0
    repeat_entries = 0
    repeat_courses = 0
    start_col = num_to_col((courses*4)+1)
    repeat_col = num_to_col((repeat_courses*2)+1)
    values = []
    repeated_values = []
    name = data.pop(0)[0]
    values.extend(title(name))
    for entry in data:
        if len(entry) == 2:
            values.append(single_entry(entry[0], int(entry[1])))
            entries += 1
        elif len(entry) == 3:
            weights = entry[1].split()
            values.extend(weighted_repeated(entry[0], int(entry[2]), weights, entries, courses * 4))
            entries += int(entry[2])
        elif len(entry) == 4:
            enter = repeated_entry(entry[0], int(entry[1]), int(entry[2]), int(entry[3]), repeat_entries, repeat_courses * 2)
            entries += 1
            repeat_entries += int(entry[2])
            values.append(enter[0])
            for entry_name in enter[1]:
                repeated_values.append([entry_name])


    if len(values) > 3:
        start = f'{num_to_col((courses*4)+2)}3'
        end = f'{num_to_col((courses*4)+3)}{entries+2}'
        values[2].extend(add_result(start, end))
        body = {
            'values': values
        }
        repeat_body = {
            'values': repeated_values
        }
        request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=f"{start_col}1:100",
                                                     valueInputOption='USER_ENTERED', body=body)
        result = request.execute()
        courses += 1
        if len(repeated_values) > 0:
            repeated_values.insert(0, [name])
            request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                             range=f"Repeated!{repeat_col}1:100",
                                                             valueInputOption='USER_ENTERED', body=repeat_body)
            result = request.execute()
            repeat_courses += 1
    print("Done")


def create_spreadsheet(service):
    spreadsheet = {
        'properties': {
            'title': 'GradeSheet'
        },
        'sheets': [
            {
                'properties': {
                    'title': 'Grades',
                    'sheetId': 0,
                    'sheetType': 'GRID',
                    'gridProperties': {
                        'frozenRowCount': 2
                    }
                }
            },
            {
                'properties': {
                    'title': 'Repeated',
                    'sheetId': 1,
                    'sheetType': 'GRID',
                    'gridProperties': {
                        'frozenRowCount': 1
                    }
                }
            },
        ]
    }
    request = service.spreadsheets().create(body=spreadsheet)
    response = request.execute()
    spreadsheet_id = response.get('spreadsheetId')
    return spreadsheet_id


def title(course: str) -> List[List[str]]:
    values = [[course.upper()], ['Name', 'Percentage', 'Mark', 'Result']]
    return values


def add_result(start: str, end: str) -> List[str]:
    values = [f'=SUM(ARRAYFORMULA({start}:{start[0]}{end[1]}*{end[0]}{start[1]}:{end}))']
    return values


def single_entry(name: str, percentage: int) -> List[str]:
    values = [name, percentage, '']
    print('Added 1 single entry')
    return values


def repeated_entry(name: str, percentage: int, num: int, taken: int, row: int, num_col: int) -> List[List[str]]:
    col = num_to_col(num_col + 2)
    start = f'{col}{row + 2}'
    end = f'{col}{row + 2 + num}'
    formula = f"=SUM(SORTN('Repeated'!{start}:{end},{taken},0))/{taken}"
    names = []
    for i in range(num):
        names.append(f'{name}{i + 1}')
    values = [[name, percentage, formula], names]
    print(f'Added {num} repeated entries')
    return values


def weighted_repeated(name: str, num: int, weights: List[int], row: int, num_col: int) -> List[List[str]]:
    weights.sort(reverse=True)
    values = []
    col = num_to_col(num_col + 3)
    for i in range(num):
        start = row + 3
        curr = row + 3 + i
        end = row + 3 + num - 1
        formula = f'=SWITCH(IFERROR(RANK({col}{curr}, {col}{start}:{col}{end})+COUNTIF({col}{curr}:{col}{end}, ' \
                  f'{col}{curr})-1, COUNTBLANK({col}{curr}:{col}{end})+COUNTIF({col}{start}: {col}{end}, ">0")), '
        for j in range(len(weights)):
            formula += f'{j+1}, {weights[j]}, '
        formula += '0)'
        values.append([f'{name}{i+1}', formula, ''])
    print(f'Added {num} weighted entries')
    return values


def num_to_col(num: int):
    if num <= 26:
        return chr(num + 64)
    else:
        return num_to_col(num // 26) + num_to_col(num % 26)
