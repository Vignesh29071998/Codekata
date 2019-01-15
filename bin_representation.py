n=input()
flag=0
for i in n:
  if i=='0' or i=='1':
    flag=0
  else:
    flag=1
    break
if flag==0:
  print('yes')
else:
  print('no')
