import asyncio
import websockets
import json
from modules.chat_automation import ChatAutomation

class AtendimentoContainer:
    def __init__(self, ws_host='localhost', ws_port=8765):
        self.ws_uri = f"ws://{ws_host}:{ws_port}"
        self.chat_automation = ChatAutomation()
        self.running = False
        
    async def start(self):
        self.running = True
        async with websockets.connect(self.ws_uri) as websocket:
            await self.send_status(websocket, "iniciado", "Container de atendimento iniciado")
            
            while self.running:
                try:
                    # Processo de atendimento
                    mensagens = await self.chat_automation.get_new_messages()
                    
                    for mensagem in mensagens:
                        resposta = await self.process_message(mensagem)
                        
                        if resposta.get('needs_confirmation'):
                            # Solicita confirmação do operador
                            response = await self.request_operator_confirmation(
                                websocket,
                                resposta['print_path'],
                                resposta['question']
                            )
                            resposta.update(response)
                            
                        await self.chat_automation.send_response(resposta)
                        
                except Exception as e:
                    await self.send_status(websocket, "erro", str(e))
                    
                await asyncio.sleep(1)
                
    async def process_message(self, mensagem):
        # Implementar lógica de processamento de mensagens
        pass
        
    async def send_status(self, websocket, status, message):
        await websocket.send(json.dumps({
            'type': 'automation_status',
            'data': {
                'status': status,
                'message': message
            }
        }))
        
    async def request_operator_confirmation(self, websocket, print_path, question):
        await websocket.send(json.dumps({
            'type': 'question',
            'data': {
                'print_path': print_path,
                'question': question
            }
        }))
        
        response = await websocket.recv()
        return json.loads(response)
