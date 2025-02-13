import unittest
from modules import state_management
import os
import json

class TestStateManagement(unittest.TestCase):
    def test_init_state(self):
        state_management.init_state()
        self.assertTrue(os.path.exists(state_management.STATE_FILE))
        with open(state_management.STATE_FILE, 'r') as f:
            state = json.load(f)
        self.assertIn('last_processed', state)
        self.assertIn('errors', state)
        self.assertIn('conference_times', state)

    def test_get_next_aposta(self):
        aposta = state_management.get_next_aposta()
        self.assertIsNotNone(aposta)

if __name__ == '__main__':
    unittest.main()