A,B,C=map(int,input().split())
s1=A
s=0
for i in range(1,C):
  A+=B
  s+=A
print(s+s1)
  
