import asyncio
import websockets

class ChatContainer:
    def __init__(self):
        self.websocket = None

    async def start(self):
        self.websocket = await websockets.connect('ws://chat_service:8080')
        await self.listen_for_messages()

    async def listen_for_messages(self):
        while True:
            message = await self.websocket.recv()
            await self.process_message(message)

    async def process_message(self, message):
        # Implementar lógica para processar mensagens do chat
        pass

    async def send_message(self, message):
        await self.websocket.send(message)