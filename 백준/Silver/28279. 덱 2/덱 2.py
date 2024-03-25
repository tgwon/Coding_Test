from collections import deque
import sys

input = sys.stdin.readline
deque = deque()
n = int(input())

for i in range(n):
    a = input().split()
    if a[0] == '1':
        deque.appendleft(a[1])
    elif a[0] == '2':
        deque.append(a[1])
    elif a[0] == '3':
        try:
            print(deque.popleft())
        except:
            print(-1)
    elif a[0] == '4':
        try:
            print(deque.pop())
        except:
            print(-1)
    elif a[0] == '5':
        print(len(deque))
    elif a[0] == '6':
        if deque:
            print(0)
        else:
            print(1)
    elif a[0] == '7':
        try:
            print(deque[0])
        except:
            print(-1)
    else:
        try:
            print(deque[-1])
        except:
            print(-1)