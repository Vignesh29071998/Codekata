n=int(input())
n1=input().split()
for i in range(0,n-1):
  if n1[i]>n1[i+1]:
    print(i)
    break
    
