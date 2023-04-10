N, M = map(int, input().split())
list = list(range(1,N+1))
for I in range(M):
    i,j = map(int, input().split())
    list[i-1], list[j-1] = list[j-1], list[i-1]
print(*list)


