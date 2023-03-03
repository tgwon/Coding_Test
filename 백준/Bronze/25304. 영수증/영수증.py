X = int(input())
N = int(input())
d = 0
for i in range(N):
    a,b = map(int, input().split())
    c = a*b
    d = c+d
if d == X:
    print('Yes')
else:
    print('No')