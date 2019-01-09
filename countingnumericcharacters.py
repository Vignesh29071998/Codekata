n=input()
n=list(n)
c=0
for i in n:
  if int(i).isdigit():
    c+=1
print(c)
