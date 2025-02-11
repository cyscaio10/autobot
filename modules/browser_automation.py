from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BrowserAutomation:
    def __init__(self):
        self.options = Options()
        self.options.headless = False  # Para ver a interface, manter False
        self.driver = Firefox(options=self.options)

    def check_aposta(self, dados_aposta):
        try:
            self.driver.get("https://www.bet365.com")
            # Supondo que o campo de busca tenha o atributo 'name' igual a 'q'
            search_box = self.driver.find_element_by_name('q')
            search_box.send_keys(dados_aposta.get('time', ''))
            self.human_like_delay()
            search_box.submit()
        except NoSuchElementException as e:
            logger.error(f"Elemento não encontrado: {e}")
        except Exception as e:
            logger.error(f"Erro na automação: {e}")

    def human_like_delay(self):
        time.sleep(2)

    def shutdown(self):
        self.driver.quit()

if __name__ == '__main__':
    ba = BrowserAutomation()
    teste = {'time': 'Time A vs Time B', 'odds': '1.5', 'valor': '100'}
    ba.check_aposta(teste)
    ba.shutdown()