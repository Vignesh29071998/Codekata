s=input()
if '/' in s:
  k=s.split('/')
  print(int(k[0])//int(k[1]))
else:
  k=s.split('%')
  print(int(k[0])%int(k[1]))
