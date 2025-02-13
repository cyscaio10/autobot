import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SheetProcessor:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open("Nome da Sua Planilha").sheet1


    def add_bet(self, bet_info):
        row = [
            self.get_next_id(),
            bet_info['date'],
            bet_info['group_name'],
            bet_info['time'],
            len(bet_info['games']),
            bet_info['bet_amount'],
            bet_info['total_odds'],
            'Em andamento',
            self.generate_summary(bet_info)
        ]
        self.sheet.append_row(row)

    def generate_summary(self, bet_info):
        summary = []
        for game in bet_info['games']:
            summary.append(f"{game['team1']} vs {game['team2']} - {game['condition']}")
        return ", ".join(summary[:3]) + ("..." if len(bet_info['games']) > 3 else "")

    def get_next_id(self):
        return len(self.sheet.get_all_values()) + 1

    def update_bet_result(self, bet_id, result):
        cell = self.sheet.find(str(bet_id))
        self.sheet.update_cell(cell.row, 8, result)  # Assumindo que a coluna de resultado é a 8ª

    # ... (outros métodos necessários) ...
