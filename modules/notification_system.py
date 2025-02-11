class NotificationSystem:
    def __init__(self):
        self.pending_issues = []
        
    def notify_operator(self, issue_type, details):
        """Tipos: odd_divergente, valor_alterado, jogo_nao_identificado"""
        notification = {
            'type': issue_type,
            'details': details,
            'timestamp': datetime.now(),
            'status': 'pending'
        }
        self.pending_issues.append(notification)
        self.show_notification_dialog(notification)
