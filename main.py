#!/usr/bin/env python
import sys
import asyncio
import json
import os
import shutil
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPixmap, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from capture_screenshot import capture_screenshot
from modules.automation_manager import AutomationManager
from modules.containers.chat_container import ChatContainer
from modules.containers.spreadsheet_container import SpreadsheetContainer
from modules.containers.betting_container import BettingContainer
from modules.containers.verification_container import VerificationContainer

# Diretório de backup
BACKUP_DIR = "/app/backups"

class Worker(QThread):
    update_label = pyqtSignal(str)
    update_image = pyqtSignal(str)
    request_input = pyqtSignal(str)

    def run(self):
        asyncio.run(self.main())

    async def main(self):
        # Simulação de processos
        await asyncio.sleep(5)
        screenshot_path = capture_screenshot("https://example.com", "/app/screenshots")
        self.update_label.emit("Captura de tela realizada!")
        self.update_image.emit(screenshot_path)
        # Manter o programa rodando
        while True:
            await asyncio.sleep(1)
            # Simulação de falha na identificação de uma função
            if not self.identify_function():
                screenshot_path = capture_screenshot("https://example.com", "/app/screenshots")
                self.update_label.emit("Não foi possível identificar a função.")
                self.update_image.emit(screenshot_path)
                self.request_input.emit("Por favor, selecione a área onde a função está localizada.")

            # Realizar backup a cada 60 segundos
            self.perform_backup()

    def identify_function(self):
        # Simulação de identificação de função
        return False

    def perform_backup(self):
        # Gravar dados de exemplo para backup
        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "recognition_patterns": {},  # Adicionar dados reais aqui
            "betting_management": {}     # Adicionar dados reais aqui
        }
        backup_file = os.path.join(BACKUP_DIR, f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.json")
        with open(backup_file, 'w') as f:
            json.dump(data, f)
        # Manter apenas os últimos 10 backups
        self.cleanup_old_backups()

    def cleanup_old_backups(self):
        backups = sorted(os.listdir(BACKUP_DIR))
        while len(backups) > 10:
            os.remove(os.path.join(BACKUP_DIR, backups.pop(0)))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Betting Automation')
        self.setGeometry(100, 100, 800, 600)
        self.label = QLabel('Iniciando...', self)
        self.label.setGeometry(50, 50, 700, 500)
        self.image_label = QLabel(self)
        self.input_label = QLabel('Selecione a área onde a função está localizada:', self)
        self.input_label.setVisible(False)
        self.input_button = QPushButton('Confirmar', self)
        self.input_button.setVisible(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.worker = Worker()
        self.worker.update_label.connect(self.update_label)
        self.worker.update_image.connect(self.update_image)
        self.worker.request_input.connect(self.request_input)
        self.worker.start()

        self.input_button.clicked.connect(self.confirm_input)

    def update_label(self, text):
        self.label.setText(self.label.text() + '\n' + text)

    def update_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)

    def request_input(self, message):
        self.input_label.setText(message)
        self.input_label.setVisible(True)
        self.input_button.setVisible(True)

    def confirm_input(self):
        # Lógica para confirmar a entrada do operador
        self.input_label.setVisible(False)
        self.input_button.setVisible(False)
        self.label.setText(self.label.text() + '\n' + "Entrada confirmada pelo operador.")

if __name__ == "__main__":
    # Criar diretório de backup se não existir
    os.makedirs(BACKUP_DIR, exist_ok=True)
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())