list = [0]*81
for i in range(9):
    list[i*9:i*9+9] = map(int, input().split())
print(max(list))
print(list.index(max(list))//9+1, (list.index(max(list)))%9+1)

