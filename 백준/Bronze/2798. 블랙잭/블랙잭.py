n, m = map(int, input().split())
array = list(map(int, input().split()))

result = []

for i in array:
    for j in array[array.index(i) + 1:]:
        for k in array[array.index(j) + 1:]:
            sum = i + j + k
            if sum <= m:
                result.append(sum)
                
print(max(result))