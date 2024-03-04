final_num = 1
for i in range(3):
    num = int(input())
    final_num *= num
for i in range(0,10):
    print(str(final_num).count(str(i)))