N = int(input())
result = []
for i in range(N):
    info = input().split()
    result.append([info[0], int(info[1]), int(info[2]), int(info[3])])

# 문자형 숫자 주의
# '20' > '110'
    
# 1, 2번 조건만 생각해보자 -> 전체적으로 국어는 내림차순이고 일부 영어만 오름차순이어야함.
# 국어 내림차순 정렬 후 영어 오름차순 정렬을 적용하면 정렬된 전체적인 국어의 순서가 흐트러짐
# 반대로, 영어 오름차순 정렬을 먼저 적용하면 이 때 같은 국어점수들만 보면 영어는 오름차순임.
# 여기서 국어 내림차순 정렬을 적용하면 전체적으로 국어는 내림차순이고 같은 국어점수들간의 순서는 변하지 않음. 대응되는 국어점수들은 오름차순.

result.sort(key = lambda x: x[0])
result.sort(key = lambda x: x[3], reverse=True)
result.sort(key = lambda x: x[2])
result.sort(key = lambda x: x[1], reverse=True)

# 이 방법도 가능
# sort의 디폴트는 오름차순. 음수를 오름차순 하는 건 해당하는 양수의 내림차순과 같은 의미.
#result.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in result:
    print(i[0])