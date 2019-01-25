st=int(input())
a=[]
for i in str(st):
  if int(i)%2!=0:
    a.append(int(i))
for i in range(0,len(a)):
  if i==len(a)-1:
    print(a[i])
  else:
    print(a[i],end=' ')
    
