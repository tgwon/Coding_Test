N,M = map(int, input().split())
list=[]
for i in range(N):
    list.append(0)
for I in range(M):
    i,j,k = map(int, input().split())
    ii = i-1
    jj = j-1
    while ii<=jj:
        list[ii] = k
        ii = ii+1
print(*list)
         

    