from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from config import settings

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_service():
    creds = Credentials.from_service_account_file(settings.GOOGLE_SHEETS_CREDENTIALS_PATH, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    return service

def update_sheet(dados_aposta):
    service = get_service()
    sheet = service.spreadsheets()
    # Atualiza a planilha com os dados da aposta
    # Exemplo de atualização
    values = [
        [dados_aposta['time'], dados_aposta['odds'], dados_aposta['valor'], dados_aposta['horario'], "Log Type", 0]  # Adiciona colunas para logs e contagem de conferências
    ]
    body = {
        'values': values
    }
    result = sheet.values().update(
        spreadsheetId=settings.SHEET_ID,
        range='A1:F1',
        valueInputOption='RAW',
        body=body
    ).execute()
    return result

def add_log(aposta_id, log_type):
    service = get_service()
    sheet = service.spreadsheets()
    # Adiciona um log para uma aposta específica
    values = [
        [log_type, 1]  # Tipo de log e incrementa a contagem de conferências
    ]
    body = {
        'values': values
    }
    result = sheet.values().append(
        spreadsheetId=settings.SHEET_ID,
        range=f'A{aposta_id}:F{aposta_id}',
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()
    return result

def read_sheet(range_name):
    service = get_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=settings.SHEET_ID,
        range=range_name
    ).execute()
    values = result.get('values', [])
    return values