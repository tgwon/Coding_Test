a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

if (a1 * n0 + a0 <= c * n0) & (a1 <= c):
    print(1)
else:
    print(0)

#c, n0은 양수. n>=n0에 대해서 성립을 해야 1이 print 되게 해야함.
#(a1 * n0 + a0 <= c * n0)
#이걸 떠올려볼 수 있는데
#n>=n0인 n들에 대해서 늘 성립하는 건 아님. 
#n0에 대해서만 성립을 하고 n0보다 큰 양수 값 n에 대해서는 성립 안하기도함.
#c보다 a1이 큰데 a0이 음수라면 n0에 대해서 위 조건이 성립할 수 있음. 하지만 n에 대해서는 바로 성립 x.
#c가 a1보다 항상 크거나 같다는 조건도 있어야함.
#이 조건도 함께 있다면 모든 n>=n0에 대해서 성립함.
