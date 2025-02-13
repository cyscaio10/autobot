import asyncio
import websockets
from .containers.atendimento_container import AtendimentoContainer
from .containers.conferencia_container import ConferenciaContainer

class ContainerManager:
    def __init__(self):
        self.containers = {
            "atendimento": AtendimentoContainer(),
            "conferencia": ConferenciaContainer()
        }
        self.status = {}

    async def start_container(self, container_type):
        if container_type in self.containers:
            await self.containers[container_type].start()
            self.status[container_type] = "running"
        else:
            raise ValueError(f"Container type '{container_type}' not found")

    async def stop_container(self, container_type):
        if container_type in self.containers:
            await self.containers[container_type].stop()
            self.status[container_type] = "stopped"
        else:
            raise ValueError(f"Container type '{container_type}' not found")

    async def monitor_containers(self):
        while True:
            for container_type, container in self.containers.items():
                status = await container.get_status()
                self.status[container_type] = status
            await asyncio.sleep(5)  # Check every 5 seconds

    async def handle_websocket(self, websocket, path):
        while True:
            try:
                message = await websocket.recv()
                # Process incoming messages (e.g., commands to start/stop containers)
                response = await self.process_message(message)
                await websocket.send(response)
            except websockets.exceptions.ConnectionClosed:
                break

    async def process_message(self, message):
        # Implement logic to process incoming messages
        pass

    def get_container_status(self):
        return self.status

