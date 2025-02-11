import docker
import logging
import os
from typing import List, Dict

class ContainerManager:
    def __init__(self):
        self.client = docker.from_env()  # Corrigido de from_client() para from_env()
        self.containers_path = os.path.join('modules', 'containers')        
    def build_containers(self):
        """Constrói todos os containers necessários"""
        containers = ['conferencia', 'atendimento']
        
        for container in containers:
            self.build_container(container)
            
    def build_container(self, container_type: str):
        """Constrói um container específico"""
        dockerfile_path = os.path.join(self.containers_path, container_type)
        
        try:
            logging.info(f"Iniciando build do container {container_type}")
            image, logs = self.client.images.build(
                path=dockerfile_path,
                tag=f"autobot-{container_type}:latest",
                rm=True
            )
            logging.info(f"Container {container_type} construído com sucesso")
            return image
        except Exception as e:
            logging.error(f"Erro ao construir container {container_type}: {e}")
            raise
            
    def deploy_containers(self):
        """Deploy de todos os containers"""
        try:
            self.build_containers()
            logging.info("Todos os containers foram construídos com sucesso")
            return True
        except Exception as e:
            logging.error(f"Erro no deploy dos containers: {e}")
            return False
