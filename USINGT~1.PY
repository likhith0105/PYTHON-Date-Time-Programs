from datetime import datetime
import time

s = "20/01/2020"
dt = datetime.strptime(s, "%d/%m/%Y")
res = time.mktime(dt.timetuple())
print(res)