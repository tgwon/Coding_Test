result = []

while True:
    value = input()
    if value == '.':
        break
    else:
        result.append(value)

for i in result:
    stack = []
    others = []
    for j in i:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
                pass
        elif j == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(j)
            
    if len(stack) == 0:
        print('yes')
    
    else:
        print('no')