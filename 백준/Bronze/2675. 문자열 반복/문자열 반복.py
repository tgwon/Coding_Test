T = int(input())

for i in range(T):
    result = []
    S, R = input().split()
    for j in range(len(R)):
        result.append(R[j]*int(S))
    print(''.join(result))
        