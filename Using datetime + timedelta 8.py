from datetime import datetime, timedelta

presentday = datetime.now()
yesterday = presentday - timedelta(days=1)
tomorrow  = presentday + timedelta(days=1)

print("Yesterday:", yesterday.strftime('%d-%m-%Y'))
print("Today:", presentday.strftime('%d-%m-%Y'))
print("Tomorrow:", tomorrow.strftime('%d-%m-%Y'))