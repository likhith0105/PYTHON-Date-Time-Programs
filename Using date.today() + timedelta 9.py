from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow  = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime('%d-%m-%Y'))
print("Today:", today.strftime('%d-%m-%Y'))
print("Tomorrow:", tomorrow.strftime('%d-%m-%Y'))