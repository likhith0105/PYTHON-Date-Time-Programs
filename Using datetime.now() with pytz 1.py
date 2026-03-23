from datetime import datetime
import pytz

tz = pytz.timezone('Asia/Kolkata')
dt = datetime.now(tz)
print("India Time:", dt.strftime("%H:%M:%S"))