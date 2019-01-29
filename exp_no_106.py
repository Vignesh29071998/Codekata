N,K=map(int,input().split())
N1=list(map(int,input().split()))
N1=sorted(N1)
if N1[K]%2!=0:
  print(N1[K])
else:
  if N1[K+1]%2!=0:
    print(N1[K+1])
  elif N1[K-1]%2!=0: 
    print(N1[K-1])
