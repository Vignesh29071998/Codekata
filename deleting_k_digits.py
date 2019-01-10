from itertools import combinations
a,b=map(int,input().split())
n,c=[],[]
if b==0:
  print(a)
else:
  d=str(a)
  n=list(combinations(list(d),len(d)-b))
  for i in n:
    c.append(''.join(i))
  print(min(c))
    
  
