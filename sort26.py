n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
for i in range(0,len(l)):
  if i==len(l)-1:
    print(l[i])
  else:
    print(l[i],end=' ')
  
  
