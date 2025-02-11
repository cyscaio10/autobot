import docker
from typing import Dict, List
import logging
from .websocket_manager import WebSocketManager
from .image_recognition import ImageRecognition
from .browser_automation import BrowserAutomation
from .notification_system import NotificationSystem

class AutomationContainer:
    def __init__(self):
        self.client = docker.from_env()
        self.ws_manager = WebSocketManager()
        self.image_recognition = ImageRecognition()
        self.browser_automation = BrowserAutomation()
        self.notification_system = NotificationSystem()
        
        self.active_automations: Dict[str, bool] = {
            'conferencia': False,
            'atendimento': False
        }
        
    def start_automation(self, automation_type: str):
        """Inicia um tipo específico de automação"""
        if automation_type not in self.active_automations:
            raise ValueError(f"Tipo de automação inválido: {automation_type}")
            
        if automation_type == 'atendimento' and not self.active_automations['conferencia']:
            raise ValueError("Atendimento requer que a conferência esteja ativa")
            
        self.active_automations[automation_type] = True
        
        if automation_type == 'conferencia':
            self._start_conferencia()
        elif automation_type == 'atendimento':
            self._start_atendimento()
            
    def _start_conferencia(self):
        """Inicia o processo de conferência de apostas"""
        try:
            container = self.client.containers.run(
                'autobot-conferencia',
                detach=True,
                environment={
                    'WS_HOST': self.ws_manager.host,
                    'WS_PORT': self.ws_manager.port
                }
            )
            logging.info(f"Container de conferência iniciado: {container.id}")
        except Exception as e:
            logging.error(f"Erro ao iniciar container de conferência: {e}")
            self.active_automations['conferencia'] = False
            raise
            
    def _start_atendimento(self):
        """Inicia o processo de atendimento"""
        try:
            container = self.client.containers.run(
                'autobot-atendimento',
                detach=True,
                environment={
                    'WS_HOST': self.ws_manager.host,
                    'WS_PORT': self.ws_manager.port
                }
            )
            logging.info(f"Container de atendimento iniciado: {container.id}")
        except Exception as e:
            logging.error(f"Erro ao iniciar container de atendimento: {e}")
            self.active_automations['atendimento'] = False
            raise
            
    def stop_automation(self, automation_type: str = None):
        """Para um ou todos os processos de automação"""
        if automation_type:
            if automation_type == 'conferencia' and self.active_automations['atendimento']:
                raise ValueError("Não é possível parar conferência enquanto atendimento está ativo")
                
            self._stop_container(automation_type)
            self.active_automations[automation_type] = False
        else:
            # Para todos os containers
            for automation_type in self.active_automations:
                if self.active_automations[automation_type]:
                    self._stop_container(automation_type)
                    self.active_automations[automation_type] = False
                    
    def _stop_container(self, automation_type: str):
        """Para um container específico"""
        try:
            containers = self.client.containers.list(
                filters={'label': f'automation_type={automation_type}'}
            )
            for container in containers:
                container.stop()
                logging.info(f"Container parado: {container.id}")
        except Exception as e:
            logging.error(f"Erro ao parar container {automation_type}: {e}")
            raise
