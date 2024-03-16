import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    a = input().split()
    result.append(a)
result.sort(key = lambda x: (int(x[0]), int(x[1])))    
for i in range(n):
    print(result[i][0], result[i][1])