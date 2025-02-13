import json
from datetime import datetime, timedelta

class BetProcessor:
    def __init__(self):
        self.load_sport_configs()
        self.load_bet_types()

    def load_sport_configs(self):
        with open('sport_configs.json', 'r') as f:
            self.sport_configs = json.load(f)

    def load_bet_types(self):
        with open('bet_types.json', 'r') as f:
            self.bet_types = json.load(f)

    def process_bet(self, bet_info):
        """
        Processa uma aposta com base nas informações fornecidas.
        """
        if not self.validate_bet(bet_info):
            return False, "Aposta inválida"

        bet_type = bet_info['bet_type']
        if bet_type not in self.bet_types:
            return False, f"Tipo de aposta não reconhecido: {bet_type}"

        processor = getattr(self, f"process_{bet_type}", None)
        if processor:
            return processor(bet_info)
        else:
            return False, f"Processador não implementado para o tipo de aposta: {bet_type}"

    def validate_bet(self, bet_info):
        """
        Valida as informações básicas da aposta.
        """
        required_fields = ['sport', 'bet_type', 'stake', 'odds']
        return all(field in bet_info for field in required_fields)

    def process_single(self, bet_info):
        """
        Processa uma aposta simples.
        """
        sport = bet_info['sport']
        odds = bet_info['odds']
        stake = bet_info['stake']

        if sport not in self.sport_configs:
            return False, f"Esporte não configurado: {sport}"

        config = self.sport_configs[sport]
        if odds < config['min_odds'] or odds > config['max_odds']:
            return False, f"Odds fora do intervalo permitido para {sport}"

        potential_return = stake * odds
        return True, {
            "type": "single",
            "stake": stake,
            "potential_return": potential_return,
            "expected_end_time": self.calculate_end_time(bet_info)
        }

    def process_multiple(self, bet_info):
        """
        Processa uma aposta múltipla.
        """
        if 'selections' not in bet_info or len(bet_info['selections']) < 2:
            return False, "Aposta múltipla deve ter pelo menos duas seleções"

        total_odds = 1
        for selection in bet_info['selections']:
            if not self.validate_bet(selection):
                return False, f"Seleção inválida: {selection}"
            total_odds *= selection['odds']

        stake = bet_info['stake']
        potential_return = stake * total_odds

        return True, {
            "type": "multiple",
            "stake": stake,
            "total_odds": total_odds,
            "potential_return": potential_return,
            "expected_end_time": self.calculate_end_time(bet_info)
        }

    def process_system(self, bet_info):
        """
        Processa uma aposta sistema.
        """
        if 'selections' not in bet_info or 'system' not in bet_info:
            return False, "Informações insuficientes para aposta sistema"

        selections = bet_info['selections']
        system = bet_info['system']
        stake = bet_info['stake']

        if len(selections) < system:
            return False, f"Número insuficiente de seleções para sistema {system}"

        # Cálculo simplificado - na prática, isso seria mais complexo
        combinations = self.calculate_combinations(len(selections), system)
        potential_return = stake * combinations * max(selection['odds'] for selection in selections)

        return True, {
            "type": "system",
            "stake": stake,
            "system": system,
            "potential_return": potential_return,
            "expected_end_time": self.calculate_end_time(bet_info)
        }

    def calculate_end_time(self, bet_info):
        """
        Calcula o tempo esperado de término da aposta.
        """
        sport = bet_info['sport']
        start_time = datetime.now()
        duration = timedelta(minutes=self.sport_configs[sport]['duration'])
        return start_time + duration

    def calculate_combinations(self, n, r):
        """
        Calcula o número de combinações de n elementos tomados r a r.
        """
        from math import factorial
        return factorial(n) // (factorial(r) * factorial(n - r))
