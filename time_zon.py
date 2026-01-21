from datetime import datetime
import pytz

def get_message_time():
    timezone = pytz.timezone('Europe/Moscow')
    now = datetime.now(timezone)
    hour = now.hour

    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"