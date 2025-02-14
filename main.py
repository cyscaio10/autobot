#!/usr/bin/env python
import sys
import asyncio
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from modules.automation_manager import AutomationManager
from modules.containers.chat_container import ChatContainer
from modules.containers.spreadsheet_container import SpreadsheetContainer
from modules.containers.betting_container import BettingContainer
from modules.containers.verification_container import VerificationContainer

class Worker(QThread):
    update_label = pyqtSignal(str)

    def run(self):
        asyncio.run(self.main())

    async def main(self):
        betting_site_url = "https://www.example-betting-site.com"
        manager = AutomationManager(betting_site_url)

        # Inicializar containers
        chat_container = ChatContainer()
        spreadsheet_container = SpreadsheetContainer()
        betting_container = BettingContainer()
        verification_container = VerificationContainer()

        # Iniciar todos os containers
        await asyncio.gather(
            chat_container.start(),
            spreadsheet_container.start(),
            betting_container.start(),
            verification_container.start()
        )
        # Exemplo de uso
        image_path = "path/to/bet_image.jpg"
        success, result, suggestion = await manager.process_bet_image(image_path)

        if success:
            self.update_label.emit("Aposta processada com sucesso!")
            self.update_label.emit(f"Resultado: {result}")
            self.update_label.emit(f"Sugestão: {suggestion}")
        else:
            self.update_label.emit("Falha ao processar a aposta.")
            self.update_label.emit(f"Erro: {result}")

        # Obter odds atuais para futebol
        football_odds = await manager.get_current_odds("football")
        self.update_label.emit(f"Odds atuais para futebol: {football_odds}")

        # Manter o programa rodando
        while True:
            await asyncio.sleep(1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Betting Automation')
        self.setGeometry(100, 100, 800, 600)
        self.label = QLabel('Iniciando...', self)
        self.label.setGeometry(50, 50, 700, 500)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.worker = Worker()
        self.worker.update_label.connect(self.update_label)
        self.worker.start()

    def update_label(self, text):
        self.label.setText(self.label.text() + '\n' + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())