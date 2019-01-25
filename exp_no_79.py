n,m=map(int,input().split())
x=(n*m)**(1/2)
if n%x==0 or m%x==0:
  print('yes')
else:
  print('no')
