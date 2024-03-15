import sys
input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        result.append(order[1])
    elif order[0] == 'pop':
        try:
            print(result.pop())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(result))
    elif order[0] == 'empty':
        if result:
            print(0)
        else:
            print(1)
    else:
        try:
            print(int(result[-1]))
        except:
            print(-1)