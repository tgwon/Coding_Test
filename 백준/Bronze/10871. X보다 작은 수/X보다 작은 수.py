N,X = map(int, input().split())
seq = list(map(int,input().split()))
result = []
for i in seq:
    if i < X:
        result.append(i)
print(*result)