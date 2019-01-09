n=int(input())
a,b=0,1
l=[]
for i in range(1,n+1):
  if i==1:
    l.append(i)
  else:
    c=a+b
    b=c
    a=b
    l.append(c)
for i in range(0,len(l)):
  if i==len(l)-1:
    print(i)
  else:
    print(i,end=' ')
    
