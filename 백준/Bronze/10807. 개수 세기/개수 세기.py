N = int(input())
l = list(map(int, input().split()))
v = int(input())
result = 0
for i in l:
    if i == v:
        result = result + 1
print(result)    