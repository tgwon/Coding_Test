N,K= map(int, input().split())
list = []
for i in range(1,N+1):
    if N%i == 0:
        list.append(i)
        
if K <= len(list):
    print(list[K-1])
else:
    print(0)