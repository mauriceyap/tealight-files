def trapeziumRule(a,b,n):
  h=(b-a)/n
  v=((1+(a**3))**0.5)+((1+(b**3))**0.5)
  for i in range(1,n):
     v += 2*((1+(a+(i*h))**3)**0.5)
  t=(h/2)*v
  f=2**0.5
  return t
print trapeziumRule(0.0,1,1024)