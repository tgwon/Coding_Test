while True:
    cnt = 0
    sent = input()
    if sent == '#':
        break
    else:
        for i in ['a','e','i','o','u','A','E','I','O','U']:
            cnt += sent.count(i)
        print(cnt)