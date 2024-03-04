ca = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
for i in ca:
    a= a.lower().replace(i,'_')
print(len(a))