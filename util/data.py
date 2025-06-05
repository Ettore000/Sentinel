import json
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

DEFAULT_USER_DATA = {
    'counter': 0,
    'paused': False,
    'current_plan': 'default',
    'plans': {},
    'history': []
}


def _user_file(chat_id: int) -> str:
    os.makedirs(DATA_DIR, exist_ok=True)
    return os.path.join(DATA_DIR, f'{chat_id}.json')


def load_user_data(chat_id: int) -> dict:
    path = _user_file(chat_id)
    if not os.path.exists(path):
        data = DEFAULT_USER_DATA.copy()
        save_user_data(chat_id, data)
        return data
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_user_data(chat_id: int, data: dict) -> None:
    path = _user_file(chat_id)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def add_minutes(chat_id: int, minutes: int) -> int:
    data = load_user_data(chat_id)
    data['counter'] += minutes
    data['history'].append({'time': datetime.utcnow().isoformat(), 'minutes': minutes})
    save_user_data(chat_id, data)
    return data['counter']


def remove_last_entry(chat_id: int) -> None:
    data = load_user_data(chat_id)
    if data['history']:
        last = data['history'].pop()
        data['counter'] = max(0, data['counter'] - last['minutes'])
        save_user_data(chat_id, data)

def set_paused(chat_id: int, paused: bool) -> None:
    data = load_user_data(chat_id)
    data['paused'] = paused
    save_user_data(chat_id, data)
