from collections import deque
n = int(input())
array = deque(enumerate(map(int, input().split())))


for i in range(n):
    index, num = array.popleft()
    print(index+1, end = ' ')
    if array:  
        if num > 0:
            for _ in range(num - 1):
                array.append(array.popleft())
        else:
            for _ in range(abs(num)):
                array.appendleft(array.pop())
    else:
        break