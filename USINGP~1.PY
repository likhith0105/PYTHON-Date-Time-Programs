import pandas as pd
s = "2023-07-21 10:30:45"
dt = pd.to_datetime(s, format="%Y-%m-%d %H:%M:%S")

print(dt)