N = int(input())
list = list(map(int, input().split()))
M = max(list)
r = 0
for i in range(N):
    list[i] = list[i]/M*100
print(sum(list)/N)
