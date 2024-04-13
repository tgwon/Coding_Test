a = 100
b = 100

n = int(input())

for i in range(n):
    A,B = map(int, input().split())
    if A<B :
        a -= B
    elif A>B :
        b -= A
    else:
        pass
    
print(a,b, sep = '\n')