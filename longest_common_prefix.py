n=int(input())
a=[]
s=''
m=100
for i in range(0,n):
    a.append(input())
for i in range(0,len(a)):
    if len(a[i])<m:
        m=len(a[i])
        c=a[i]
a.remove(c)
i=1
while i<=len(a):
    if s=='':
        for j in range(0,len(c)):
                if c[j]==a[i-1][j]:
                    s+=c[j]
                else:
                    break
    
    else:
        d=s
        s=''
        for j in range(0,len(d)):
            if d[j]==a[i-1][j]:
                s+=d[j]
            else:
                break
    i+=1
print(s)
            
