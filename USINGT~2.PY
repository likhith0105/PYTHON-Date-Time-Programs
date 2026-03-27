import time
st = time.time()
lt = st
lapnum = 1

print("Press ENTER to count laps.\nPress CTRL+C to stop")

try:
    while True:
        input()

        laptime = round((time.time() - lt), 2)
        tt = round((time.time() - st), 2)

        print("Lap No.", lapnum)
        print("Total Time:", tt)
        print("Lap Time:", laptime)
        print("*" * 20)

        lt = time.time()
        lapnum += 1

except KeyboardInterrupt:
    print("Done")