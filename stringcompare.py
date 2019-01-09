a,b=input().split()
if len(a)>len(b):
  print(a)
elif len(b)>len(a):
  print(b)
else:
  if len(a)//2==1:
    print(a)
  elif len(a)//2==2:
    print(b)
  else:
    print(b)
