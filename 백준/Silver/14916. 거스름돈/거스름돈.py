n = int(input())
count = 0
if (n%5)%2 == 0:
    count += n//5
    count += (n%5)//2
    print(count)
elif n//5 == 0:
    print(-1)
else:
    count += n//5 -1
    count += (n-5*(n//5 -1))//2
    print(count)