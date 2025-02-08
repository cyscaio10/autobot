import unittest
from modules import state_management

class TestStateManagement(unittest.TestCase):
    def test_init_state(self):
        state_management.init_state()
        # Verifique se o arquivo de estado foi criado corretamente

    def test_get_next_aposta(self):
        aposta = state_management.get_next_aposta()
        self.assertIsNotNone(aposta)

if __name__ == '__main__':
    unittest.main()