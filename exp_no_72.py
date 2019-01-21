s=input()
flag=0
for i in s:
  if i.lower() in ['a','e','i','o','u']:
    flag=1
    break
  else:
    flag=0
if flag==1:
  print('yes')
else:print('no')
