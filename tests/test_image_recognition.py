import unittest
from modules import image_recognition

class TestImageRecognition(unittest.TestCase):
    def test_process_aposta(self):
        aposta = {'image_path': 'tests/test_image.jpg'}
        dados_aposta = image_recognition.process_aposta(aposta)
        self.assertIn('time', dados_aposta)
        self.assertIn('odds', dados_aposta)
        self.assertIn('valor', dados_aposta)
        self.assertIn('horario', dados_aposta)
        self.assertEqual(dados_aposta['time'], 'expected_time')
        self.assertEqual(dados_aposta['odds'], 'expected_odds')
        self.assertEqual(dados_aposta['valor'], 'expected_valor')
        self.assertEqual(dados_aposta['horario'], 'expected_horario')

if __name__ == '__main__':
    unittest.main()