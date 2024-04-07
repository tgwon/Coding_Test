a,b,c = map(int, input().split())

if max(a,b,c) == a:
    one = a
    other = b+c
elif max(a,b,c) == b:
    one = b
    other = a+c
else:
    one = c
    other = a+b
    
while one >= other:
    one -= 1

print(one + other)