a = input()
if a[0:len(a)//2] == a[::-1][0:len(a)//2]:
    print(1)
else:
    print(0)