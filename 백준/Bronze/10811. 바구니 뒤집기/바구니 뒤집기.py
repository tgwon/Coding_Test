N,M = map(int, input().split())
list = list(range(1,N+1))
for _ in range(M):
    i,j = map(int, input().split())
    result = list[i-1:j]
    list[i-1:j] = result[::-1]
print(*list)