import time
s = time.perf_counter()
l = s
lap = 1

print("Press ENTER to record laps.\nPress CTRL+C to stop")

try:
    while True:
        # wait for ENTER key press
        input()
        
        # calculate lap time and total time
        cur = time.perf_counter()
        lt  = round(cur - l, 4)
        tt = round(cur - s, 4)
        
        print("Lap No.:", lap)
        print("Total Time:", tt)
        print("Lap Time:", lt)
        print("*" * 20)
        
        # update previous lap time
        l = cur
        lap += 1

# stop when CTRL+C is pressed
except KeyboardInterrupt:
    print("Done")