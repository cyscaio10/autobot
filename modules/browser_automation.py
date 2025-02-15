from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import io

class BrowserAutomation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def capture_screenshot(self, url):
        self.driver.get(url)
        screenshot = self.driver.get_screenshot_as_png()
        return Image.open(io.BytesIO(screenshot))

    def login(self, url, username, password):
        self.driver.get(url)
        # Implementar lógica de login
        screenshot = self.capture_screenshot(self.driver.current_url)
        return screenshot

    def navigate_to_page(self, url):
        self.driver.get(url)
        return self.capture_screenshot(url)

    def close(self):
        self.driver.quit()