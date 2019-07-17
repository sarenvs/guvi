b=input()
a=len(b)
ba=b[::-1]
if b==ba:
  print(b[:a-1])
else:
  print(b)
