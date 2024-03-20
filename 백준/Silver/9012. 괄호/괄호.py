t = int(input())
for _ in range(t):
    a = input()
    while a.find('()') != -1:
        a = a.replace('()','')
    if len(a) == 0:
        print('YES')
    else:
        print('NO')