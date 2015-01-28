def trapeziumRule(a,b,n):
  a=0
  b=0.5
  n=5
  h=(b-a)/n
  v=((1+(a**3))**0.5)+((1+(b**3))**0.5)
  for i in range(1,n):
     v += 2*((1+(a+(i*h))**3)**0.5)
  t=(h/2)*v
  f=2**0.5
  return trap
print trap