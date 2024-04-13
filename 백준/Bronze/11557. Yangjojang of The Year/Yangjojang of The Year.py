t = int(input())
for i in range(t):
    n = int(input())
    result = []
    for j in range(n):
        value = input().split()
        result.append((value[0],int(value[1])))
    result.sort(key = lambda x : x[1])
    print(result[-1][0])