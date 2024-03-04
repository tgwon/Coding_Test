num = list(input().split())
square = 0
for i in num:
    square += int(i)**2
print(square%10)