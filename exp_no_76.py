N=int(input())
flag=0
for i in range(2,N):
  if N%i==0:
    flag=1
    break
  else:flag=0
if flag==1:
  print('yes')
else:print('no')
