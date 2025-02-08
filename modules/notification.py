import smtplib
from email.mime.text import MIMEText
from config import settings

def notify_operator(dados_aposta):
    msg = MIMEText(f"Aposta processada: {dados_aposta}")
    msg['Subject'] = 'Nova Aposta Processada'
    msg['From'] = 'noreply@example.com'
    msg['To'] = settings.NOTIFICATION_EMAIL
    
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()