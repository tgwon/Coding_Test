

result1 = []
result2 = []

for i in range(3):
    a,b = map(int,input().split())
    result1.append(a)
    result2.append(b)

for i in result1:
    if result1.count(i) == 1:
        print(i, end= ' ')

for i in result2:
    if result2.count(i) == 1:
        print(i, end= ' ')