n=input()
if n in ['a','e','i','o','u']:
  print("Vowel")
else:
  n=ord(n)
  if n in range(97,123):
    print("Consonant")
  else:
    print("invalid")
  
