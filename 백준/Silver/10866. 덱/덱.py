from collections import deque
import sys
deque = deque()
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a = input().split()
    if a[0] == 'push_front':
        deque.appendleft(a[1])
    elif a[0] == 'push_back':
        deque.append(a[1])
    elif a[0] == 'pop_front':
        try:
            print(deque.popleft())
        except:
            print(-1)
    elif a[0] == 'pop_back':
        try:
            print(deque.pop())
        except:
            print(-1)
    elif a[0] == 'size':
        print(len(deque))
    elif a[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        try:
            print(deque[0])
        except:
            print(-1)
    else:
        try:
            print(deque[-1])
        except:
            print(-1)