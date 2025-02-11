import asyncio
import websockets
import json
from typing import Callable, Dict
from queue import Queue
import threading

class WebSocketManager:
    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.message_queue = Queue()
        self.callbacks: Dict[str, Callable] = {}
        self.running = False
        
    def start(self):
        """Inicia o servidor WebSocket em uma thread separada"""
        self.running = True
        self.ws_thread = threading.Thread(target=self._run_server)
        self.ws_thread.daemon = True
        self.ws_thread.start()
        
    def _run_server(self):
        """Executa o servidor WebSocket"""
        async def handler(websocket, path):
            try:
                async for message in websocket:
                    data = json.loads(message)
                    event_type = data.get('type')
                    if event_type in self.callbacks:
                        response = await self.callbacks[event_type](data)
                        if response:
                            await websocket.send(json.dumps(response))
            except websockets.exceptions.ConnectionClosed:
                pass
                
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        server = websockets.serve(handler, self.host, self.port)
        loop.run_until_complete(server)
        loop.run_forever()
        
    def register_callback(self, event_type: str, callback: Callable):
        """Registra um callback para um tipo específico de evento"""
        self.callbacks[event_type] = callback
        
    def send_message(self, message_type: str, data: dict):
        """Envia uma mensagem para os clientes conectados"""
        message = {
            'type': message_type,
            'data': data
        }
        self.message_queue.put(json.dumps(message))
