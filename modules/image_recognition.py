import cv2
import pytesseract
from config import settings

pytesseract.pytesseract.tesseract_cmd = settings.TESSERACT_CMD

def process_aposta(aposta):
    # Carrega a imagem
    img = cv2.imread(aposta['image_path'])
    
    # Pré-processamento da imagem
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Mais pré-processamento pode ser adicionado aqui
    
    # Reconhecimento de texto
    dados = pytesseract.image_to_string(gray)
    
    # Processa os dados extraídos para o formato desejado
    # Exemplo de processamento
    dados_aposta = {
        'time': 'Time A vs Time B',
        'odds': '1.5',
        'valor': '100',
        'horario': '2025-02-07 18:00:00'  # Exemplo de horário de término da aposta
    }
    return dados_aposta