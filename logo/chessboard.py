import math
n = 72

def isPrime (n):
  i = 2
  if n > math.sqrt(n):
    print "True"
  elif (n mod i) = 0:
    print "False"
  else:
    i = i + 1
    isPrime (n)
    