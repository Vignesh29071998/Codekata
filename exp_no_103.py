st=input()
l=[x.title() for x in st.split()]
for i in range(0,len(l)):
  if i==len(l)-1:
    print(l[i])
  else:
    print(l[i],end=' ')
