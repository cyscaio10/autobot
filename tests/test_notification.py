import unittest
from modules import notification

class TestNotification(unittest.TestCase):
    def test_notify_operator(self):
        dados_aposta = {'time': 'Time A vs Time B', 'odds': '1.5', 'valor': '100'}
        notification.notify_operator(dados_aposta)
        # Adicione verificações de assertivas conforme necessário

if __name__ == '__main__':
    unittest.main()