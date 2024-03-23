from collections import Counter
import sys

input = sys.stdin.readline

input()
list1 = list(map(int,input().split()))
input()
list2 = list(map(int,input().split()))

cnt_dict = Counter(list1)

for i in list2:
    if i in cnt_dict:
        print(cnt_dict[i], end = ' ')
    else:
        print(0, end = ' ')