from dateutil import parser

s = "2023-07-21 10:30:45"
dt = parser.parse(s)

print(dt)