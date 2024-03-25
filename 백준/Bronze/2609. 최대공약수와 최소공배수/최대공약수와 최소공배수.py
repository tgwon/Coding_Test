n, m = map(int, input().split())

# 값을 저장할 리스트 
result = []

# 나누는 수의 시작
i = 2

# 두개 다 나누어 떨어지면 i는 다시 2
# 두개 다 나누어 떨어지지 않으면 i는 1 더해서 다시 하기

while i <= min(n,m):
    if (n%i == 0) and (m%i == 0):
        result.append([i, n//i, m//i])
        n //= i
        m //= i
        i = 2
    else:
        i += 1

# 만약 result에 값이 있다면, 다음과 같이 최소 공배수랑 최대 공약수를 구할 수 있음
if result:
    a = 1
    b = 1
    
    for i in result:
        a *= i[0]
        b *= i[0]
    
    for i in result[-1][1:]:
        b *= i
    
    print(a)
    print(b)

# 만약 result에 값이 없다면, 즉 두 수의 공약수가 없다면 최대 공약수는 1, 최소 공배수는 두 수의 곱.
else:
    print(1)
    print(n*m)