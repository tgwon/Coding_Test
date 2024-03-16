import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    a = input().split()
    result.append([int(a[1]), int(a[0])]) 
result.sort()    
for i in range(n):
    print(result[i][1], result[i][0])