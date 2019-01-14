import re
n=input()
if re.search("[a-zA-Z]",n) is not None:
    if re.search("[0-9]",n) is not None:
        print('Yes')
    else:
        print('No')
    
