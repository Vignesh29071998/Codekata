a=int(input())
a1=[]
for i in range(1,a+1):
  if a%i==0:
    a1.append(i)
for i in range(0,len(a1)):
  print(a1[i],end=' ')
  
