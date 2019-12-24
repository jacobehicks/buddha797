import gspread
import sys
import os
from oauth2client.service_account import ServiceAccountCredentials

print("Current Working Directory: " + sys.path[0])
print("Getting Credentials From: " + os.path.join(sys.path[0], "credentials.json"))

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(sys.path[0], "credentials.json"), scope)
client = gspread.authorize(creds)



sheet = client.open('Under The Golden Dome Database').sheet1

telemedicine = sheet.get_all_records()
print(telemedicine)