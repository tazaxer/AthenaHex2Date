import sys
import datetime

# total args
n = len(sys.argv)

if n != 5:
    exit(1)

s = ""
for i in range(1, n):
    s += sys.argv[i]
b = bin(int(s, 16)).zfill(8)
data = b.replace('b', '0')

year = int(data[0:6], 2) + 2010
month = int(data[6:10], 2)
day = int(data[10:15], 2)

hour = int(data[15:20], 2)
min = int(data[20:26], 2)
sec = int(data[26:32], 2)

date = datetime.datetime(year, month, day, hour, min, sec)
print(date)