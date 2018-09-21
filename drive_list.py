from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1ZH-JVx8LL09L0stBu2RBF-zi1ElqOtQapWFQAQBDvnc'
SAMPLE_RANGE_NAME = 'Class Data!A2:B3'
"""
def sendEmails() :
  sheet = SpreadsheetApp.getActiveSheet()
  startRow = 2 
  numRows = 2 
  dataRange = sheet.getRange(startRow, 1, numRows, 2)
  # Fetch values for each row in the Range.
  data = dataRange.getValues()
  for (i in data):
    row = data[i]
    emailAddress = row[0]  ' First column
    expDate = row[1] 'Second column
    name = row[2]
    subject = 'Sending emails from a Spreadsheet'
    message = name + 'Your certificate expires on ' + expDate
    MailApp.sendEmail(emailAddress, subject, message)

"""

def main():
  """Shows basic usage of the Sheets API>
  Prints values from a sample spreadsheet.
  """
  store = file.Storage('token.json')
  creds = store.get()
  if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
    creds = tools.run_flow(flow, store)
  service = discovery.build('sheets', 'v4', http=creds.authorize(Http()))

  # Call the Sheets API
  SPREADSHEET_ID = '1ZH-JVx8LL09L0stBu2RBF-zi1ElqOtQapWFQAQBDvnc'
  RANGE_NAME = 'Class Data!A2:B3'
  result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
  values = result.get('values', [])
  if not values:
    print('No data found.')
  else:
    print('Results:')
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      emal = row[0]
      expdate = row[1]
      print(emal, expdate)

if __name__ == '__main__':
    main()



#https://developers.google.com/drive/api/v2/reference/files/get


 
