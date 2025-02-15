import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SpreadsheetManager:
    def __init__(self, credentials_file, spreadsheet_id):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_key(spreadsheet_id).sheet1

    def append_row(self, data):
        self.sheet.append_row(data)

    def get_all_records(self):
        return self.sheet.get_all_records()

    def update_cell(self, row, col, value):
        self.sheet.update_cell(row, col, value)

    def find_cell(self, value):
        return self.sheet.find(value)