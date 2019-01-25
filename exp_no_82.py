a,b=input().split()
if type(a) and type(b)==int:
  x=int(a)*int(b)
else:
  x=float(a)*float(b)
print("{:.5f}".format(x))
