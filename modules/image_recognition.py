import cv2
import pytesseract
from PIL import Image
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

class ImageRecognition:
    def __init__(self):
        """
        Inicializa o sistema de reconhecimento de imagem.
        """
        # Configurar o Tesseract (ajuste o caminho conforme necessário)
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        self.model = self.load_model()

    def load_model(self):
        """
        Carrega o modelo de aprendizado de máquina treinado.
        """
        try:
            model = joblib.load('bet_recognition_model.pkl')
            return model
        except FileNotFoundError:
            return None

    def train_model(self, texts, labels):
        """
        Treina o modelo de reconhecimento de apostas.
        """
        vectorizer = CountVectorizer()
        X_train = vectorizer.fit_transform(texts)
        model = MultinomialNB()
        model.fit(X_train, labels)
        joblib.dump(model, 'bet_recognition_model.pkl')
        joblib.dump(vectorizer, 'vectorizer.pkl')
        self.model = model

    def process_image(self, image_path):
        """
        Processa uma imagem e extrai informações de aposta.
        """
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        text = pytesseract.image_to_string(thresh)
        bet_info = self.extract_bet_info(text)

        return bet_info

    def extract_bet_info(self, text):
        """
        Extrai informações de aposta do texto reconhecido.
        """
        if self.model:
            vectorizer = joblib.load('vectorizer.pkl')
            X = vectorizer.transform([text])
            prediction = self.model.predict(X)
            bet_info = {
                'type': prediction[0],
                'events': [],
                'odds': [],
                'stake': 0
            }
        else:
            bet_info = {
                'type': 'unknown',
                'events': [],
                'odds': [],
                'stake': 0
            }

        lines = text.split('\n')
        for line in lines:
            if 'Aposta Simples' in line:
                bet_info['type'] = 'single'
            elif 'Aposta Múltipla' in line:
                bet_info['type'] = 'multiple'
            elif 'vs' in line:
                bet_info['events'].append(line.strip())
            elif 'Odd:' in line:
                odds = line.split(':')[1].strip()
                bet_info['odds'].append(float(odds))
            elif 'Valor da Aposta:' in line:
                stake = line.split(':')[1].strip()
                bet_info['stake'] = float(stake)

        return bet_info