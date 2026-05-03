import gspread
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/spreadsheets',]
creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
client = gspread.authorize(creds)

sheet_id = '1YZ3u9X4f0iZaKjluteKi9lUcRY9diTjQUiyi_ZH5AvY'
sheet = client.open_by_key(sheet_id)

