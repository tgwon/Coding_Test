n = int(input())
result = [input() for i in range(n)]
result = list(set(result))
result.sort(key = lambda x: (len(x),x))
for i in result:
    print(i)