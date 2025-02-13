import asyncio
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SpreadsheetContainer:
    def __init__(self):
        self.client = None

    async def start(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)
        self.client = gspread.authorize(creds)
        await self.update_spreadsheet()

    async def update_spreadsheet(self):
        while True:
            # Implementar lógica para atualizar a planilha
            await asyncio.sleep(60)  # Atualiza a cada minuto

    async def add_bet(self, bet_info):
        sheet = self.client.open("Apostas").sheet1
        await sheet.append_row([bet_info['date'], bet_info['amount'], bet_info['odds']])