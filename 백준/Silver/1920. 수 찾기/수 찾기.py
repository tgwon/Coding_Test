input()
list1 = sorted(list(map(int,input().split())))
input()
list2 = list(map(int,input().split()))

def bs(list,x):
    l,u = 0,len(list) - 1
    while u >= l:
        mid = (l + u) // 2
        if x > list[mid]:
            l = mid + 1
        elif x < list[mid]:
            u = mid - 1
        else:
            return print(1)
    return print(0)

for i in list2:
    bs(list1, i)