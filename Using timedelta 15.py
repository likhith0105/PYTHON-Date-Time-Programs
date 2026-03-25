from datetime import timedelta

h1, m1, h2, m2 = 7, 20, 9, 45

t1 = timedelta(hours=h1, minutes=m1)
t2 = timedelta(hours=h2, minutes=m2)

if t2 < t1:
    t2 += timedelta(days=1)

diff = t2 - t1
h, m = divmod(diff.seconds // 60, 60)
print("{} : {}".format(h, m))