n=input()
n=list(n)
c=0
for i in n:
  if i.isalnum() or i==' ':
    continue
  else:
    c+=1
print(c)
