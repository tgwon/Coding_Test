from collections import deque

n = int(input())

result = deque([i for i in range(1,n+1)])

while len(result) > 1:
    result.popleft()
    result.append(result.popleft())

print(result[0])