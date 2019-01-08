a,b=map(int,input().split())
l=[]
for i in range(a+1,b):
  c=i
  s=0
  while i>0:
    d=i%10
    s+=d**3
    i=i//10
  if s==c:
    l.append(s)
for i in range(0,len(l)):
  if i==len(l)-1:
    print(l[i])
  else:
    print(l[i],end=' ')
  
    
  
    
