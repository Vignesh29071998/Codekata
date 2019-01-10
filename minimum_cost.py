x,y=input().split()
c=0
if len(x)<len(y):
  for i in range(0,len(y)):
    try:
      if x[i]!=y[i]:
        x.replace(x[i],y[i])
        c+=1
    except IndexError:
      x+=y[i]
      c+=1
  print(c)
else:
  for i in range(0,len(x)):
    try:
      if x[i]!=y[i]:
        x.replace(x[i],y[i])
        c+=1
    except IndexError:
      c+=len(x)-i
      print(c)
      break
    
