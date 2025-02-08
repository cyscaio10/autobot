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

if __name__ == '__main__':
    unittest.main()