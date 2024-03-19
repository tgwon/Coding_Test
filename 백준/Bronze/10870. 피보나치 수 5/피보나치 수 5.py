def func(k):
    if k in [0,1]:
        return k
    return func(k-1) + func(k-2)
n = int(input())
print(func(n))