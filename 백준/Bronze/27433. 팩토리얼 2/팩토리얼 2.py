N = int(input())

def factorial(N):
    if N in [0,1]:
        return 1
    return N*factorial(N-1)

print(factorial(N))