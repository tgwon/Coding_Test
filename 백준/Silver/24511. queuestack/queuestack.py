from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

queue = deque()
for j,k in enumerate(b):
    if a[j] == 0:
        queue.append(k)

for i in c:
    queue.appendleft(i)
    print(queue.pop(), end = ' ')