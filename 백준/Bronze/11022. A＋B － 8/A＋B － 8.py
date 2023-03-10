T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    x = i + 1
    C = a+b
    print(f"Case #{x}:", a , "+" , b ,f"= {C}")