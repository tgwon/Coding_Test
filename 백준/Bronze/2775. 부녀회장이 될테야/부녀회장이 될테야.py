import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    result = list(range(1,n+1))

    for _ in range(k):
        for j in range(1,n):
            result[j] += result[j-1]
            
    print(result[-1])