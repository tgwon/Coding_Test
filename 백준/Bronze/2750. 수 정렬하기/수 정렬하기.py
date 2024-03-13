import sys
n = int(sys.stdin.readline())

array = []
for i in range(n):
    num = int(input())
    array.append(num)
    
for i in range(len(array)):
    min_value = min(array[i:])
    min_index = array.index(min_value)
    array[i], array[min_index] = array[min_index], array[i]

for i in range(len(array)):
    print(array[i])
