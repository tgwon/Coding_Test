import sys
input = sys.stdin.readline

c,k,p = map(int,input().split())
result = 0

for i in range(1,c+1):
    result += k*i + p*i*i

print(result)