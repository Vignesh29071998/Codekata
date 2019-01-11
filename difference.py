x,y=input().split()
s=0
if len(x)<len(y):
  for i in range(0,len(y)):
    if i<=len(x)-1:
      s+=abs(ord(x[i])-ord(y[i]))
    else:
      s+=ord(y[i])-ord('a')+1
else:
   for i in range(0,len(x)):
    if i<=len(y)-1:
      s+=abs(ord(x[i])-ord(y[i]))
    else:
      break
print(s)
