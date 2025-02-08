import os
import json
from datetime import datetime, timedelta

STATE_FILE = 'state.json'
LOG_FILE = 'logs/log.txt'

def init_state():
    if not os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'w') as f:
            json.dump({'last_processed': None, 'errors': [], 'conference_times': []}, f)

def get_next_aposta():
    # Exemplo de obtenção da próxima aposta
    return {'image_path': 'path/to/image.jpg'}

def check_new_apostas():
    # Exemplo de verificação de novas apostas
    pass

def log_error(aposta, error):
    with open(STATE_FILE, 'r') as f):
        state = json.load(f)
    state['errors'].append({'aposta': aposta, 'error': str(error)})
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

    with open(LOG_FILE, 'a') as log:
        log.write(f"{datetime.now()} - Error: {str(error)}\n")

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

def load_state():
    with open(STATE_FILE, 'r') as f):
        state = json.load(f)
    return state

def schedule_conferences():
    conference_times = [
        datetime.now().replace(hour=8, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=13, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=18, minute=0, second=0, microsecond=0),
        datetime.now().replace(hour=22, minute=0, second=0, microsecond=0)
    ]
    state = load_state()
    state['conference_times'] = [time.isoformat() for time in conference_times]
    save_state(state)

def perform_conference():
    state = load_state()
    now = datetime.now()
    for time_str in state['conference_times']:
        conference_time = datetime.fromisoformat(time_str)
        if now >= conference_time:
            # Realiza a conferência das apostas
            # Atualiza a planilha e incrementa a contagem de conferências
            print(f"Conferência realizada às {conference_time}")
            state['conference_times'].remove(time_str)
    save_state(state)