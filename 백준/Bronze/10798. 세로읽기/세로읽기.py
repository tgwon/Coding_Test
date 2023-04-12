result = [0]*5
for i in range(5):
    list = []
    a= input()
    for j in range(len(a)):
        list.append(a[j])
    result[i] = list

for i in range(len(max(result, key=len))):
    for j in range(5):
        try:
            print(result[j][i], end='')
        except:
            print('',end='')

    