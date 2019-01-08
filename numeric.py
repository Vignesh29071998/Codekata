a = input()
try:
  a = int(a)
  print("yes")
except ValueError:
  try:
    a = float(a)
    print("yes")
  except ValueError:
    print("no")
