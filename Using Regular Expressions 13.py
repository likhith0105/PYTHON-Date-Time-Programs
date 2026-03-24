import re

t = '11:21:30 PM'
hour, mins, sec, am_pm = re.findall(r'\d+|\w+', t)
hour = int(hour)

if am_pm == 'PM' and hour != 12:
    hour += 12
elif am_pm == 'AM' and hour == 12:
    hour = 0

c = f'{hour:02d}:{mins}:{sec}'
print(c)

t2 = '12:12:20 AM'
hour, mins, sec, am_pm = re.findall(r'\d+|\w+', t2)
hour = int(hour)

if am_pm == 'PM' and hour != 12:
    hour += 12
elif am_pm == 'AM' and hour == 12:
    hour = 0

c2 = f'{hour:02d}:{mins}:{sec}'
print(c2)