num = int(input())
for i in range(num):
    word = input()
    result = 0
    weight = 1
    for i in range(len(word)):
        if word[i] == 'O':
            result += 1*weight
            weight += 1
        else:
            weight = 1
    print(result)