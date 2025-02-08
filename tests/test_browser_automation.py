import unittest
from modules import browser_automation

class TestBrowserAutomation(unittest.TestCase):
    def test_check_aposta(self):
        dados_aposta = {'time': 'Time A vs Time B', 'odds': '1.5', 'valor': '100'}
        browser_automation.check_aposta(dados_aposta)
        # Adicione verificações de assertivas conforme necessário

if __name__ == '__main__':
    unittest.main()