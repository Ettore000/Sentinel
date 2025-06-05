import json
import os
from datetime import datetime, time

PLANS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'plans')


def load_plan(name: str):
    path = os.path.join(PLANS_DIR, f'{name}.json')
    if not os.path.exists(path):
        raise FileNotFoundError(f'Plan {name} not found')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_current_event(plan):
    now = datetime.now().time()
    upcoming = None
    prev = None
    for event in sorted(plan, key=lambda e: e['time']):
        t = datetime.strptime(event['time'], '%H:%M').time()
        if now >= t:
            prev = event
        elif now < t and upcoming is None:
            upcoming = event
    return prev, upcoming
