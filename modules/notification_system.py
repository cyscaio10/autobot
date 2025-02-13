class NotificationSystem:
    def __init__(self):
        self.channels = {
            'operador': 'canal_operador',
            'teste': 'canal_teste',
            'administracao': 'canal_admin',
            'financeiro': 'canal_financeiro'
        }

    def notify_operator(self, message):
        self.send_message(self.channels['operador'], message)

    def notify_admin(self, message):
        self.send_message(self.channels['administracao'], message)

    def notify_financial(self, message):
        self.send_message(self.channels['financeiro'], message)

    def send_message(self, channel, message):
        # Implementar lógica para enviar mensagem para o canal específico
        print(f"Enviando mensagem para {channel}: {message}")

    def set_channel(self, role, channel_name):
        if role in self.channels:
            self.channels[role] = channel_name
            print(f"Canal para {role} atualizado para {channel_name}")
        else:
            print(f"Papel {role} não encontrado")
