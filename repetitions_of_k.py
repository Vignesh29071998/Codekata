a,b=map(int,input().split())
n=list(map(int,input().split()))
li=[0]*10
for i in range(0,len(n)):
  li[n[i]]+=1
print(li[b])
