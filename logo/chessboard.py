import math

def isPrime(n):
  i = 2
  if i > math.sqrt(n):
    print "POO"
  elif n % i == 0:
    print "False"
  else:
    i = i + 1
    isPrime (n)
    
print (isPrime(76))
    