#hello 
a,b=map(int,input().split())
flag=0
l=[]
for i in range(a+1,b):
  for j in range(2,i):
    if i%j==0:
      flag=1
      break
    else:
      flag=0
  if flag==0:
    l.append(i)
for k in range(0,len(l)):
  if k==len(l)-1:
    print(l[k])
  else:
    print(l[k],end=' ')
