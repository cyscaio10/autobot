from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime
import os

def capture_screenshot(url, output_dir):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_path = os.path.join(output_dir, f"screenshot_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    driver.quit()
    return screenshot_path

if __name__ == "__main__":
    url = "https://example.com"
    output_dir = "/app/screenshots"
    os.makedirs(output_dir, exist_ok=True)
    screenshot_path = capture_screenshot(url, output_dir)
    print(f"Screenshot saved to {screenshot_path}")