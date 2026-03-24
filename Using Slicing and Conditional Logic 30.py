t = "08:05:45 PM"

if t[-2:] == "AM" and t[:2] == "12":
    c = "00" + t[2:-2]
elif t[-2:] == "AM":
    c = t[:-2]
elif t[-2:] == "PM" and t[:2] == "12":
    c = t[:-2]
else:
    c = str(int(t[:2]) + 12) + t[2:8]

print(c)