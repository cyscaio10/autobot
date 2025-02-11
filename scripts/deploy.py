import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import click
from modules.container_manager import ContainerManager
@click.group()
def cli():
    """Ferramenta de deploy dos containers do AutoBot"""
    pass

@cli.command()
def build():
    """Constrói todos os containers"""
    manager = ContainerManager()
    if manager.build_containers():
        click.echo("Containers construídos com sucesso!")
    else:
        click.echo("Erro ao construir containers")

@cli.command()
def deploy():
    """Realiza o deploy completo dos containers"""
    manager = ContainerManager()
    if manager.deploy_containers():
        click.echo("Deploy realizado com sucesso!")
    else:
        click.echo("Erro no deploy")

if __name__ == '__main__':
    cli()

self.client = docker.from_env()