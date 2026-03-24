import calendar
from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow  = today + timedelta(days=1)

print("Yesterday:", calendar.day_name[yesterday.weekday()], yesterday.strftime('%d-%m-%Y'))
print("Today:", calendar.day_name[today.weekday()], today.strftime('%d-%m-%Y'))
print("Tomorrow:", calendar.day_name[tomorrow.weekday()], tomorrow.strftime('%d-%m-%Y'))