l = int(input())
char = input()

r = 31

list1 = 'abcdefghijklmnopqrstuvwxyz'
list2 = list(range(1,27))

result = 0

for i,j in enumerate(char):
    idx = list1.index(j)
    value = list2[idx]
    result += value*r**(i)

print(result)