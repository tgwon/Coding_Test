result = [1,1,2,2,2,8]
list = list(map(int,input().split()))
for i in range(6):
    print(result[i]-list[i], end=' ')