import pytz

from datetime import datetime

tz = pytz.timezone('Asia/Kolkata')

current_time = datetime.now().astimezone(tz).strftime("%Y-%m-%d %H:%M")
