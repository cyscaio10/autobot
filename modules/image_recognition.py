import cv2
import pytesseract
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageRecognition:
    def __init__(self, max_workers=2):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def process_aposta(self, aposta):
        """
        Processa a imagem da aposta e retorna os dados extraídos.
        'aposta' deve ser um dicionário com a chave 'image_path'.
        """
        try:
            img = cv2.imread(aposta['image_path'])
            if img is None:
                raise ValueError("Imagem não pôde ser carregada. Verifique o caminho informado: {}"
                                 .format(aposta['image_path']))
            # Pré-processamento
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            processed = cv2.adaptiveThreshold(gray, 255,
                                              cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)
            # Realiza OCR com suporte a inglês e português
            extracted_text = pytesseract.image_to_string(processed, lang='eng+por')
            dados_aposta = self.extract_data(extracted_text)
            logger.info(f"Processamento concluído para: {aposta['image_path']}")
            return dados_aposta
        except Exception as e:
            logger.error(f"Erro no processamento da imagem {aposta.get('image_path', '')}: {e}")
            return None

    def extract_data(self, text):
        """
        Extrai informações relevantes do texto obtido pelo OCR.
        Retorna um dicionário com time, odds, valor e horário.
        """
        return {
            'time': self.extract_team(text),
            'odds': self.extract_odds(text),
            'valor': self.extract_valor(text),
            'horario': self.extract_horario(text)
        }

    def extract_team(self, text):
        match = re.search(r'(\w+\s?)+\s+vs\s+(\w+\s?)+', text, re.IGNORECASE)
        return match.group(0) if match else "Não identificado"

    def extract_odds(self, text):
        match = re.search(r'(\d+[\.,]\d+)', text)
        return match.group(0).replace(',', '.') if match else "N/A"

    def extract_valor(self, text):
        match = re.search(r'[\$R]\s?[\d,\.]+', text)
        return match.group(0) if match else "N/A"

    def extract_horario(self, text):
        match = re.search(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}', text)
        return match.group(0) if match else "Horário não identificado"

    def process_aposta_concurrent(self, aposta):
        return self.executor.submit(self.process_aposta, aposta)

    def shutdown(self):
        self.executor.shutdown(wait=True)

if __name__ == '__main__':
    # Teste simples: certifique-se de que os arquivos de teste existam.
    ir = ImageRecognition(max_workers=2)
    apostas = [
        {'image_path': 'tests/test_image1.jpg'},
        {'image_path': 'tests/test_image2.jpg'},
    ]
    futures = [ir.process_aposta_concurrent(aposta) for aposta in apostas]
    for future in futures:
        resultado = future.result()
        print("Resultado:", resultado)
    ir.shutdown()