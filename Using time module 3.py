import time
t = time.localtime()
c = time.strftime("%H:%M:%S", t)
print("Current Time:", c)