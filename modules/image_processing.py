import cv2
import numpy as np
import pytesseract

class ImageProcessor:
    @staticmethod
    def preprocess_image(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        denoised = cv2.fastNlMeansDenoising(gray)
        threshold = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return threshold

    @staticmethod
    def extract_text(image):
        preprocessed = ImageProcessor.preprocess_image(image)
        text = pytesseract.image_to_string(preprocessed)
        return text

    @staticmethod
    def find_bet_info(image):
        text = ImageProcessor.extract_text(image)
        # Implementar lógica para extrair informações de apostas do texto
        # Retornar um dicionário com as informações extraídas
        return {}
