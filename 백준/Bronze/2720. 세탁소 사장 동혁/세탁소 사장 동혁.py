t = int(input())
array = [25,10,5,1]

for i in range(t):
    money = int(input())
    for j in array:
        print(money//j, end = ' ')
        money %= j