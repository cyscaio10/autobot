class SheetProcessor:
    def process_bet_info(self, row):
        return {
            'conferencias': int(row['conferencias']),
            'horario_ultimo_jogo': row['horario_final'],
            'status': row['status']
        }
