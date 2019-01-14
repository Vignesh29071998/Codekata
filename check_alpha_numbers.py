import re
n=input()
if re.search("\w",n) is not None:
  print('Yes')
else:
  print('No')
