num = input()
left = 0
right = 0

for i in range(len(num)//2):
    right += int(num[:len(num)//2][i])
    left += int(num[len(num)//2:][i])

if right == left:
    print('LUCKY')
else:
    print('READY')