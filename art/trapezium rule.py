a=0.5
b=0
n=5
def trapeziumRule(a,b,n):
  h=(b-a)/n
  t=((1+a^3)^0.5)+((1+b^3)^0.5)
  for i in range (1,n):
    t += 2*((1+(a+(i*h))^3)^0.5)
  return (h/2)*t
print trapeziumRule