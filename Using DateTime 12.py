from datetime import datetime

t1 = datetime.strptime('11:21:30 PM', '%I:%M:%S %p')
print(t1.strftime('%H:%M:%S'))

t2 = datetime.strptime('12:12:20 AM', '%I:%M:%S %p')
print(t2.strftime('%H:%M:%S'))