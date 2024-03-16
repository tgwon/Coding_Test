n = int(input())
f = 1
if n in [0,1]:
    pass
else:
    for i in range(1,n+1):
        f *= i
for i,j in enumerate(str(f)[::-1]):
    if j != '0':
        print(int(i))
        break