from datetime import datetime
import calendar

s = "20/01/2020"
dt = datetime.strptime(s, "%d/%m/%Y")
res = calendar.timegm(dt.utctimetuple())
print(res)