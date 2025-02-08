import unittest
from modules import google_sheets

class TestGoogleSheets(unittest.TestCase):
    def test_update_sheet(self):
        dados_aposta = {'time': 'Time A vs Time B', 'odds': '1.5', 'valor': '100', 'horario': '2025-02-07 18:00:00'}
        result = google_sheets.update_sheet(dados_aposta)
        self.assertIsNotNone(result)

    def test_read_sheet(self):
        values = google_sheets.read_sheet('A1:D1')
        self.assertIsInstance(values, list)

if __name__ == '__main__':
    unittest.main()