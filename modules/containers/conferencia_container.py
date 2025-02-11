import asyncio
import websockets
import json
from modules.image_recognition import ImageRecognition
from modules.browser_automation import BrowserAutomation

class ConferenciaContainer:
    def __init__(self, ws_host='localhost', ws_port=8765):
        self.ws_uri = f"ws://{ws_host}:{ws_port}"
        self.image_recognition = ImageRecognition()
        self.browser_automation = BrowserAutomation()
        self.running = False
        
    async def start(self):
        self.running = True
        async with websockets.connect(self.ws_uri) as websocket:
            await self.send_status(websocket, "iniciado", "Container de conferência iniciado")
            
            while self.running:
                try:
                    # Processo de conferência
                    prints = await self.capture_prints()
                    for print_data in prints:
                        # Análise do print
                        dados_aposta = self.image_recognition.process_aposta(print_data)
                        
                        if dados_aposta.get('needs_confirmation'):
                            # Solicita confirmação do operador
                            response = await self.request_operator_confirmation(
                                websocket,
                                print_data['image_path'],
                                dados_aposta['question']
                            )
                            dados_aposta.update(response)
                        
                        # Verificação no site
                        await self.browser_automation.check_aposta(dados_aposta)
                        
                except Exception as e:
                    await self.send_status(websocket, "erro", str(e))
                    
                await asyncio.sleep(1)  # Evita consumo excessivo de CPU
                
    async def send_status(self, websocket, status, message):
        await websocket.send(json.dumps({
            'type': 'automation_status',
            'data': {
                'status': status,
                'message': message
            }
        }))
        
    async def request_operator_confirmation(self, websocket, image_path, question):
        await websocket.send(json.dumps({
            'type': 'question',
            'data': {
                'image_path': image_path,
                'question': question
            }
        }))
        
        response = await websocket.recv()
        return json.loads(response)
