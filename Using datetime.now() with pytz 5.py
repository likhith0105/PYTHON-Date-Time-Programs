from datetime import datetime
import pytz

tz = pytz.timezone('india')
ct = datetime.now(tz)
print(ct)