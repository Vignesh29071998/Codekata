n1,n2=map(int,input().split())
if n1>n2:
  n3=n1
else:
  n3=n2
while(True):
  if n3%n1==0 and n3%n2==0:
    lcm=n3
    break
  n3+=1
print(n3)
