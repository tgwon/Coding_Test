while True:
    n = input()
    if n == '0':
        break
    else:
        if n[::-1] == n:
            print('yes')
        else:
            print('no')