n = int(input())
array = list(map(int, input().split()))

# 한 명씩만 설 수 있는 공간
wait = []

num = 1

# 1부터 1씩 늘리면서 비교
# 순서가 아나라면 대기 장소에 넣기
while array:
    if array[0] == num:
        num += 1
        array.pop(0)
    else:
        wait.append(array.pop(0))
        
    while wait:
        if wait[-1] == num:
            num += 1
            wait.pop()
        else:
            break

if len(wait) == 0: 
    print('Nice')
else:
    print('Sad')