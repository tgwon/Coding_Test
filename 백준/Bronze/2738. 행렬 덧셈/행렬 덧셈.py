N,M = map(int,input().split())
A =[]
B= []
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
C =[]
for i in range(N):
    for j in range(M):
        C.append(A[i][j] + B[i][j])
        r = C[0+(i*M):M*(i+1)]     
    print(*r)
