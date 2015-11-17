import math

def isPrime(n):
  i = 2
  if n > math.sqrt(n):
    print "True"
  elif n % i == 0:
    print "False"
  else:
    i = i + 1
    isPrime (n)
    
print (isPrime(66))
    