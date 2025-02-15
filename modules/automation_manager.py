from modules.image_processing import ImageProcessor
from modules.chat_automation import ChatAutomation
from modules.spreadsheet_manager import SpreadsheetManager
from modules.flashscore_integration import FlashscoreIntegration
from modules.betting_site_integration import BettingSiteIntegration

class AutomationManager:
    def __init__(self, config):
        self.config = config
        self.image_processor = ImageProcessor()
        self.chat_automation = ChatAutomation(config['chat_window_title'])
        self.spreadsheet_manager = SpreadsheetManager(config['credentials_file'], config['spreadsheet_id'])
        self.flashscore = FlashscoreIntegration()
        self.betting_site = BettingSiteIntegration(config['betting_site_url'])

    def run_automation(self):
        while True:
            # Capturar screenshot do chat
            chat_image = self.chat_automation.capture_chat_screenshot()

            # Processar imagem e extrair informações da aposta
            bet_info = self.image_processor.find_bet_info(chat_image)

            if bet_info:
                # Verificar resultado no Flashscore
                match_result = self.flashscore.get_match_results(bet_info['match_id'])

                # Atualizar planilha
                self.spreadsheet_manager.append_row([bet_info['id'], bet_info['match'], match_result['score']])

                # Colocar aposta no site de apostas
                self.betting_site.place_bet(bet_info)

            # Aguardar antes da próxima iteração
            time.sleep(self.config['automation_interval'])

    def stop_automation(self):
        self.betting_site.close()
