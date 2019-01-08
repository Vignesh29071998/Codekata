n=int(input())
l=[]
for i in range(1,6):
  l.append(n*i)
for i in range(0,len(l)):
  if i==len(l)-1:
    print(l[i])
  else:
    print(l[i],end=' ')
  
  
