from datetime import datetime

s = "20/01/2020"
dt = datetime.strptime(s, "%d/%m/%Y")
res = dt.timestamp()
print(res)