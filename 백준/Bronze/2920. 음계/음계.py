num = list(map(int,input().split()))
a_count = 0
d_count = 0
for i in range(len(num)-1):
    if num[i] < num[i+1]:
        a_count += 1
    elif num[i] > num[i+1]:
        d_count += 1
    else:
        pass
if a_count == 7:
    print('ascending')
elif d_count == 7:
    print('descending')
else:
    print('mixed')