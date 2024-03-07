N = int(input())
count = 1
result = 0
while True:
    if N <= count:
        print(result+1)
        break
    else:
        result += 1
        count += 6*result