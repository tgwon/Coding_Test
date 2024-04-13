value = input()
result = 10
for i in range(len(value) - 1):
    if value[i+1] != value[i]:
        result += 10
    else:
        result += 5
print(result)