list1 = []
for i in range(28):
    a = int(input())
    list1.append(a)
set1 = set(list1)
list2 = list(range(1,31))
set2 = set(list2)
print(min(set2-set1))
print(max(set2-set1))