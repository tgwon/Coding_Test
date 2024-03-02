word = input().upper()
result = {}
for i in word:
    try:
        result[i] += 1
    except:
        result[i] = 1
        
if list(result.values()).count(max(result.values())) != 1:
    print('?')
else:
    print([k for k,v in result.items() if v == max(result.values())][0])