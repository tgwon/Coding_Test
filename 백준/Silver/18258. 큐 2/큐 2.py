from collections import deque
import sys

queue = deque()
n = int(input())
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        queue.append(a[1])
    elif a[0] == 'pop':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    else:
        try:
            print(queue[-1])
        except:
            print(-1)