N,K=map(int,input(),split())
N1=map(int,input().split())
if N1[K]%2!=0:
  print(N1[K])
else:
  print(N1[K-1])
