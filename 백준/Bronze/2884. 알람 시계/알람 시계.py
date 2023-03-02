a, b = map(int, input().split())
import datetime as dt
a = dt.datetime(2000,6,29,a,b,0)
b = a + dt.timedelta(minutes=-45)
print(b.hour, b.minute)