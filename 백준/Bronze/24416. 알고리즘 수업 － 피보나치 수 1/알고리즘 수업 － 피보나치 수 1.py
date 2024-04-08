import sys
input = sys.stdin.readline
n = int(input())

f = [0] * (n+1)
def b(n):
    global f
    f[1] = f[2] = 1
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]

b(n)
print(f[n], n-2)