import time

h1, m1, h2, m2 = 7, 20, 9, 45

t1 = time.mktime((2025, 11, 12, h1, m1, 0, 0, 0, 0))
t2 = time.mktime((2025, 11, 12, h2, m2, 0, 0, 0, 0))

if t2 < t1:
    t2 += 86400

diff = t2 - t1
h, m = divmod(int(diff // 60), 60)
print("{} : {}".format(h, m))