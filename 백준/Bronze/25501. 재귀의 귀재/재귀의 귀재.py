t = int(input())
count = 0
def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return print(recursion(s, 0, len(s)-1), count)

for _ in range(t):
    isPalindrome(input())
    count = 0