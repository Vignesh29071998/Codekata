import collections
s=input()
flag=0
a=collections.Counter(s)
for i in a:
  if a[i]==1:
    flag=0
  else:
    flag=1
    break
if flag==0:
  print('Yes')
else:
  print('No')
  
