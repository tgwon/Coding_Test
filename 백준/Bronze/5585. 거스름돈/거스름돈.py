n = int(input())
n = 1000-n
coin_type = [500,100,50,10,5,1]
count = 0

for i in coin_type:
    count += n//i
    n = n%i
    
print(count)