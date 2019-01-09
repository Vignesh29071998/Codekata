n=int(input())
a,b=0,1
l=[]
for i in range(1,n+1):
  if i==1:
    l.append(i)
  else:
    c=a+b
    a=b
    b=c
    l.append(c)
for i in range(0,len(l)):
  if i==len(l)-1:
    print(l[i])
  else:
    print(l[i],end=' ')
    
