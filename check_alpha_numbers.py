import re
n=input()
if re.search("[a-zA-Z][0-9]",n) is not None:
  print('Yes')
else:
  print('No')
