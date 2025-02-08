from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import settings

class BrowserAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome(settings.SELENIUM_DRIVER_PATH)

    def human_like_delay(self):
        time.sleep(2 + (time.time() % 1))

    def check_aposta(self, dados_aposta):
        self.driver.get(settings.BET365_URL)
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys(dados_aposta['time'])
        self.human_like_delay()
        search_box.submit()
        # Mais interações podem ser adicionadas aqui

    def add_to_favorites(self, url, name):
        self.driver.get(url)
        self.driver.execute_script(f"window.external.AddFavorite('{url}', '{name}')")

    def close(self):
        self.driver.quit()

# Exemplo de uso
automation = BrowserAutomation()
automation.add_to_favorites("https://www.bet365.com", "Bet365")
automation.close()