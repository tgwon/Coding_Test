N = int(input())
for i in range(2*N-1):
    print(' '*abs(N-i-1)+'*'*(2*N-1-2*abs(N-i-1)))


