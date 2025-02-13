import numpy as np
from sklearn.ensemble import RandomForestClassifier
import requests
from bs4 import BeautifulSoup
import cv2

class MiniAI:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.data = []
        self.labels = []
        self.betting_types = {}
        self.layout_patterns = {}

    async def learn_from_bet(self, bet_info, result):
        features = await self.extract_features(bet_info)
        self.data.append(features)
        self.labels.append(1 if result['won'] else 0)

        if len(self.data) >= 100:
            await self.train_model()

    async def extract_features(self, bet_info):
        return [
            len(bet_info['events']),
            np.mean(bet_info['odds']),
            bet_info['stake'],
            self.betting_types.get(bet_info['type'], 0)
        ]

    async def train_model(self):
        X = np.array(self.data)
        y = np.array(self.labels)
        self.model.fit(X, y)

    # ... outros métodos ...
