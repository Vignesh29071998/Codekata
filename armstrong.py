n=int(input())
a=n
s=0
while n>0:
  b=n%10
  s+=b**3
  n=n//10
if s==a:
  print("yes")
else:
  print("no")
