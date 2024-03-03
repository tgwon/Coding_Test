import math
a,b,v = map(int, input().split())

if a>=v:
    print(1)
elif a-b >= v-a:
    print(2)
else:
    print(math.ceil((v-a)/(a-b))+1)