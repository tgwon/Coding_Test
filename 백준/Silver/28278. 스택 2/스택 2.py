import sys
input = sys.stdin.readline 

n = int(input())
result = []
for i in range(n):
    nums = list(input().split())
    if nums[0] == '1':
        result.append(nums[1])
    elif nums[0] == '2':
        try:
            print(result.pop())
        except:
            print(-1)
    elif nums[0] == '3':
        print(len(result))
    elif nums[0] == '4':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    else:
        try:
            print(result[-1])
        except:
            print(-1)