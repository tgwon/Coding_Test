def solution(N, stages):
    result = []
    stages.sort()
    for i in range(1,N+1):
        try:
            fail_rate = stages.count(i)/len(stages[stages.index(i):])
        except:
            fail_rate = 0
        result.append((i,fail_rate))
    result.sort(key = lambda x: x[1], reverse=True)
    return [i for i,k in result]
solution(5, [2,1,2,6,2,5,3,3])