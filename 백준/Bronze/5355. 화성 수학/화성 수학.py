t = int(input())
for i in range(t):
    result = 0
    value = input().split()
    for j in value:
        if j == '@':
            result *= 3
        elif j == '%':
            result += 5
        elif j == '#':
            result -= 7
        else:
            result = float(j)
    print("%0.2f" % result)