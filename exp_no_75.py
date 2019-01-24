s=input()
s1=''
if len(s)%2!=0:
  a=len(s)//2
  for i in range(0,len(s)):
    if i==a:
      s1+='*'
    else:s1+=s[i]
else:
  a=len(s)//2
  for i in range(0,len(s)):
    if i==a or i==a-1:
      s1+='*'
    else:
      s1+=s[i]
print(s1)
      
