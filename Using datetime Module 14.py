from datetime import datetime, timedelta

h1, m1, h2, m2 = 7, 20, 9, 45

t1 = datetime.strptime("{}:{}".format(h1, m1), "%H:%M")
t2 = datetime.strptime("{}:{}".format(h2, m2), "%H:%M")

if t2 < t1:
    t2 += timedelta(days=1)

diff = t2 - t1
h, m = divmod(diff.seconds // 60, 60)
print("{} : {}".format(h, m))