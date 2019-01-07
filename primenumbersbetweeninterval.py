a,b=map(int,input().split())
flag=0
for i in range(a+1,b):
  for j in range(2,i):
    if i%j==0:
      flag=1
      break
    else:
      flag=0
  if flag==0:
    print(i,end=' ')
