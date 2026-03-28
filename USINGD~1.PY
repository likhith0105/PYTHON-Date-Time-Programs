from datetime import datetime
s = "2023-07-21 10:30:45"
dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

print(dt)