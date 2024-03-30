n = int(input())

result = []
for i in range(n):
    result.append(list(map(int, input().split())))


value = []

for i in range(n):
    count = 1
    for j in range(n):
        if result[j][0] > result[i][0] and result[j][1] > result[i][1]:
            count += 1
    value.append(count)

print(*value)