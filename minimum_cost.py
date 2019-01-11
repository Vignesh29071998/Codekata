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
  i,j=0,0
  x=list(x)
  y=list(y)
  while i<len(x) and j<len(y):
    if x[i]==y[j]:
      i+=1
      j+=1
    else:
      x.pop(0)
      c+=1
  print(c+len(x[i:]))
