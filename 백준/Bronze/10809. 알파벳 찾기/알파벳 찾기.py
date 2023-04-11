S = input()
list = []
for i in range(len(S)):
    list.append(S[i])
for i in range(26):
    try:
        print(list.index(chr(97+i)), end=' ')
    except:
        print(-1, end=' ')