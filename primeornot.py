#hello
n=int(input())
for i in range(2,n):
    if n%i==0:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("no")
else:
    print("yes")
    
