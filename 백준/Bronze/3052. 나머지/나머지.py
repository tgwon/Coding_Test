list = []
result = []
for i in range(10):
    a = int(input())
    list.append(a)
for j in range(10):
    result.append(list[j]%42)
result = set(result)
print(len(result))