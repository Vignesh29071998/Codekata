a = input()
try:
  a = int(a)
  print("Yes")
except ValueError:
  try:
    a = float(a)
    print("yes")
  except ValueError:
    print("No")
