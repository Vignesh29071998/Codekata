#hello
a,b=map(int,input().split())
l=[]
for i in range(a+1,b):
  if i%2!=0:
    l.append(i)
for j in range(0,len(l)):
  if j==len(l)-1:
    print(l[j])
  else:
    print(l[j],end=' ')
