a,b = input().split()
A=''
for i in range(len(a)):
    A = A + a[len(a)-i-1]
B=''
for i in range(len(b)):
    B = B + b[len(b)-i-1]

print(max(int(A),int(B)))