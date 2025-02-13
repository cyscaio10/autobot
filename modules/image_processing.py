import cv2
import pytesseract

class ImageProcessor:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract_executable'

    def process_bet_image(self, image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)

        # Implementar lógica para extrair informações relevantes do texto
        bet_info = self.extract_bet_info(text)
        return bet_info

    def extract_bet_info(self, text):
        # Implementar lógica para extrair informações da aposta do texto
        # Exemplo simplificado:
        lines = text.split('\n')
        bet_info = {}
        for line in lines:
            if "Time:" in line:
                bet_info['time'] = line.split("Time:")[1].strip()
            elif "Odd:" in line:
                bet_info['odd'] = line.split("Odd:")[1].strip()
            elif "Valor:" in line:
                bet_info['valor'] = line.split("Valor:")[1].strip()
        return bet_info
