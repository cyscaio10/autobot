#!/usr/bin/env python
import asyncio
from modules.automation_manager import AutomationManager
from modules.containers.chat_container import ChatContainer
from modules.containers.spreadsheet_container import SpreadsheetContainer
from modules.containers.betting_container import BettingContainer
from modules.containers.verification_container import VerificationContainer

async def main():
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
        print("Aposta processada com sucesso!")
        print(f"Resultado: {result}")
        print(f"Sugestão: {suggestion}")
    else:
        print("Falha ao processar a aposta.")
        print(f"Erro: {result}")

    # Obter odds atuais para futebol
    football_odds = await manager.get_current_odds("football")
    print("Odds atuais para futebol:", football_odds)

    # Manter o programa rodando
    while True:
        await asyncio.sleep(1)
if __name__ == "__main__":
    asyncio.run(main())