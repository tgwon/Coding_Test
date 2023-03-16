list = []
for i in range(5):
    a =int(input())
    list.append(a)  
avg = sum(list)//5
list.sort()
med = list[2]
print(avg)
print(med)
