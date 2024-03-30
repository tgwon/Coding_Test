n = int(input())

value = 1
while True:
    count = int(value)
    count += sum(map(int, str(value)))
    
    if count == n:
        print(value)
        break
    elif value == n:
        print(0)
        break
    else:
        value += 1