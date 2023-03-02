a,b = map(int, input().split())
c = int(input())

import datetime as dt
a = dt.datetime(2000,6,29,a,b,0)
d = a + dt.timedelta(minutes = c)
print(d.hour, d.minute)