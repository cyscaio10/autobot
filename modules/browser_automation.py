from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BrowserAutomation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def check_flashscore(self, bet):
        results = []
        for game in bet['games']:
            try:
                self.driver.get("https://www.flashscore.com")
                search_box = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "searchInput"))
                )
                search_box.send_keys(game['team1'])

                result = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "searchResult"))
                )
                result.click()

                score = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "score"))
                ).text
                details = self.driver.find_element(By.CLASS_NAME, "matchDetails").text

                game_result = self.process_game_result(game, score, details)
                results.append(game_result)
            except Exception as e:
                print(f"Error processing game {game['team1']}: {str(e)}")
                results.append(None)

        return self.evaluate_bet_result(bet, results)

    def process_game_result(self, game, score, details):
        # Implement logic to process the game result
        # This is a placeholder implementation
        home_score, away_score = map(int, score.split('-'))
        return {
            'team1': game['team1'],
            'team2': game['team2'],
            'score': score,
            'details': details,
            'winner': game['team1'] if home_score > away_score else game['team2'] if away_score > home_score else 'Draw'
        }

    def evaluate_bet_result(self, bet, results):
        # Implement logic to evaluate the overall bet result
        # This is a placeholder implementation
        correct_predictions = sum(1 for result in results if result and result['winner'] == bet['prediction'])
        return {
            'bet': bet,
            'results': results,
            'correct_predictions': correct_predictions,
            'total_games': len(bet['games']),
            'success_rate': correct_predictions / len(bet['games']) if bet['games'] else 0
        }

    def close(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    # Test the BrowserAutomation class
    automation = BrowserAutomation()
    test_bet = {
        'games': [
            {'team1': 'Real Madrid', 'team2': 'Barcelona'},
            {'team1': 'Manchester United', 'team2': 'Liverpool'}
        ],
        'prediction': 'Real Madrid'
    }
    result = automation.check_flashscore(test_bet)
    print(result)
    automation.close()