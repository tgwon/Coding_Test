result = []
for i in range(3):
    result.append(int(input()))

if sum(result) == 180:
    if len(set(result)) == 3:
        print('Scalene')
    elif len(set(result)) == 2:
        print('Isosceles')
    else:
        print('Equilateral')
else:
    print('Error')