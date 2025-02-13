from .modules.automation_manager import AutomationManager
from .interface.main_ui import MainUI

class Controller:
    def __init__(self):
        self.automation_manager = AutomationManager()
        self.ui = MainUI(self)

    def start(self):
        self.ui.run()

    def process_new_bet(self, image):
        bet_info = self.automation_manager.recognize_bet(image)
        if self.automation_manager.validate_bet(bet_info):
            if not self.automation_manager.is_duplicate_bet(bet_info):
                self.automation_manager.register_bet(bet_info)
                self.ui.update_dashboard()

    def check_results(self):
        results = self.automation_manager.check_bet_results()
        self.ui.update_dashboard(results)

    def learn_from_data(self):
        self.automation_manager.learn_from_existing_data()

if __name__ == "__main__":
    controller = Controller()
    controller.start()