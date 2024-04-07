x,y,z=sorted(map(int,input().split()))
print(x+y+min(x+y-1,z))