n, k = map(int, input().split())

result = list(range(1,n+1))
idx = k-1
value = []

while result:
    if idx >= len(result):
        idx %= len(result)
    value.append(result.pop(idx))
    idx += (k-1)

print('<', end='')
for i in range(0,n-1):
    print(str(value[i])+',', end =' ')
print(str(value[n-1])+'>')