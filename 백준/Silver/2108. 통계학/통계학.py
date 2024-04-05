from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())

result = []

for i in range(n):
    result.append(int(input()))
    
result.sort()

print(round(sum(result)/len(result)))
print(result[len(result)//2])

result2 = []
max_value = max(Counter(result).values())

for i,j in Counter(result).items():
    if j == max_value:
        result2.append(i)
        
if len(result2) == 1:
    print(result2[0])
else:
    print(result2[1])
    
print(result[-1] - result[0])