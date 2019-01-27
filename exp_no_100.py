nu=int(input())
s=1
while nu>0:
  a=nu%10
  s*=a
  nu=nu//10
print(nu)
