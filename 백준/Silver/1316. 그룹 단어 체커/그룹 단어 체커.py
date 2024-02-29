num = int(input())
group_word = num

for i in range(num) :
    w1 = input()
    for j in range(len(w1)-1) :
        if w1[j] == w1[j+1] :
            continue
        elif w1[j] in w1[j+1:] :
            group_word -= 1
            break
print(group_word)