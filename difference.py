x,y=input().split()
while len(x)<len(y):
  for i in range(0,len(y)):
    try:
      s+=abs(ord(x[i])-ord(y[i]))
    except IndexError:
      s+=ord(y[i])-ord('a')+1
else:
   for i in range(0,len(x)):
    try:
      s+=abs(ord(x[i])-ord(y[i]))
    except IndexError:
      s+=ord(x[i])-ord('a')+1
  
