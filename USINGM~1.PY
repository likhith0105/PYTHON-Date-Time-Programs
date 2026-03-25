h1, m1, h2, m2 = 7, 20, 9, 45

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

if t1 == t2:
    print("Both are same times")
else:
    diff = t2 - t1 if t2 > t1 else (24 * 60 - (t1 - t2))
    h = diff // 60
    m = diff % 60
    print("{} : {}".format(h, m))