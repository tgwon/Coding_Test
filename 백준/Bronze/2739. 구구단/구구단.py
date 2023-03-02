N = int(input())

for i in range(9):
    a = i + 1
    b = N*a
    N = N
    print(f'{N} * {a} = {b}')